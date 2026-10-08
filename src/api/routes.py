from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from src.backend.services import create_ticket, get_ticket


router = APIRouter()


class TicketCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    message: str


class TicketResponse(BaseModel):
    ticket_id: int
    category: str
    priority: str
    status: str


@router.post("/tickets", response_model=TicketResponse)
def create_support_ticket(ticket: TicketCreate):
    """
    Create and classify a support ticket.
    """

    ticket_id = create_ticket(
        customer_name=ticket.customer_name,
        customer_email=ticket.customer_email,
        message=ticket.message,
    )

    created_ticket = get_ticket(ticket_id)

    return TicketResponse(
        ticket_id=created_ticket["id"],
        category=created_ticket["category"],
        priority=created_ticket["priority"],
        status=created_ticket["status"],
    )