from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from src.routers import AbstractRouter
from src.services import BaseService


class BaseRouter(AbstractRouter):

    def __init__(
            self,
            service: BaseService,
            overview_model: BaseModel,
            incoming_model: BaseModel = None,
            prefix: str = "/"
    ):
        self.service = service
        self.router = APIRouter(prefix=prefix)
        self.overview_model = overview_model

        self.router.add_api_route(endpoint=self.list, path="/", methods=["GET"])
        self.router.add_api_route(endpoint=self.get, path="/{id}", methods=["GET"])
        self.router.add_api_route(endpoint=self.post(incoming_model), path="/", methods=["POST"])

    def get(self, id: str | int):
        return self.service.get_by_id(e_id=id)

    def list(self, limit: int = 100, offset: int = 0):
        return self.service.all(limit=limit, offset=offset)

    def post(self, batch):
        def wrapper(batch_type: batch):
            self.service.create(batch=batch_type.batch)

        return wrapper

    def put(self, eid: int | str, entity: BaseModel):
        pass

    def delete(self, eid: int | str):
        pass
