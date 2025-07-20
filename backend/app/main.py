from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import models
from app.core import database
from app.api.v1 import contacts  # importa o módulo que tem router

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

app.include_router(contacts.router, prefix="/contacts", tags=["Contacts"])
