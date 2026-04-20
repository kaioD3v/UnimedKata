import { useEffect, useState } from "react";
import axios from "axios";
import type { Task } from "../types/tarefas";

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [titulo, setTitulo] = useState("");

  // GET
  const fetchTasks = async () => {
    try {
      const res = await axios.get<Task[]>("http://127.0.0.1:5000/tasks");
      setTasks(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  // POST
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

  // DELETE
  const deleteTask = async (id: number) => {
    await axios.delete(`http://127.0.0.1:5000/tasks/${id}`);
    fetchTasks();
  };

  // PATCH (marcar como concluída)
  const completeTask = async (id: number) => {
    await axios.patch(`http://127.0.0.1:5000/tasks/${id}`, {
      status: "concluida"
    });
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>📋 Minhas Tarefas</h1>

      <input
        type="text"
        value={titulo}
        onChange={(e) => setTitulo(e.target.value)}
        placeholder="Digite uma tarefa..."
      />

      <button onClick={createTask}>Criar</button>

      <hr />

      {tasks.map((task) => (
        <div key={task.idTarefa}>
          <span
            style={{
              textDecoration:
                task.status === "concluida" ? "line-through" : "none"
            }}
          >
            {task.tituloTarefa} ({task.status})
          </span>

          <button onClick={() => completeTask(task.idTarefa)}>
            ✔
          </button>

          <button onClick={() => deleteTask(task.idTarefa)}>
            ❌
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;