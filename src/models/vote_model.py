from datetime import datetime
from typing import Any

from pydantic import BaseModel

"""
     id serial primary key,
    maintainer_id int references employees(id),
    votes_json jsonb default null,
    created_at timestamp default now(),
    changed_at timestamp default now()
"""


class Vote(BaseModel):
    id: int
    maintainer_id: int
    votes_json: dict[str, Any]
    created_at: datetime = datetime.now()
    changed_at: datetime = datetime.now()
