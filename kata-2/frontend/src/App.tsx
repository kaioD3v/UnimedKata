// Importações de bibliotecas, css e tipos
import { useEffect, useState } from "react";
import { createPortal } from "react-dom";
import axios from "axios";
import type { Task } from "../types/tarefas";
import "./App.css";
import { Filter, Check, RotateCcw, X, Pencil } from "lucide-react";

export default function App() {

  // State que armazena todas as tarefas
  const [tarefas, setTarefas] = useState<Task[]>([]);

  // state de input de criação da tarefa
  const [tituloTarefa, setTituloTarefa] = useState("");

  // state do filtro (todas, a fazer ou concluída)
  const [filtro, setFiltro] = useState<"todas" | "a_fazer" | "concluida">("todas");

  // controla se o floating do filtro está aberto
  const [filtroAberto, setFiltroAberto] = useState(false);

  // sabe se a tarefa está sendo editada
  const [tarefaEditando, setTarefaEditando] = useState<Task | null>(null);

  // state do input de edição
  const [tituloEdicao, setTituloEdicao] = useState("");

  // busca tarefas no backend
  const buscarTarefas = async () => {
    const res = await axios.get<Task[]>("http://127.0.0.1:5000/tasks");
    setTarefas(res.data);
  };

  // criar uma nova tarefa
  const criarTarefa = async () => {
    if (!tituloTarefa.trim()) return;

    await axios.post("http://127.0.0.1:5000/tasks", {
      tituloTarefa,
      status: "a_fazer",
      prioridade: 1,
    });

    setTituloTarefa("");
    buscarTarefas();
  };

  // deletar uma tarefa
  const deletarTarefa = async (id: number) => {
    await axios.delete(`http://127.0.0.1:5000/tasks/${id}`);
    buscarTarefas();
  };

  // alterna o status da tarefa
  const alternarStatusTarefa = async (tarefa: Task) => {
    const novoStatus =
      tarefa.status === "concluida" ? "a_fazer" : "concluida";

    await axios.patch(
      `http://127.0.0.1:5000/tasks/${tarefa.idTarefa}`,
      { status: novoStatus }
    );

    buscarTarefas();
  };

  // abre edição
  const abrirEdicao = (tarefa: Task) => {
    setTarefaEditando(tarefa);
    setTituloEdicao(tarefa.tituloTarefa);
  };

  // confirma edição
const confirmarEdicao = async () => {
  if (!tarefaEditando || !tituloEdicao.trim()) return;

  const tituloLimpo = tituloEdicao.trim();

  //  se for igual → só fecha
  if (tituloLimpo === tarefaEditando.tituloTarefa) {
    fecharModal();
    return;
  }

  // se mudou → salva e fecha
  await axios.patch(
    `http://127.0.0.1:5000/tasks/${tarefaEditando.idTarefa}`,
    { tituloTarefa: tituloLimpo }
  );

  fecharModal();
  buscarTarefas();
};

  const fecharModal = () => {
    setTarefaEditando(null);
    setTituloEdicao("");
  };

  // ESC pra fechar
  useEffect(() => {
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === "Escape") fecharModal();
    };

    document.addEventListener("keydown", handleEsc);
    return () => document.removeEventListener("keydown", handleEsc);
  }, []);

  // executa ao carregar
  useEffect(() => {
    buscarTarefas();
  }, []);

  // filtro
  const tarefasFiltradas =
    filtro === "todas"
      ? tarefas
      : tarefas.filter((t) => t.status === filtro);

  return (
    <div className="aplicacao">

      {/* header */}
      <header className="cabecalho">
        <h2>TaskFlow</h2>
      </header>

      <div className="containerPrincipal">

        {/* esquerda */}
        <div className="ladoEsquerdo">
          <h1>Organize suas tarefas</h1>
          <p>Simples, rápido e eficiente.</p>

          <div className="caixaInput">
            <input
              value={tituloTarefa}
              onChange={(e) => setTituloTarefa(e.target.value)}
              placeholder="Digite uma tarefa..."
            />
            <button onClick={criarTarefa}>Criar</button>
          </div>
        </div>

        {/* direita */}
        <div className="ladoDireito">

          <div className="cabecalhoTarefas">
            <h2>Suas tarefas</h2>

            <div className="wrapperFiltro">
              <Filter
                size={20}
                onClick={() => setFiltroAberto(!filtroAberto)}
              />

              {filtroAberto && (
                <div className="floatingFiltro">
                  <div onClick={() => { setFiltro("todas"); setFiltroAberto(false); }}>
                    Todas
                  </div>
                  <div onClick={() => { setFiltro("a_fazer"); setFiltroAberto(false); }}>
                    a Fazer
                  </div>
                  <div onClick={() => { setFiltro("concluida"); setFiltroAberto(false); }}>
                    Concluídas
                  </div>
                </div>
              )}
            </div>
          </div>

          {tarefasFiltradas.map((tarefa) => (
            <div key={tarefa.idTarefa} className="itemTarefa">

              <span className={tarefa.status === "concluida" ? "concluida" : ""}>
                {tarefa.tituloTarefa}
              </span>

              <div className="acoes">
                <button onClick={() => abrirEdicao(tarefa)}>
                  <Pencil size={15} />
                </button>

                <button onClick={() => alternarStatusTarefa(tarefa)}>
                  {tarefa.status === "concluida" ? (
                    <RotateCcw size={15} />
                  ) : (
                    <Check size={15} />
                  )}
                </button>

                <button onClick={() => deletarTarefa(tarefa.idTarefa)}>
                  <X size={15} />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* MODAL COM PORTAL */}
      {tarefaEditando &&
        createPortal(
          <div className="overlayEdicao" onClick={fecharModal}>
            <div
              className="modalEdicao animarEntrada"
              onClick={(e) => e.stopPropagation()}
            >
              <h3>Editar tarefa</h3>

              <input
                autoFocus
                value={tituloEdicao}
                onChange={(e) => setTituloEdicao(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && confirmarEdicao()}
                placeholder="Novo nome da tarefa..."
              />

              <div className="acoesEdicao">
                <button className="botaoCancelar" onClick={fecharModal}>
                  Cancelar
                </button>

                <button
                  className="botaoConfirmar"
                  onClick={confirmarEdicao}
                >
                  Salvar
                </button>
              </div>
            </div>
          </div>,
          document.body
        )}
    </div>
  );
}