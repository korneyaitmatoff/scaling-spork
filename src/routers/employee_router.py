from typing import TypedDict

from pydantic import BaseModel

from src.routers import BaseRouter
from src.services import BaseService


class EmployeeRouter(BaseRouter):
    def __init__(self, service: BaseService, overview_model, incoming_model = None,
                 prefix: str = "/"):
        super().__init__(service, overview_model, incoming_model, prefix)


        self.router.add_api_route(endpoint=self.is_user_creds_correct, path="/is_user_creds_correct", methods=["POST"])

    def is_user_creds_correct(self, data: TypedDict("Dict", {"login": str, "password": str})) -> bool:
        print(self.service)
        print(self.service._repository)
        print(self.service._repository.entity)

        return self.service.is_user_creds_correct(login=data["login"], password=data["password"])
