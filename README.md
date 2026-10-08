# AI Support Ticket System

A production-style V1 support ticket system built to learn and practically implement the Software Development Life Cycle (SDLC), backend development, testing, Docker, and basic CI/CD.

The system allows a customer to submit a support ticket through a Streamlit frontend. The FastAPI backend stores the ticket, classifies the issue, assigns a priority, and returns the result.

---

## Features

- Submit support tickets through a Streamlit UI
- REST API using FastAPI
- Rule-based ticket classification
- Automatic priority assignment
- SQLite database for ticket storage
- Service layer for business logic
- API validation using Pydantic
- Automated testing using Pytest
- Dockerized backend
- Dockerized frontend
- Docker Compose for multi-container setup
- End-to-end frontend-to-backend communication

---

## Architecture

```text
                    Customer
                       |
                       v
              Streamlit Frontend
                  Port 8501
                       |
                       | HTTP
                       v
              FastAPI Backend
                  Port 8000
                       |
                       v
                services.py
                 /        \
                /          \
               v            v
       classifier.py    database.py
          (AI Logic)       |
                            v
                         SQLite