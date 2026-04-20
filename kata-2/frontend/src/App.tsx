import { useEffect, useState } from "react";
import axios from "axios";
import type { Task } from "../types/tarefas";
import "./App.css";
import { Filter } from "lucide-react";

export default function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [titulo, setTitulo] = useState("");


  const [filter, setFilter] = useState<"all" | "a_fazer" | "concluida">("all");
  const [openFilter, setOpenFilter] = useState(false);

  const fetchTasks = async () => {
    const res = await axios.get<Task[]>("http://127.0.0.1:5000/tasks");
    setTasks(res.data);
  };

  const createTask = async () => {
    if (!titulo.trim()) return;

    await axios.post("http://127.0.0.1:5000/tasks", {
      tituloTarefa: titulo,
      status: "a_fazer",
      prioridade: 1
    });

    setTitulo("");
    fetchTasks();
  };

  const deleteTask = async (id: number) => {
    await axios.delete(`http://127.0.0.1:5000/tasks/${id}`);
    fetchTasks();
  };

  const toggleTask = async (task: Task) => {
    const novoStatus =
      task.status === "concluida" ? "a_fazer" : "concluida";

    await axios.patch(`http://127.0.0.1:5000/tasks/${task.idTarefa}`, {
      status: novoStatus
    });

    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // 🔎 FILTRO
  const filteredTasks =
    filter === "all"
      ? tasks
      : tasks.filter((t) => t.status === filter);

  return (
    <div className="app">

      <header className="header">
        <h2>TaskFlow</h2>
      </header>

      <div className="container">

        {/* LEFT */}
        <div className="left">
          <h1>Organize suas tarefas</h1>
          <p>Simples, rápido e eficiente.</p>

          <div className="inputBox">
            <input
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              placeholder="Digite uma tarefa..."
            />
            <button onClick={createTask}>Criar</button>
          </div>
        </div>

        {/* RIGHT */}
        <div className="right">
          <div className="tasksHeader">
            <h2>Suas tarefas</h2>

            <div className="filterWrapper">
              <Filter
                size={20}
                className="filterIcon"
                onClick={() => setOpenFilter(!openFilter)}
              />

              {openFilter && (
                <div className="filterDropdown">
                  <div onClick={() => { setFilter("all"); setOpenFilter(false); }}>
                    Todas
                  </div>
                  <div onClick={() => { setFilter("a_fazer"); setOpenFilter(false); }}>
                    Pendentes
                  </div>
                  <div onClick={() => { setFilter("concluida"); setOpenFilter(false); }}>
                    Concluídas
                  </div>
                </div>
              )}
            </div>
          </div>

          {filteredTasks.map((task) => (
            <div key={task.idTarefa} className="taskItem">
              <span className={task.status === "concluida" ? "done" : ""}>
                {task.tituloTarefa}
              </span>

              <div className="actions">
                <button onClick={() => toggleTask(task)}>
                  {task.status === "concluida" ? "↩" : "✔"}
                </button>
                <button onClick={() => deleteTask(task.idTarefa)}>✖</button>
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}