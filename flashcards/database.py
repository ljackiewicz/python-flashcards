import os
from sqlite3 import dbapi2 as sqlite
from sqlite3 import Cursor
from typing import Any

DATABASE = 'data/example.db'


class Database(object):
    DB_FILE = "data/example.db"
    DB_SCHEMA_FILE = "data/schema.sql"

    def __init__(self) -> None:
        schema = None

        if not os.path.exists(Database.DB_FILE):
            with open(Database.DB_SCHEMA_FILE, "r") as file:
                schema = file.read()

        self.conn = sqlite.connect(Database.DB_FILE)
        self.conn.row_factory = sqlite.Row
        self.cur = self.conn.cursor()

        if schema:
            self.conn.executescript(schema)
            self.conn.commit()

    def execute(self, sql: str, *args: Any) -> Cursor:
        cur = self.conn.execute(sql, args)
        return cur

    def commit(self) -> None:
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "Database":
        return self

    def __exit__(self, *args: Any) -> None:
        self.conn.close()
