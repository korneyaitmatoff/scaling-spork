from pydantic import BaseModel


class VoteEmployees(BaseModel):
    id: int
    vote_id: int
    protocol_id: int
    employee_id: int
