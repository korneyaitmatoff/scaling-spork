from src.models.incoming_request_model import IncomingRequestRequest
from src.routers import BaseRouter
from src.services import BaseService


class IncomingRequestRouter(BaseRouter):
    def __init__(self, service: BaseService, overview_model, incoming_model=None,
                 prefix: str = "/"):
        super().__init__(service, overview_model, incoming_model, prefix)

        self.router.add_api_route(endpoint=self.create_incoming_request, path="/create", methods=["POST"])

    def create_incoming_request(self, data: IncomingRequestRequest):
        self.service.create_incoming_request(data=data)
