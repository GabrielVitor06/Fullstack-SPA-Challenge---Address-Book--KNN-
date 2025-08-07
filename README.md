## Como rodar o projeto localmente

RECOMENDADO:  
RODAR: `docker-compose up --build` na raiz de tudo

Colocar o `.env` na raiz de tudo com a variável:

```
DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
```

Adicione isso no arquivo `.env` na raiz do frontend:

```
VUE_APP_API_BASE_URL=http://127.0.0.1:8000/api/v1
```

_(Utilizei Supabase)_

---

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd Fullstack-SPA-Challenge-Address-Book-KNN
```

---

### 2. Configure a variável de ambiente do banco de dados

Crie um arquivo `.env` na raiz do projeto com o conteúdo:

```
DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
```

---

### 3. Crie e ative seu ambiente virtual Python

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 4. Instale as dependências e rode o backend

```bash
cd backend
pip install -r requirements.txt
```

Caso tenha migrations:

```bash
python backend/migrate.py
```

Inicie o backend:

```bash
uvicorn app.main:app --reload
```

---

### 5. Inicie os testes (opcional)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest httpx pytest-asyncio
pytest -v
```

O backend estará disponível em:  
http://127.0.0.1:8000

---

### 6. Instale as dependências e rode o frontend

```bash
cd frontend
npm install
```

Certifique-se de adicionar o seguinte em um `.env` na raiz do frontend:

```
VUE_APP_API_BASE_URL=http://127.0.0.1:8000/api/v1
```

Ou:

```bash
yarn install
```

Execute o servidor:

```bash
npm run serve
# ou
yarn serve
```

O frontend estará disponível em:  
http://localhost:8080

---

### 7. Documentação da API

Você pode acessar a documentação Swagger da API backend em:

http://127.0.0.1:8000/docs#

---

### 8. Rodando com Docker (opcional)

Se preferir usar Docker, rode na raiz do projeto:

```bash
docker-compose up --build
```

Isso vai iniciar os serviços nas portas:

- Backend: 8000  
- Frontend: 8080

---

## Observações importantes

- Lembre-se de criar o arquivo `.env` com sua URL do banco antes de iniciar o backend.
- Use a documentação Swagger para testar os endpoints.

---

## .env.example

```env
# URL do banco PostgreSQL, use o formato:
# postgresql+asyncpg://<usuario>:<senha>@<host>:<porta>/<database>

DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}
```

```env
# Em frontend/.env
VUE_APP_API_BASE_URL=http://127.0.0.1:8000/api/v1
```

