from sqlalchemy import String, DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from src.database.models import Base

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    login: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    changed_at: Mapped[DateTime] = mapped_column(DateTime)
