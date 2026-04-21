# Documentação – TaskFlow

Sistema de gerenciamento de tarefas (to-do list) com:

Frontend em React + TypeScript
Backend em Flask (Python)
Banco de dados MySQL

Permite:

Criar tarefas
Editar
Deletar
Marcar como concluída
Filtrar tarefas

# Pré-requisitos

Antes de rodar, precisa ter instalado e confifurado:

Node.js (recomendado 18+)
Python 3.10+
MySQL
Criar o banco no MySQL, (que está detro da pasta kata-2)
criar .env igual no arquivo .env_example

Backend (Flask)

1. Instalar dependências

# pip install flask flask-cors pymysql

2. Rodar o servidor

# python app.py

Vai subir em:

# http://127.0.0.1:5000 (local)

3. Configuração importante

No teu código muda a senha


# Frontend (React)

1. Instalar dependências
npm install

2. Rodar o projeto
npm run dev

3. API

O frontend já está configurado pra consumir (esse http vai de maquina pra maquina se a sua mudar altere):

http://127.0.0.1:5000/tasks

# Rotas da API

GET /tasks
POST /tasks
PATCH /tasks/{id}
DELETE /tasks/{id}

# Funcionalidades do Front

Criar tarefa

Editar com modal

Filtro (todas / a fazer / concluída)

UI responsiva e simples

# backend
python app.py

# frontend
npm install
npm run dev