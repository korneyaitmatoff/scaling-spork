from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.database.models import Base


class VoteStudents(Base):
    __tablename__ = "vote_students"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey(column="students.id"))
    vote_id: Mapped[int] = mapped_column(ForeignKey(column="votes.id"))
    protocol_id: Mapped[int] = mapped_column(ForeignKey(column="protocols.id"))
