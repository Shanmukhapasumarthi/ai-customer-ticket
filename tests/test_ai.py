from src.ai.classifier import classify_ticket


def test_billing_ticket():
    result = classify_ticket(
        "I was charged twice for my subscription."
    )

    assert result.category == "billing"
    assert result.priority == "high"


def test_account_ticket():
    result = classify_ticket(
        "I cannot login to my account."
    )

    assert result.category == "account"
    assert result.priority == "high"


def test_technical_ticket():
    result = classify_ticket(
        "The application is showing an error."
    )

    assert result.category == "technical"
    assert result.priority == "medium"


def test_general_ticket():
    result = classify_ticket(
        "I have a question about your service."
    )

    assert result.category == "general"
    assert result.priority == "low"