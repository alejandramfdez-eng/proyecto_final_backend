from fastapi import FastAPI, HTTPException
from consultas import *
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import httpx
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

omdb_api_key = "ca48e3ef"

class Movie(BaseModel):
    id_movies: str
    title: str
    date: str
    gender: str

class Qualification(BaseModel):
    id_movies: str
    person: str
    qualification: int
    date: str

class Comment(BaseModel):
    id_movies: str
    person: str
    comment: str
    date: str

#historial de peliculas
@app.get("/movies", tags=["movies"])
def index():
    return select_all_history()

@app.post("/movies", tags=["movies"])
def insert_movie(body: Movie):
    try:
        insert_data((body.id_movies, body.title, body.date, body.gender))
        return {"message": "Movie inserted successfully"}
    except Exception as ex:
        print(ex)
        return {"error": 'Error inserting movie'}

@app.put("/movies/{id_movies}", tags=["movies"])
def update_movie(id_movies: str, body: Movie):
    try:
        update_data(id_movies, (body.id_movies, body.title, body.date, body.gender))
        return {"message": "Movie updated successfully"}
    except Exception as ex:
        print(ex)
        return {"error": 'Error updating movie'}
    
@app.delete("/movies/{id}", tags=["movies"])
def delete_movie(id_movies: str):
    try:
        delete_data(id_movies)
        return {"message": "Movie deleted successfully"}
    except Exception as ex:
        print(ex)
        return {"error": 'Error deleting movie'}

#conexion con la api de omdb
@app.get("/movies/search", tags=["OMDB API"])
async def search_movies(title: str, year: str = ""):
    url = f"http://www.omdbapi.com/?s={title}&apikey={omdb_api_key}"
    if year:
        url += f"&y={year}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return data

@app.get("/movies/{id_movies}/details", tags=["OMDB API"])
async def get_movie_details(id_movies: str):
    url = f"http://www.omdbapi.com/?i={id_movies}&apikey={omdb_api_key}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return data

#calificaciones de las peliculas
@app.get("/movies/{id_movies}/qualifications", tags=["qualifications"])
def get_qualifications(id_movies: str):
    return select_qualifications(id_movies)

@app.post("/movies/{id_movies}/qualifications", tags=["qualifications"])
def add_qualification(id_movies: str, body: Qualification):
    try:
        insert_qualifications((id_movies, body.person, body.qualification, body.date))
        return {"message": "Qualification inserted successfully"}
    except Exception as ex:
        print(ex)
        return {"error": 'Error inserting qualification'}

#comentarios de las peliculas
@app.get("/movies/{id_movies}/comments", tags=["comments"])
def get_comments(id_movies: str):
    return select_comments(id_movies)

@app.post("/movies/{id_movies}/comments", tags=["comments"])
def add_comment(id_movies: str, body: Comment):
    try:
        insert_comment((id_movies, body.person, body.comment, body.date))
        return {"message": "Comment inserted successfully"}
    except Exception as ex:
        print(ex)
        return {"error": 'Error inserting comment'}