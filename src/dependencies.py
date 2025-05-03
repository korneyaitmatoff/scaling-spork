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
    VoteEmployees,
)
from src.database.engine import DatabaseEngine
from src.models import (
    OverviewEmployee
)
from src.models.employee_model import EmployeeRequest
from src.models.incoming_request_model import IncomingRequestRequest, IncomingRequestOverview
from src.models.protocol_model import ProtocolOverview, ProtocolRequest
from src.models.student_model import OverviewStudent, StudentRequest
from src.models.vote_employees_model import VoteEmployeesRequest, VoteEmployeesOverview
from src.models.vote_model import Vote, VoteOverview, VoteRequest
from src.models.vote_students_model import VoteStudentsRequest, VoteStudentsOverview
from src.repository.sqlalchemy_repository import SqlAlchemyRepository
from src.routers import BaseRouter
from src.services import BaseService

engine: Engine = create_engine(
    url=f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
)

sql_alchemy_repository: SqlAlchemyRepository = SqlAlchemyRepository(
    engine=engine,
    entity=Employee
)
db_engine: DatabaseEngine = DatabaseEngine(
    postgres_user=POSTGRES_USER,
    postgres_password=POSTGRES_PASSWORD,
    postgres_db=POSTGRES_DB,
    db_host=DB_HOST,
    db_port=DB_PORT
)

# Routers
employee_router: BaseRouter = type("EmployeeRouter", (BaseRouter,), {})(
    service=type("EmployeeService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=Employee
        )
    ),
    overview_model=OverviewEmployee,
    prefix="/employee",
    incoming_model=EmployeeRequest
)
student_router: BaseRouter = type("StudentRouter", (BaseRouter,), {})(
    service=type("StudentService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=Student
        )
    ),
    overview_model=OverviewStudent,
    prefix="/student",
    incoming_model=StudentRequest
)
vote_router: BaseRouter = type("VoteRouter", (BaseRouter,), {})(
    service=type("VoteService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=Vote
        )
    ),
    overview_model=VoteOverview,
    prefix="/vote",
    incoming_model=VoteRequest
)
vote_employee_router: BaseRouter = type("VoteEmployeeRouter", (BaseRouter,), {})(
    service=type("VoteEmployeeService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=VoteEmployees
        )
    ),
    overview_model=VoteEmployeesOverview,
    prefix="/vote_employee",
    incoming_model=VoteEmployeesRequest
)
vote_students_router: BaseRouter = type("VoteStudentsRouter", (BaseRouter,), {})(
    service=type("VoteStudentsService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=VoteEmployees
        )
    ),
    overview_model=VoteStudentsOverview,
    prefix="/vote_students",
    incoming_model=VoteStudentsRequest
)
protocol_router: BaseRouter = type("ProtocolRouter", (BaseRouter,), {})(
    service=type("ProtocolService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=VoteEmployees
        )
    ),
    overview_model=ProtocolOverview,
    prefix="/protocol",
    incoming_model=ProtocolRequest
)
incoming_request_router: BaseRouter = type("IncomingRequestRouter", (BaseRouter,), {})(
    service=type("IncomingRequestService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=VoteEmployees
        )
    ),
    overview_model=IncomingRequestOverview,
    prefix="/incoming_request",
    incoming_model=IncomingRequestRequest
)
