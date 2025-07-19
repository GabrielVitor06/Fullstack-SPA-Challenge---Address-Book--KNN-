import asyncio
from app import crud, database

async def main():
    async with database.async_session() as session:
        contacts = await crud.get_contacts(session, skip=0, limit=10)
        for c in contacts:
            print(f"ID: {c.id}")
            print(f"Nome: {c.name}")
            print(f"Email: {c.email}")
            print(f"Telefone: {c.phone}")
            print(f"CEP: {c.cep}")
            print(f"Logradouro: {c.logradouro}")
            print(f"Bairro: {c.bairro}")
            print(f"Cidade: {c.cidade}")
            print(f"Estado: {c.estado}")
            print("-" * 30)

if __name__ == "__main__":
    asyncio.run(main())
