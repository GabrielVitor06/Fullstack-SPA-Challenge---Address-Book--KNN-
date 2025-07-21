# Fullstack SPA Challenge - Address Book (KNN)

Bem-vindo(a) ao desafio FullStack SPA da KNN!

Este projeto consiste em uma aplicação FullStack Single Page Application (SPA) para cadastro e consulta de contatos, com preenchimento automático de endereço via consulta de CEP.

---

## Tecnologias usadas

- **Frontend:** Vue 2 + TypeScript + Vuetify + Vuex + Vue Router
- **Backend:** FastAPI + SQLAlchemy 2.x + Pydantic v2 + PostgreSQL + Uvicorn
- **Banco de dados:** PostgreSQL
- **Extras:** Docker + Docker Compose (opcional)

---

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd Fullstack-SPA-Challenge-Address-Book-KNN

2. Configure a variável de ambiente do banco de dados
Crie um arquivo .env na raiz do projeto (ou na pasta backend) com o conteúdo:

DATABASE_URL=postgresql+asyncpg://postgres:523079GJ@db.xplpbktjaomsjvvygjwv.supabase.co:5432/postgres

3. Crie e ative seu ambiente virtual Python
No Linux/macOS:

python3 -m venv .venv
source .venv/bin/activate

python -m venv .venv
.venv\Scripts\activate
```

4. Instale as dependências e rode o backend

cd backend
pip install -r requirements.txt

# Caso tenha migrations:

python backend/migrate.py

# Inicie o backend

uvicorn app.main:app --reload
pytest tests

O backend estará disponível em http://127.0.0.1:8000

5. Instale as dependências e rode o frontend

cd frontend
npm install

# ou

yarn install

npm run serve

# ou

yarn serve

O frontend estará disponível em http://localhost:8080

6. Documentação da API
   Você pode acessar a documentação Swagger da API backend em:

http://127.0.0.1:8000/docs#

7. Rodando com Docker (opcional)
   Se preferir usar Docker, rode na raiz do projeto:

docker-compose up --build

Isso vai iniciar os serviços nas portas:

Backend: 8000
Frontend: 8080

Observações importantes

Lembre-se de criar o arquivo .env com sua URL do banco antes de iniciar o backend.
Nunca commit o .env para não expor suas credenciais.
Use a documentação Swagger para testar os endpoints.

# .env.example

# URL do banco PostgreSQL, use o formato:

# postgresql+asyncpg://<usuario>:<senha>@<host>:<porta>/<database>

DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@YOUR_HOST:5432/postgres
