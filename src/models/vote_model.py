from datetime import datetime
from typing import Any

from pydantic import BaseModel


class Vote(BaseModel):
    id: int
    maintainer_id: int
    votes_json: dict[str, Any]
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()
