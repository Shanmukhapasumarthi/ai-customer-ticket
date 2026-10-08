from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_create_ticket_api():
    response = client.post(
        "/tickets",
        json={
            "customer_name": "Test User",
            "customer_email": "test@example.com",
            "message": "I was charged twice for my subscription.",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["ticket_id"] > 0
    assert data["category"] == "billing"
    assert data["priority"] == "high"
    assert data["status"] == "open"