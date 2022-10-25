from imdb import Cinemagoer
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response


from .. import schemas, models

def get_all_films(db: Session):
    "Returns all films from input db"
    films = db.query(models.Film).all()
    return films

def film_getter(id: int, db: Session):
    "Gets a specific film (selected by id) from input db"
    film = db.query(models.Film).filter(models.Film.id == id).first()
    if not film:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"film with id {id} not found in db")
    return film

def movie_extractor(movie_request):
    iterator = 0
    cine_obj = Cinemagoer()
    while iterator < 10:
        try:
            movie = list(cine_obj.search_movie(movie_request.name))[0]
            title = movie['title']
            year = movie['year']
            imdb_id = movie.getID()
            return {"name": title, "release_year": year, "imdb_id": imdb_id}
        except IndexError as e:
            iterator +=1 
            print(f"Error with cinemagoer extraction, retrying extraction: try no. {iterator}, error detail: {e}")

def movie_maker(db: Session, request = schemas.FilmRequest):
    retrieved_film = movie_extractor(request)
    new_movie = models.Film(name=retrieved_film["name"], release_year=retrieved_film["release_year"], imdb_id=retrieved_film["imdb_id"])
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return f"{retrieved_film['name']} (release year: {retrieved_film['release_year']}) has been added to the db" 

def film_deleter(id: int, db: Session):
    "Deletes a film from db, takes id as input"
    film = db.query(models.Film).filter(models.Film.id == id)
    if not film.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"film with id {id} not found") 
    film.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
