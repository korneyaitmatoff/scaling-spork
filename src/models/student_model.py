from datetime import datetime
from typing import Any, TypedDict

from pydantic import BaseModel

class StudentRequest(BaseModel):
    name: str
    group_code: str
    inn: str
    is_resident: bool
    passport_data: TypedDict("Dict", {"serial_number": str, "birthdate": str})

class StudentBatch(BaseModel):
    batch: list[StudentRequest]

class OverviewStudent(BaseModel):
    name: str
    group_code: str
    inn: str
    is_resident: bool
    passport_data: TypedDict("Dict", {"serial_number": str, "birthdate": str})
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()



class Student(BaseModel):
    id: int | None = None
    name: str
    group_code: str
    inn: str
    is_resident: bool
    passport_data: TypedDict("Dict", {"serial_number": str, "birthdate": str})
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()
