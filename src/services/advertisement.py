from uuid import UUID

from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from models.advertisement import Advertisement
from repositories.base_repository import BaseRepository
from schemas import advertisement


async def create_advertisement(
    data: advertisement.CreateAdvertisement,
    repository: BaseRepository,
    session: AsyncSession,
):
    return await repository.create(session, Advertisement, data.model_dump())


async def get_advertisement(
    repository: BaseRepository,
    session: AsyncSession,
    page: int,
    size: int,
):
    prev_page = page - 1 if page - 1 > 0 else None

    page = (page - 1) * size
    data = await repository.get(session, Advertisement, size, page)

    next_page = page + 1 if data and len(data) == size else None

    result = {
        "links": {
            "prev": prev_page,
            "next": next_page,
        },
    }
    result["data"] = data

    return result


async def get_single_advertisement(
    advertisement_id: UUID,
    repository: BaseRepository,
    session: AsyncSession,
):
    filters = {"id": advertisement_id}
    result = await repository.get_one(session, Advertisement, **filters)
    if not result:
        return JSONResponse(
            {"error": "An object with this identifier does not exist."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result


async def update_advertisement(
    data: advertisement.UpdateAdvertisement,
    repository: BaseRepository,
    session: AsyncSession,
):
    filters = {"id": data.id}
    update_result = await repository.update(session, Advertisement, data.model_dump(), **filters)
    if not update_result:
        return JSONResponse(
            {"error": "An object with this ID cannot be updated."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return update_result


async def delete_advertisement(
    filters: advertisement.DeleteAdvertisement,
    repository: BaseRepository,
    session: AsyncSession,
):
    await repository.delete(session, Advertisement, **filters.model_dump())
    return {"msg": "Succesfully deleted."}
