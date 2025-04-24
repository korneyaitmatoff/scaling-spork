from datetime import datetime

from pydantic import BaseModel


class Protocol(BaseModel):
    id: int | None = None
    number: str
    doc_date: datetime = datetime.now()
    maintainer_id: int
    vote_id: int
    budget_amount: int
    vote_json: dict
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()
