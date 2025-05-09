from datetime import datetime

from pydantic import BaseModel


class IncomingRequest(BaseModel):
    id: int | None = None
    student: int
    reason: str
    study_kind: str
    name: str
    is_commerce: bool
    faculty: str
    course: int
    group_code: str
    contract: str
    doc_date: datetime = datetime.now()
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()


class IncomingRequestOverview(BaseModel):
    id: int | None = None
    student: int
    reason: str
    study_kind: str
    name: str
    is_commerce: bool
    faculty: str
    course: int
    group_code: str
    contract: str
    doc_date: datetime = datetime.now()
    created_at: datetime = datetime.now()


class IncomingRequestRequest(BaseModel):
    reason: str
    study_kind: str
    student_name: str
    is_commerce: bool
    faculty: str
    course: int
    student_group_code: str
    contact: str
