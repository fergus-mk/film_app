from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database
from ..helpers import user_helpers


router = APIRouter(prefix = "/user", tags=["user"])


@router.get("/{id}", response_model=schemas.ShowUser)
async def get_user(id: int, db: Session = Depends(database.get_db)):
    "Gets a user from the db, selection uses user id"
    return user_helpers.user_getter(id, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all_users(db: Session = Depends(database.get_db)):
    "Returns all users in the db"
    return user_helpers.get_all_users(db)


@router.post("/", response_model=schemas.ShowUser)
async def add_user(request: schemas.User, db: Session = Depends(database.get_db)):
    "Adds a user to the db"
    return user_helpers.user_creator(request, db)


@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db)):
    "Deletes user from the db, selection uses user id"
    return user_helpers.user_deleter(id, db)