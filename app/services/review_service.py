
from sqlalchemy.orm import Session

from app.models import Review
from app.schemas.review import ReviewCreate, ReviewUpdate


# CREATE
def create_review(db: Session, review_data: ReviewCreate):

    try:

        new_review = Review(
            repository=review_data.repository,
            pr_number=review_data.pr_number,
            title=review_data.title,
            description=review_data.description
        )

        db.add(new_review)

        db.commit()

        db.refresh(new_review)

        return new_review

    except Exception:

        db.rollback()

        raise


# READ ALL
def get_all_reviews(db: Session):

    return db.query(Review).all()


# READ ONE
def get_review_by_id(db: Session, review_id: int):

    return db.query(Review).filter(
        Review.id == review_id
    ).first()


# UPDATE
def update_review(
    db: Session,
    review: Review,
    updated_data: ReviewUpdate
):

    try:

        review.repository = updated_data.repository

        review.pr_number = updated_data.pr_number

        review.title = updated_data.title

        review.description = updated_data.description

        db.commit()

        db.refresh(review)

        return review

    except Exception:

        db.rollback()

        raise


# DELETE
def delete_review(db: Session, review: Review):

    try:

        db.delete(review)

        db.commit()

    except Exception:

        db.rollback()

        raise
