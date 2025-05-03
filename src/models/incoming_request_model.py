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
    student: int
    reason: str
    study_kind: str
    name: str
    is_commerce: bool
    faculty: str
    course: int
    group_code: str
    contract: str
