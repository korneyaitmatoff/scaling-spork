from sqlalchemy import create_engine

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
    IncomingRequest,
    Vote,
    VoteStudents,
    VoteEmployees,
    Protocol
)
from src.database.engine import DatabaseEngine
from src.repository.sqlalchemy_repository import SqlAlchemyRepository
from src.services import (
    BaseService,
    IncomingRequestService,
    VoteEmployeesService,
    VoteStudentsService,
    VoteService,
    ProtocolService
)

engine = create_engine(
    url=f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
)

sql_alchemy_repository = SqlAlchemyRepository(
    engine=engine,
    entity=Employee
)
db_engine = DatabaseEngine(
    postgres_user=POSTGRES_USER,
    postgres_password=POSTGRES_PASSWORD,
    postgres_db=POSTGRES_DB,
    db_host=DB_HOST,
    db_port=DB_PORT
)

# services don't realize hard logic
employee_service = type("EmployeeService", (BaseService,), {})(repository=sql_alchemy_repository, entity=Employee)
student_service = type("StudentService", (BaseService,), {})(repository=sql_alchemy_repository, entity=Student)

# services that include hard logic
vote_employees_service = VoteEmployeesService(repository=sql_alchemy_repository, entity=VoteEmployees)
vote_students_service = VoteStudentsService(repository=sql_alchemy_repository, entity=VoteStudents)
vote_service = VoteService(repository=sql_alchemy_repository, entity=Vote)
protocol_service = ProtocolService(repository=sql_alchemy_repository, entity=Protocol)
