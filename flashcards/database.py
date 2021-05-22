import os
import sqlite3

DATABASE = 'example.db'


def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = connect_db()
    with conn:
        conn.execute("CREATE TABLE cards (front text, back text)")


def query_db(query: str, args=()):
    conn = connect_db()
    with conn:
        return conn.execute(query, args).fetchall()


def main():
    # initialize database
    if not os.path.exists(DATABASE):
        init_db()

    cards = query_db("SELECT rowid, front, back FROM cards")

    for card in cards:
        print(card["rowid"], card["front"], card["back"])


if __name__ == "__main__":
    main()
