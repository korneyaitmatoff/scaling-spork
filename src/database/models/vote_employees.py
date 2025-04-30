from sqlalchemy import (
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.database.models import Base


class VoteEmployees(Base):
    __tablename__ = "vote_employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    vote_id: Mapped[int] = mapped_column(ForeignKey(column="votes.id"))
    protocol_id: Mapped[int] = mapped_column(ForeignKey(column="protocols.id"))
    employee_id: Mapped[int] = mapped_column(ForeignKey(column="employees.id"))
