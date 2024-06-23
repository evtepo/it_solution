from uuid import UUID
from typing import Annotated

from fastapi import status, APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from connect.db_connect import get_session
from schemas import advertisement
from services import advertisement as services_advertisement
from repositories.base_repository import BaseRepository
from repositories.sqlalchemy_repository import get_repository


router = APIRouter()

session_dependency = Annotated[AsyncSession, Depends(get_session)]
repository_dependency = Annotated[BaseRepository, Depends(get_repository)]


@router.post(
    "/",
    response_model=advertisement.ResponseAdvertisement | dict[str, str],
    status_code=status.HTTP_201_CREATED,
)
async def create(
    data: advertisement.CreateAdvertisement,
    repository: repository_dependency,
    session: session_dependency,
):
    return await services_advertisement.create_advertisement(data, repository, session)


@router.get(
    "/",
    response_model=dict[str, dict | list[advertisement.ResponseAdvertisement | None]],
    status_code=status.HTTP_200_OK,
)
async def get(
    repository: repository_dependency,
    session: session_dependency,
    page: int = Query(ge=1, default=1),
    size: int = Query(ge=10, le=50, default=10),
):
    return await services_advertisement.get_advertisement(repository, session, page, size)


@router.get(
    "/{advertisement_id}",
    response_model=advertisement.ResponseAdvertisement | dict[str, str],
    status_code=status.HTTP_200_OK,
)
async def get_one(
    advertisement_id: UUID,
    repository: repository_dependency,
    session: session_dependency,
):
    return await services_advertisement.get_single_advertisement(advertisement_id, repository, session)


@router.put(
    "/",
    response_model=advertisement.ResponseAdvertisement | dict[str, dict],
    status_code=status.HTTP_200_OK,
)
async def update(
    data: advertisement.UpdateAdvertisement,
    repository: repository_dependency,
    session: session_dependency,
):
    return await services_advertisement.update_advertisement(data, repository, session)


@router.delete("/", response_model=dict[str, str], status_code=status.HTTP_200_OK)
async def delete(
    filters: advertisement.DeleteAdvertisement,
    repository: repository_dependency,
    session: session_dependency,
):
    return await services_advertisement.delete_advertisement(filters, repository, session)
