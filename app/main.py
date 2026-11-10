
from fastapi import FastAPI

from app.database import engine, Base
from app import models

from app.routers import reviews


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="AI Code Reviewer",
    description="AI-powered GitHub Pull Request Reviewer",
    version="1.0.0"
)


# Register routers
app.include_router(reviews.router)


# Home endpoint
@app.get("/")
def home():

    return {
        "message": "AI Code Reviewer is running!"
    }
