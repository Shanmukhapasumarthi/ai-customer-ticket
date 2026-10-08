from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ClassificationResult:
    category: str
    priority: str


def classify_ticket(message: str) -> ClassificationResult:
    """
    Classify a support ticket into a category and priority.

    This is the V1 baseline classifier.
    """

    text = message.lower()

    if any(
        keyword in text
        for keyword in ["charged twice", "double charged", "refund", "payment"]
    ):
        return ClassificationResult(
            category="billing",
            priority="high",
        )

    if any(
        keyword in text
        for keyword in ["password", "login", "log in", "cannot access"]
    ):
        return ClassificationResult(
            category="account",
            priority="high",
        )

    if any(
        keyword in text
        for keyword in ["slow", "not working", "error", "bug"]
    ):
        return ClassificationResult(
            category="technical",
            priority="medium",
        )

    return ClassificationResult(
        category="general",
        priority="low",
    )