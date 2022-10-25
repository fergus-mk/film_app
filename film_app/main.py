from fastapi import FastAPI

from functionality import models
from functionality.database import engine
from functionality.routers import user, homepage, film


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(film.router)
app.include_router(homepage.router)
