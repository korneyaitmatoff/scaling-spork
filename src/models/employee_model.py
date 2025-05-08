from datetime import datetime

from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    login: str
    password: str


class EmployeeRequest(BaseModel):
    batch: list[Employee]


class OverviewEmployee(BaseModel):
    id: int | None = None
    name: str
    created_at: datetime = datetime.now()
