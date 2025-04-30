from sqlalchemy.orm import DeclarativeBase

from src.repository.sqlalchemy_repository import SqlAlchemyRepository
from src.services.abstract_service import AbstractService


class BaseService(AbstractService):
    def __init__(self, repository: SqlAlchemyRepository, entity: DeclarativeBase):
        self.repository = repository
        self.entity = entity

    def create(self, entity):
        raise NotImplementedError

    def all(self, limit: int = 100, offset: int = 0):
        with self.repository as rep:
            return rep.list(limit=limit, offset=offset)

    def read_by(self, entity, filters):
        raise NotImplementedError

    def update(self, eid, entity):
        raise NotImplementedError

    def delete(self, eid):
        raise NotImplementedError
