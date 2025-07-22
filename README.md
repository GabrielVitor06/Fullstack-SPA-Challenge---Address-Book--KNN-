## Como rodar o projeto localmente

RECOMENDADO:
RODAR: docker-compose up --build na raiz de tudo

Colocar o .env na raiz de tudo com a
DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}

Adicione isso VUE_APP_API_BASE_URL=http://127.0.0.1:8000/api/v1 em um .env na raiz do frontend

(Utilizei Supabase)

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd Fullstack-SPA-Challenge-Address-Book-KNN

2. Configure a variável de ambiente do banco de dados
Crie um arquivo .env na raiz do projeto com o conteúdo:

DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}

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

# Inicie o teste

python3 -m venv .venv
source .venv/bin/activate
pip install pytest httpx pytest-asyncio
pytest -v

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
Use a documentação Swagger para testar os endpoints.

# .env.example

# URL do banco PostgreSQL, use o formato:

Usei Supabase

# postgresql+asyncpg://<usuario>:<senha>@<host>:<porta>/<database>

DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
