from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: bool


class FilmRequest(BaseModel):
    name: str
    user_id: int


class Film(BaseModel):
    name: str
    release_year: int
    imdb_id: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class ShowFilm(BaseModel):
    name: str
    release_year: int
    owner: ShowUser

    class Config:
        orm_mode = True
