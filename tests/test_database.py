from src.database.database import get_connection, initialize_database


def test_database_initialization():
    initialize_database()

    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            AND name = 'tickets'
            """
        )

        table = cursor.fetchone()

        assert table is not None
        assert table["name"] == "tickets"

    finally:
        connection.close()