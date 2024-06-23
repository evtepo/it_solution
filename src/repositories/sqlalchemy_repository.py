from typing import TypeVar

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models.advertisement import Advertisement
from repositories.base_repository import BaseRepository


Model = TypeVar("Model", Advertisement, ...)


class SqlAlchemyRepository(BaseRepository):
    async def create(self, session: AsyncSession, model: Model, data: dict):
        instance = model(**data)
        session.add(instance)
        await session.commit()

        return instance

    async def get(self, session: AsyncSession, model: Model, limit: int, offset: int):
        query = select(model).limit(limit).offset(offset)
        res = await session.execute(query)

        return res.scalars().all()

    async def get_one(self, session: AsyncSession, model: Model, **filters):
        query = select(model).filter_by(**filters)
        res = await session.execute(query)

        return res.scalar_one_or_none()

    async def update(self, session: AsyncSession, model: Model, data: dict, **filters):
        query = update(model).values(**data).filter_by(**filters).returning(model)
        res = await session.execute(query)
        await session.commit()

        return res.scalar_one_or_none()

    async def delete(self, session: AsyncSession, model: Model, **filters):
        query = delete(model).filter_by(**filters)
        await session.execute(query)
        await session.commit()


repository: BaseRepository | None = SqlAlchemyRepository()


async def get_repository():
    return repository
