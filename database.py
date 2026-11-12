import sqlite3
from datetime import datetime

DB_FILE = "tickets.db"


def get_connection():
    return sqlite3.connect(DB_FILE)


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT,
                ticket_text TEXT,
                category TEXT,
                priority TEXT,
                summary TEXT,
                reply TEXT
            )
            """
        )


def save_ticket(ticket_text, result):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO tickets (created_at, ticket_text, category, priority, summary, reply) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                ticket_text,
                result["category"],
                result["priority"],
                result["summary"],
                result["reply"],
            ),
        )


def get_all_tickets():
    with get_connection() as conn:
        return conn.execute(
            "SELECT created_at, category, priority, summary FROM tickets ORDER BY id DESC"
        ).fetchall()