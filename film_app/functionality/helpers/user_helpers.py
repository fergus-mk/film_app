from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models, hashing


def get_all_users(db: Session):
    "Returns all users from input db"
    users = db.query(models.User).all()
    return users


def user_getter(id: int, db: Session):
    "Gets a specific user (selected by id) from input db"
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} not found in db",
        )
    return user


def user_creator(request: schemas.User, db: Session):
    "Creates a new user, input is in format of User object"
    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=hashing.Hash.encrypt(request.password),
        is_active=request.is_active,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request


def user_deleter(id: int, db: Session):
    "Deletes a user from db, takes id as input"
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found"
        )
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
