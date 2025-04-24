from datetime import datetime
from typing import Any

from pydantic import BaseModel


class Student(BaseModel):
    id: int | None = None
    name: str
    group_code: str
    inn: str
    is_resident: bool
    passport_data: dict[str, Any]
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()
