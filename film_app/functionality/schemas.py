from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: bool

class ShowUser(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config():
        orm_mode=True

class FilmRequest(BaseModel):
    name: str

class Film(BaseModel):
    name: str
    release_year: int
    imbd_id: str

class ShowFilm(BaseModel):
    name: str
    release_year: int

    class Config():
        orm_mode=True
