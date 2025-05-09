from cProfile import label

from sqlalchemy import create_engine, Engine

from src.config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    DB_HOST,
    DB_PORT
)
from src.database.models import (
    Employee,
    Student,
    VoteEmployees, Protocol,
)
from src.database.engine import DatabaseEngine
from src.models import (
    OverviewEmployee
)
from src.models.employee_model import EmployeeRequest
from src.models.incoming_request_model import IncomingRequestRequest, IncomingRequestOverview, IncomingRequest
from src.models.protocol_model import ProtocolOverview, ProtocolRequest
from src.models.student_model import OverviewStudent, StudentRequest
from src.models.vote_model import Vote, VoteOverview, VoteRequest
from src.repository.sqlalchemy_repository import SqlAlchemyRepository
from src.routers import BaseRouter
from src.routers.employee_router import EmployeeRouter
from src.routers.students_router import StudentsRouter
from src.services import BaseService
from src.services.employee_service import EmployeeService
from src.services.students_service import StudentsService

engine: Engine = create_engine(
    url=f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
)

db_engine: DatabaseEngine = DatabaseEngine(
    postgres_user=POSTGRES_USER,
    postgres_password=POSTGRES_PASSWORD,
    postgres_db=POSTGRES_DB,
    db_host=DB_HOST,
    db_port=DB_PORT
)

student_repository = SqlAlchemyRepository(engine=engine, entity=Student)

# Services
employee_service = EmployeeService(
    repository=type("EmployeeRepository", (SqlAlchemyRepository,), {})(
        engine=engine,
        entity=Employee
    )
)
student_service = StudentsService(
    repository=student_repository
)

# Routers

employee_router: BaseRouter = EmployeeRouter(
    service=employee_service,
    overview_model=OverviewEmployee,
    prefix="/employee",
    incoming_model=EmployeeRequest
)
student_router: BaseRouter = StudentsRouter(
    service=student_service,
    overview_model=OverviewStudent,
    prefix="/student",
    incoming_model=StudentRequest
)
