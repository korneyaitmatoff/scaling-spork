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
from src.models.student_model import OverviewStudent, StudentRequest, StudentBatch
from src.models.vote_model import Vote, VoteOverview, VoteRequest
from src.repository.sqlalchemy_repository import SqlAlchemyRepository
from src.routers import BaseRouter
from src.routers.employee_router import EmployeeRouter
from src.services import BaseService
from src.services.employee_service import EmployeeService

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

# Services
employee_service = EmployeeService(
    repository=type("EmployeeRepository", (SqlAlchemyRepository,), {})(
        engine=engine,
        entity=Employee
    )
)

# Routers

employee_router: BaseRouter = EmployeeRouter(
    service=employee_service,
    overview_model=OverviewEmployee,
    prefix="/employee",
    incoming_model=EmployeeRequest
)

# Routers
student_router: BaseRouter = type("StudentRouter", (BaseRouter,), {})(
    service=type("StudentService", (BaseService,), {})(
        repository=type("StudentRepository", (SqlAlchemyRepository,), {})(
        engine=engine,
        entity=Student
    )
    ),
    overview_model=OverviewStudent,
    prefix="/student",
    incoming_model=StudentBatch
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
protocol_router: BaseRouter = type("ProtocolRouter", (BaseRouter,), {})(
    service=type("ProtocolService", (BaseService,), {})(
        repository=SqlAlchemyRepository(
            engine=engine,
            entity=Protocol
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
            entity=IncomingRequest
        )
    ),
    overview_model=IncomingRequestOverview,
    prefix="/incoming_request",
    incoming_model=IncomingRequestRequest
)