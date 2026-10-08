from src.backend.services import create_ticket
from src.database.database import get_connection, initialize_database


def test_create_ticket():
    initialize_database()

    ticket_id = create_ticket(
        customer_name="Test User",
        customer_email="test@example.com",
        message="I was charged twice for my subscription.",
    )

    assert ticket_id is not None
    assert ticket_id > 0

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT *
            FROM tickets
            WHERE id = ?
            """,
            (ticket_id,),
        )

        ticket = cursor.fetchone()

        assert ticket is not None
        assert ticket["customer_name"] == "Test User"
        assert ticket["customer_email"] == "test@example.com"
        assert ticket["message"] == "I was charged twice for my subscription."
        assert ticket["category"] == "billing"
        assert ticket["priority"] == "high"
        assert ticket["status"] == "open"

    finally:
        connection.close()