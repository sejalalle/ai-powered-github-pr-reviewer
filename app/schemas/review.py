
from pydantic import BaseModel, Field, ConfigDict


# Schema for creating a review
class ReviewCreate(BaseModel):

    repository: str = Field(min_length=1, max_length=255)

    pr_number: int = Field(gt=0)

    title: str = Field(min_length=1, max_length=255)

    description: str = Field(min_length=1)


# Schema for updating a review
class ReviewUpdate(BaseModel):

    repository: str = Field(min_length=1, max_length=255)

    pr_number: int = Field(gt=0)

    title: str = Field(min_length=1, max_length=255)

    description: str = Field(min_length=1)


# Schema for returning a review
class ReviewResponse(BaseModel):

    id: int

    repository: str

    pr_number: int

    title: str

    description: str

    model_config = ConfigDict(from_attributes=True)
