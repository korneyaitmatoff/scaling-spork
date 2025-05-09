from pydantic import BaseModel

from src.repository.sqlalchemy_repository import SqlAlchemyRepository
from src.services.abstract_service import AbstractService


class BaseService(AbstractService):
    def __init__(self, repository: SqlAlchemyRepository):
        self._repository = repository

    def create(self, batch: BaseModel):
        with self._repository as rep:
            return rep.add(batch=[batch.model_dump(mode="python")])

    def all(self, limit: int = 100, offset: int = 0):
        with self._repository as rep:
            return [
                [
                    {
                        key: value
                        for key, value in chunk_value.__dict__.items()
                        if key != "_sa_instance_state"
                    }
                    for _, chunk_value in chunk._mapping.items()
                ][0]
                for chunk in rep.list(limit=limit, offset=offset)
            ]

    def get_by_id(self, e_id: int):
        with self._repository as rep:
            return [
                [
                    {
                        key: value
                        for key, value in chunk_value.__dict__.items()
                        if key != "_sa_instance_state"
                    }
                    for _, chunk_value in chunk._mapping.items()
                ][0]
                for chunk in rep.get(filters=(rep.entity.id == e_id,))
            ]

    def read_by(self, entity, filters):
        pass

    def update(self, eid, entity):
        pass

    def delete(self, eid):
        pass
