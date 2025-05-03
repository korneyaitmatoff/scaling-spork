from pydantic import BaseModel


class VoteStudents(BaseModel):
    id: int
    student_id: int
    vote_id: int
    protocol_id: int

class VoteStudentsOverview(VoteStudents):
    pass

class VoteStudentsRequest(BaseModel):
    student_id: int
    vote_id: int
    protocol_id: int