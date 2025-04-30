import abc
from typing import Any


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: Any):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, filters):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, limit: int = 100, offset: int = 0):
        raise NotImplementedError
