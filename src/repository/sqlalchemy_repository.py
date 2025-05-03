from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import select, insert

from src.repository.abstract_repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SqlAlchemyRepository, cls).__new__(cls)

        return cls._instance

    def __init__(self, engine, entity):
        self.engine = engine
        self.entity = entity
        self.session = None

    def __enter__(self):
        self.session = Session(self.engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def add(self, batch: list[dict[str, Any]]):
        self.session.execute(insert(self.entity), batch)
        self.session.commit()

    def get(self, filters=()):
        stmt = select(self.entity).filter(*filters)

        return self.session.execute(stmt).all()

    def list(self, limit: int = 100, offset: int = 0):
        stmt = select(self.entity).limit(limit).offset(offset)

        return self.session.execute(stmt).all()
