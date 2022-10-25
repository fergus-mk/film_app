from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from imdb import Cinemagoer
from sqlalchemy.orm import Session

from .. import schemas, database
from ..helpers import film_helpers


router = APIRouter(prefix = "/film", tags=["film"])


@router.get("/{id}", response_model=schemas.ShowFilm)
async def get_film(id: int, db: Session = Depends(database.get_db)):
    "Gets a user from the db, selection uses user id"
    return film_helpers.film_getter(id, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowFilm])
def all_films(db: Session = Depends(database.get_db)):
    "Returns all films in the db"
    return film_helpers.get_all_films(db)


@router.post("/")
async def add_film(request: schemas.FilmRequest, db: Session = Depends(database.get_db)):
    "Adds a film to the db"
    return film_helpers.movie_maker(db, request)


@router.delete("/{id}")
def delete_film(id: int, db: Session = Depends(database.get_db)):
    "Deletes film from the db, selection uses film id"
    return film_helpers.film_deleter(id, db)