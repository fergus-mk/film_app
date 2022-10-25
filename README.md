# film_app

Film app is a project to showcase building an app with the FastAPI framework. It is designed to simulate a film ownership service, where users own films. The app is designed for staff to be able to access and API where they can add both users and films and depict which user owns which film. Information about films is extracted from the IMDB database using the Cinemagoer API. All data is stored in a SQLite database.


## Use
---


### Users 
(I.e., owners of films) can be created, accessed and deleted using HTTP request methods:

- GET - The user id is given and an individual users details are returned
- GET - All users can be extracted
- POST - It is possible to create a new user. Pydantic is used to enforce correct types of inputs
- DELETE - The user id is given and the user is deleted


### Films
(I.e., films owned) can be created, accessed and deleted using HTTP request methods:

- GET - The film id is given and an individual films details are returned. Note the films owner is shown
- GET - All films can be extracted. Note for each film the owners are shown
- POST - It is possible to create a new film. Pydantic is used to enforce correct types of inputs. When a new film is created the user_id is also given. This means as films are created they should be assigned owners
- DELETE - The user id is given and the user is deleted


### Hosting
The API is hosted using [Deta Cloud](https://www.deta.sh/) at: #####


### Note
This project was inspired by: [Bitfumes FastAPI Full Course](https://www.youtube.com/watch?v=7t2alSnE2-I&t=11405s)
