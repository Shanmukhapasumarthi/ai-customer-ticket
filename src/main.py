from fastapi import FastAPI

from src.api.routes import router
from src.database.database import initialize_database


initialize_database()


app = FastAPI(
    title="AI Support Ticket System",
    version="1.0.0",
)


app.include_router(router)