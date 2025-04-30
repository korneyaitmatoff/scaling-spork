from sqlalchemy import (
    Integer,
    DateTime,
    ForeignKey,
    JSON
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.database.models import Base


class Vote(Base):
    __tablename__ = "votes"

    id: Mapped[int] = mapped_column(primary_key=True)
    maintainer_id: Mapped[int] = mapped_column(ForeignKey(column="employees.id"))
    votes_json: Mapped[JSON] = mapped_column(JSON)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    changed_at: Mapped[DateTime] = mapped_column(DateTime)
