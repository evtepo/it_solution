from uuid import UUID

from pydantic import BaseModel


class IdMixin(BaseModel):
    id: UUID

    class Config:
        from_attributes = True


class BaseMixin(BaseModel):
    title: str
    author: str
    views: int
    position: int


class CreateAdvertisement(BaseMixin): ...


class UpdateAdvertisement(IdMixin, BaseMixin): ...


class DeleteAdvertisement(IdMixin): ...


class ResponseAdvertisement(IdMixin, BaseMixin): ...
