from sqlalchemy import String, DateTime, Boolean, JSON
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.database.models import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column(String)
    group_code: Mapped[String] = mapped_column(String)
    inn: Mapped[String] = mapped_column(String)
    is_resident: Mapped[Boolean] = mapped_column(Boolean)
    passport_data: Mapped[JSON] = mapped_column(JSON)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    changed_at: Mapped[DateTime] = mapped_column(DateTime)
