from src.services.base_service import BaseService


class EmployeeService(BaseService):
    def is_user_creds_correct(self, login: str, password: str) -> bool:
        with self._repository as rep:
            return len(rep.get(filters=(
                self._repository.entity.login == login,
                self._repository.entity.password == password,
            ))) == 1
