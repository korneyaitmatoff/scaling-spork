from sqlalchemy import String, DateTime, Integer, Boolean, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from src.database.models import Base


class IncomingRequest(Base):
    __tablename__ = "incoming_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    student: Mapped[int] = mapped_column(ForeignKey(column="students.id"))
    reason: Mapped[String] = mapped_column(String)
    study_kind: Mapped[String] = mapped_column(String)
    name: Mapped[String] = mapped_column(String)
    is_commerce: Mapped[Boolean] = mapped_column(Boolean)
    faculty: Mapped[String] = mapped_column(String)
    course: Mapped[Integer] = mapped_column(Integer)
    group_code: Mapped[String] = mapped_column(String)
    contract: Mapped[String] = mapped_column(String)
    doc_date: Mapped[DateTime] = mapped_column(DateTime)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    changed_at: Mapped[DateTime] = mapped_column(DateTime)
