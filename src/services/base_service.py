from pydantic import BaseModel

from src.repository.sqlalchemy_repository import SqlAlchemyRepository
from src.services.abstract_service import AbstractService


class BaseService(AbstractService):
    def __init__(self, repository: SqlAlchemyRepository):
        self._repository = repository

    def create(self, batch: list[BaseModel]):
        with self._repository as rep:
            return rep.add(batch=[chunk.model_dump(mode="python") for chunk in batch])

    def all(self, limit: int = 100, offset: int = 0):
        with self._repository as rep:
            return [chunk._mapping for chunk in rep.list(limit=limit, offset=offset)]

    def read_by(self, entity, filters):
        pass

    def update(self, eid, entity):
        pass

    def delete(self, eid):
        pass
