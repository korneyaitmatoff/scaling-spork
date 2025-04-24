from typing import Any

from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from src.config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    DB_HOST,
    DB_PORT
)

class DatabaseEngine:
    def __init__(self):

        self.connection = connect(
            dsn=f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def execute_and_commit(self, statement: str):
        self.cursor.execute(query=statement)
        self.connection.commit()

    def execute(self, statement: str) -> list[dict[str, Any]]:
        self.cursor.execute(query=statement)

        return self.cursor.fetchall()
