from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.models.models import Contact

async def get_contacts(session: AsyncSession, skip: int = 0, limit: int = 10):
    result = await session.execute(select(Contact).offset(skip).limit(limit))
    return result.scalars().all()

async def get_contact(session: AsyncSession, contact_id: int):
    result = await session.execute(select(Contact).where(Contact.id == contact_id))
    return result.scalar_one_or_none()

async def create_contact(session: AsyncSession, contact: Contact):
    session.add(contact)
    await session.commit()
    await session.refresh(contact)
    return contact

async def update_contact(session: AsyncSession, contact_id: int, update_data: dict):
    await session.execute(update(Contact).where(Contact.id == contact_id).values(**update_data))
    await session.commit()

async def delete_contact(session: AsyncSession, contact_id: int):
    await session.execute(delete(Contact).where(Contact.id == contact_id))
    await session.commit()
