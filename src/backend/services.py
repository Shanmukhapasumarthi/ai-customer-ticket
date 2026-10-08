from __future__ import annotations

from src.ai.classifier import classify_ticket
from src.database.database import get_connection


def create_ticket(
    customer_name: str,
    customer_email: str,
    message: str,
) -> int:
    """
    Create a support ticket, classify it,
    and save the classification.
    """

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO tickets (
                customer_name,
                customer_email,
                message
            )
            VALUES (?, ?, ?)
            """,
            (
                customer_name,
                customer_email,
                message,
            ),
        )

        ticket_id = cursor.lastrowid

        classification = classify_ticket(message)

        connection.execute(
            """
            UPDATE tickets
            SET category = ?,
                priority = ?
            WHERE id = ?
            """,
            (
                classification.category,
                classification.priority,
                ticket_id,
            ),
        )

        connection.commit()

        return ticket_id

    finally:
        connection.close()


def get_ticket(ticket_id: int):
    """
    Retrieve a ticket by its ID.
    """

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT
                id,
                category,
                priority,
                status
            FROM tickets
            WHERE id = ?
            """,
            (ticket_id,),
        )

        return cursor.fetchone()

    finally:
        connection.close()