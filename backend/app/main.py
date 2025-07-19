from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from app import models, schemas, crud, services, database

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

@app.get("/contacts", response_model=list[schemas.ContactResponse])
async def list_contacts(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(database.get_session)):
    contacts = await crud.get_contacts(session, skip, limit)
    return [
        schemas.ContactResponse(
            id=contact.id,
            name=contact.name,
            email=contact.email,
            phone=contact.phone,
            cep=contact.cep,
            address={
                "cep": contact.cep,
                "logradouro": contact.logradouro,
                "bairro": contact.bairro,
                "cidade": contact.cidade,
                "estado": contact.estado,
            }
        )
        for contact in contacts
    ]


@app.post("/contacts", response_model=schemas.ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(contact_create: schemas.ContactCreate, session: AsyncSession = Depends(database.get_session)):
    address = await services.get_address_from_cep(contact_create.cep)

    new_contact = models.Contact(
        name=contact_create.name,
        email=contact_create.email,
        phone=contact_create.phone,
        cep=contact_create.cep,
        logradouro=address.get("logradouro", ""),
        bairro=address.get("bairro", ""),
        cidade=address.get("cidade", ""),
        estado=address.get("estado", ""),
    )

    created = await crud.create_contact(session, new_contact)

    return schemas.ContactResponse(
        id=created.id,
        name=created.name,
        email=created.email,
        phone=created.phone,
        cep=created.cep,
        address=schemas.Address(
            cep=created.cep,
            logradouro=created.logradouro,
            bairro=created.bairro,
            cidade=created.cidade,
            estado=created.estado,
        )
    )


@app.put("/contacts/{id}", response_model=schemas.ContactResponse)
async def update_contact(id: int, contact_update: schemas.ContactUpdate, session: AsyncSession = Depends(database.get_session)):
    existing = await crud.get_contact(session, id)
    if not existing:
        raise HTTPException(status_code=404, detail="Contato não encontrado")

    # Busca o endereço atualizado pelo CEP
    address = await services.get_address_from_cep(contact_update.cep)

    # Prepara os dados para atualização
    update_data = contact_update.dict(exclude_unset=True)
    update_data.update(address)

    # Atualiza o contato no banco
    await crud.update_contact(session, id, update_data)

    # Busca o contato atualizado
    updated = await crud.get_contact(session, id)

    # Retorna o schema com o campo 'address' aninhado
    return schemas.ContactResponse(
        id=updated.id,
        name=updated.name,
        email=updated.email,
        phone=updated.phone,
        cep=updated.cep,
        address=schemas.Address(
            cep=updated.cep,
            logradouro=updated.logradouro,
            bairro=updated.bairro,
            cidade=updated.cidade,
            estado=updated.estado,
        )
    )


@app.delete("/contacts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(id: int, session: AsyncSession = Depends(database.get_session)):
    existing = await crud.get_contact(session, id)
    if not existing:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    await crud.delete_contact(session, id)
    return

@app.get("/cep/{cep}")
async def get_address(cep: str):
    return await services.get_address_from_cep(cep)
