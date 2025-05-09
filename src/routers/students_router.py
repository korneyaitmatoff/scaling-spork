from typing import Any

from src.routers import BaseRouter
from src.services import BaseService


class StudentsRouter(BaseRouter):
    def __init__(
            self,
            service: BaseService,
            overview_model,
            incoming_model=None,
            prefix: str = "/"
    ):
        super().__init__(service, overview_model, incoming_model, prefix)

        self.router.add_api_route(
            endpoint=self.get_students_by_name,
            path="/get_students_by_name/{name}",
            methods=["GET"]
        )

    def get_students_by_name(self, name: str) -> list[dict[str, Any]]:
        return self.service.get_students_by_name(name=name)
