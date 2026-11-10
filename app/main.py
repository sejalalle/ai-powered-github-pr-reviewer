
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import Review

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Code Reviewer")


# Pydantic request model
class ReviewCreate(BaseModel):
    repository: str
    pr_number: int = Field(gt=0)
    title: str
    description: str


# Home endpoint
@app.get("/")
def home():
    return {"message": "AI Code Reviewer is running!"}


# CREATE - Add a review
@app.post("/reviews", status_code=201)
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):

    new_review = Review(
        repository=review.repository,
        pr_number=review.pr_number,
        title=review.title,
        description=review.description
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return {
        "message": "Review created successfully",
        "review": {
            "id": new_review.id,
            "repository": new_review.repository,
            "pr_number": new_review.pr_number,
            "title": new_review.title,
            "description": new_review.description
        }
    }


# READ - Get all reviews
@app.get("/reviews")
def get_reviews(db: Session = Depends(get_db)):

    reviews = db.query(Review).all()

    return reviews


# READ - Get one review by ID
@app.get("/reviews/{review_id}")
def get_review(
    review_id: int,
    db: Session = Depends(get_db)
):

    review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review


# UPDATE - Update a review
@app.put("/reviews/{review_id}")
def update_review(
    review_id: int,
    updated_review: ReviewCreate,
    db: Session = Depends(get_db)
):

    review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    review.repository = updated_review.repository
    review.pr_number = updated_review.pr_number
    review.title = updated_review.title
    review.description = updated_review.description

    db.commit()
    db.refresh(review)

    return {
        "message": "Review updated successfully",
        "review": review
    }


# DELETE - Delete a review
@app.delete("/reviews/{review_id}")
def delete_review(
    review_id: int,
    db: Session = Depends(get_db)
):

    review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    db.delete(review)
    db.commit()

    return {"message": "Review deleted successfully"}
