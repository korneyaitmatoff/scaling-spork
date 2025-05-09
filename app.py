from fastapi import FastAPI

from src.dependencies import (
    employee_router,
    student_router,
    incoming_request_router
)

app = FastAPI()

app.include_router(router=employee_router.router)
app.include_router(router=student_router.router)
app.include_router(router=incoming_request_router.router)
