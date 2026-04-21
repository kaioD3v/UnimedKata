from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# conexão MySQL
def get_db():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )


# GET /tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    status = request.args.get("status")

    conn = get_db()
    cursor = conn.cursor()

    if status:
        cursor.execute("SELECT * FROM tarefa WHERE status = %s", (status,))
    else:
        cursor.execute("SELECT * FROM tarefa")

    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200


# POST /tasks

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "tituloTarefa" not in data or not data["tituloTarefa"].strip():
        return jsonify({"error": "Título é obrigatório"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tarefa (tituloTarefa, status, prioridade) VALUES (%s, %s, %s)",
        (
            data["tituloTarefa"],
            data.get("status", "a_fazer"),
            data.get("prioridade")
        )
    )

    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": task_id, "message": "Tarefa criada"}), 201



# PATCH /tasks/{id}

@app.route("/tasks/<int:id>", methods=["PATCH"])
def update_task(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    fields = []
    values = []

    # mapeamento correto dos nomes
    mapping = {
        "tituloTarefa": "tituloTarefa",
        "status": "status",
        "prioridade": "prioridade"
    }

    for key in mapping:
        if key in data:
            fields.append(f"{mapping[key]} = %s")
            values.append(data[key])

    if not fields:
        return jsonify({"error": "Nada para atualizar"}), 400

    values.append(id)

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        f"UPDATE tarefa SET {', '.join(fields)} WHERE idTarefa = %s",
        values
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Tarefa não encontrada"}), 404

    conn.close()
    return jsonify({"message": "Atualizada"}), 200



# DELETE /tasks/{id}

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tarefa WHERE idTarefa = %s", (id,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Tarefa não encontrada"}), 404

    conn.close()
    return jsonify({"message": "Deletada"}), 200



# RODAR

if __name__ == "__main__":
    app.run(debug=True)