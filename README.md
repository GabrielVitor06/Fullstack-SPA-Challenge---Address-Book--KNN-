<!-- ========== Clone o repositório: ========== -->

git clone <url-do-repositorio>
cd Fullstack-SPA-Challenge-Address-Book-KNN

<!-- ========== Configurar banco de dados PostgreSQL: ========== -->

DATABASE_URL = "postgresql+asyncpg://postgres:523079GJ@db.xplpbktjaomsjvvygjwv.supabase.co:5432/postgres"

<!-- ========== Crie e ative seu ambiente virtual: ========== -->

python -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows

<!-- ========== BACKEND ========== -->

Navegue para a pasta backend: cd backend

Instale dependências:

pip install -r requirements.txt

Rode as migrations/crie as tabelas (caso tenha script):

python backend/migrate.py

Inicie o backend:

uvicorn app.main:app --reload

<!-- ========== FRONTEND ========== -->

Navegue para a pasta frontend: cd frontend

Instale as dependências:

npm install
ou
yarn install

npm run serve
ou
yarn serve

<!-- ========== Docs swegger: ========== -->

http://127.0.0.1:8000/docs#
