from sqlalchemy import func, text
from src.models.incoming_request_model import IncomingRequestRequest
from src.services.base_service import BaseService


class IncomingRequestService(BaseService):
    def create_incoming_request(self, data: IncomingRequestRequest):
        with self._repository as rep:
            return rep.execute(
                statement=(
                    f"""
                    select
                        create_incoming_request(
                        reason =>'{data.reason}',
                        study_kind => '{data.study_kind}',
                        student_name => '{data.student_name}',
                        is_commerce => {data.is_commerce},
                        faculty => '{data.faculty}',
                        course => {data.course},
                        student_group_code => '{data.student_group_code}',
                        contact => '{data.contact}'
                    );
                """
                )
            )
