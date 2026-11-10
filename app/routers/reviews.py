
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.review import (
    ReviewCreate,
    ReviewUpdate,
    ReviewResponse
)

from app.services import review_service


router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


# CREATE
@router.post(
    "/",
    response_model=ReviewResponse,
    status_code=201
)
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):

    return review_service.create_review(db, review)


# READ ALL
@router.get(
    "/",
    response_model=list[ReviewResponse]
)
def get_reviews(db: Session = Depends(get_db)):

    return review_service.get_all_reviews(db)


# READ ONE
@router.get(
    "/{review_id}",
    response_model=ReviewResponse
)
def get_review(
    review_id: int,
    db: Session = Depends(get_db)
):

    review = review_service.get_review_by_id(db, review_id)

    if review is None:

        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review


# UPDATE
@router.put(
    "/{review_id}",
    response_model=ReviewResponse
)
def update_review(
    review_id: int,
    updated_review: ReviewUpdate,
    db: Session = Depends(get_db)
):

    review = review_service.get_review_by_id(db, review_id)

    if review is None:

        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review_service.update_review(
        db,
        review,
        updated_review
    )


# DELETE
@router.delete("/{review_id}")
def delete_review(
    review_id: int,
    db: Session = Depends(get_db)
):

    review = review_service.get_review_by_id(db, review_id)

    if review is None:

        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    review_service.delete_review(db, review)

    return {
        "message": "Review deleted successfully"
    }
