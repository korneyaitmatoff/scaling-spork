import abc


class AbstractService(abc.ABC):
    @abc.abstractmethod
    def create(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def all(self, limit: int = 100, offset: int = 0):
        raise NotImplementedError

    @abc.abstractmethod
    def read_by(self, entity, filters):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, eid, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, eid):
        raise NotImplementedError
