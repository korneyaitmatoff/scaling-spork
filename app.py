from fastapi import FastAPI

from src.dependencies import (
    employee_router,
    student_router,
    vote_router,
    vote_employee_router,
    vote_students_router,
    protocol_router,
    incoming_request_router,
)

app = FastAPI()

app.include_router(router=employee_router.router)
app.include_router(router=student_router.router)
app.include_router(router=vote_router.router)
app.include_router(router=vote_employee_router.router)
app.include_router(router=vote_students_router.router)
app.include_router(router=incoming_request_router.router)
app.include_router(router=protocol_router.router)
