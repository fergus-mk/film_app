from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    films = relationship(
        "Film", back_populates="owner"
    )


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    imdb_id = Column(String)
    name = Column(String)
    release_year = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))


    owner = relationship(
        "User", back_populates="films"
    )



# user_film_table = Table( # If I want to add many to many relationship later 
#     "user_film_table",
#     Base.metadata,
#     Column("user_id", ForeignKey("users.id")),
#     Column("film_id", ForeignKey("films.id")),
# )