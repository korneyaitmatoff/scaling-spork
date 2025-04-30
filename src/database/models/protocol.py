from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    DateTime,
    JSON
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.database.models import Base


class Protocol(Base):
    __tablename__ = "protocols"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[String] = mapped_column(String)
    doc_date: Mapped[DateTime] = mapped_column(DateTime)
    maintainer_id: Mapped[int] = mapped_column(Integer)
    vote_id: Mapped[int] = mapped_column(Integer)
    budget_amount: Mapped[Integer] = mapped_column(Integer)
    vote_json: Mapped[JSON] = mapped_column(JSON)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    changed_at: Mapped[DateTime] = mapped_column(DateTime)
