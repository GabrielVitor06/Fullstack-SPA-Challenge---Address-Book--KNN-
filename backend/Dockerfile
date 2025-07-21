# # Dockerfile
# FROM python:3.11-slim

# # Criar diretório de trabalho
# WORKDIR /app

# # Copiar arquivos
# COPY ./requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copiar tudo (cuidado com .dockerignore)
# COPY . .

# # Rodar o FastAPI com Uvicorn
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
