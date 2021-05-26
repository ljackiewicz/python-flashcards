import os
import sqlite3

DATABASE = 'data/example.db'


def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if not os.path.exists(DATABASE):
        conn = connect_db()
        with open("data/schema.sql", "r") as file:
            with conn:
                conn.executescript(file.read())


def query_db(query: str, args=()):
    conn = connect_db()
    with conn:
        return conn.execute(query, args).fetchall()
