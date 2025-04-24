from datetime import datetime

from pydantic import BaseModel


class Employee(BaseModel):
    id: int | None = None
    name: str
    login: str
    password: str
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()
