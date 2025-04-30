from typing import Any

from psycopg2 import connect
from psycopg2.extras import RealDictCursor


class DatabaseEngine:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseEngine, cls).__new__(cls)

        return cls._instance

    def __init__(self, postgres_user, postgres_password, db_host, db_port, postgres_db):
        self.connection = connect(
            dsn=f"postgres://{postgres_user}:{postgres_password}@{db_host}:{db_port}/{postgres_db}"
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def execute_and_commit(self, statement: str):
        self.cursor.execute(query=statement)
        self.connection.commit()

    def execute(self, statement: str) -> list[dict[str, Any]]:
        self.cursor.execute(query=statement)

        return self.cursor.fetchall()
