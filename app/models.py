
from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Review(Base):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    repository = Column(String(255), nullable=False)

    pr_number = Column(Integer, nullable=False)

    title = Column(String(255), nullable=False)

    description = Column(Text, nullable=False)
