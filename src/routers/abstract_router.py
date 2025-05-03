from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel


class AbstractRouter(ABC):
    @abstractmethod
    def get(self, eid: str | int):
        raise NotImplementedError

    @abstractmethod
    def list(self, limit: int = 100, offset: int = 0):
        raise NotImplementedError

    @abstractmethod
    def post(self, batch):
        raise NotImplementedError

    @abstractmethod
    def put(self, eid: int | str, entity: Any):
        raise NotImplementedError

    @abstractmethod
    def delete(self, eid: int | str):
        raise NotImplementedError
