from datetime import datetime

from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    login: str
    password: str

class EmployeeRequest(BaseModel):
    batch: list[Employee]

class OverviewEmployee(Employee):
    id: int | None = None
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()
