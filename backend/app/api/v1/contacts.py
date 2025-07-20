from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import models
from app.core import database
from app.crud import crud
from app.schemas import schemas
from app.services import services

router = APIRouter()

@router.get("/contacts", response_model=list[schemas.ContactResponse])
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


@router.post("/contacts", response_model=schemas.ContactResponse, status_code=status.HTTP_201_CREATED)
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


@router.put("/contacts/{id}", response_model=schemas.ContactResponse)
async def update_contact(id: int, contact_update: schemas.ContactUpdate, session: AsyncSession = Depends(database.get_session)):
    existing = await crud.get_contact(session, id)
    if not existing:
        raise HTTPException(status_code=404, detail="Contato não encontrado")

    address = await services.get_address_from_cep(contact_update.cep)

    update_data = contact_update.dict(exclude_unset=True)
    update_data.update(address)

    await crud.update_contact(session, id, update_data)

    updated = await crud.get_contact(session, id)

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

@router.get("/contacts/{id}", response_model=schemas.ContactResponse)
async def get_contact_by_id(id: int, session: AsyncSession = Depends(database.get_session)):
    contact = await crud.get_contact(session, id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return schemas.ContactResponse(
        id=contact.id,
        name=contact.name,
        email=contact.email,
        phone=contact.phone,
        cep=contact.cep,
        address=schemas.Address(
            cep=contact.cep,
            logradouro=contact.logradouro,
            bairro=contact.bairro,
            cidade=contact.cidade,
            estado=contact.estado,
        ),
    )


@router.delete("/contacts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(id: int, session: AsyncSession = Depends(database.get_session)):
    existing = await crud.get_contact(session, id)
    if not existing:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    await crud.delete_contact(session, id)
    return


@router.get("/cep/{cep}")
async def get_address(cep: str):
    return await services.get_address_from_cep(cep)
