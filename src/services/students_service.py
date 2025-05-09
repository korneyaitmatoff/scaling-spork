from typing import Any

from src.services.base_service import BaseService


class StudentsService(BaseService):
    def get_students_by_name(self, name: str) -> list[dict[str, Any]]:
        with self._repository as rep:
            return [
                {
                    key: value
                    for key, value in item._mapping["Student"].__dict__.items()
                    if key != '_sa_instance_state'
                }
                for item in rep.get(filters=(self._repository.entity.name.like(name),))
            ]