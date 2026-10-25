from fastapi import FastAPI, HTTPException
from consultas import *
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import httpx
import sqlite3
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

omdb_api_key = "ca48e3ef"

class Qualification(BaseModel):
    id_movies: str
    name: str
    qualification: int = Field(ge=1, le=5)
    date: str

class Comment(BaseModel):
    id_movies: str
    name: str
    comment: str
    date: str

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
    try:        
        return select_qualifications(id_movies)
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudieron cargar las calificaciones") from error
   

@app.post("/movies/{id_movies}/qualifications", tags=["qualifications"])
def add_qualification(id_movies: str, body: Qualification):
    try:
        insert_qualifications([id_movies, body.name, body.qualification, body.date])
        return {"message": "Qualification inserted successfully"}
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudo guardar la calificación") from error


@app.put("/movies/{id_movies}/qualifications/{qualification_id}", tags=["qualifications"])
def edit_qualification(id_movies: str, qualification_id: int, body: Qualification):
    if body.id_movies != id_movies:
        raise HTTPException(status_code=400, detail="La película del cuerpo no coincide con la ruta")
    try:
        updated = update_qualification(
            id_movies,
            qualification_id,
            [body.name, body.qualification, body.date],
        )
        if not updated:
            raise HTTPException(status_code=404, detail="Calificación no encontrada")
        return {"message": "Qualification updated successfully"}
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudo actualizar la calificación") from error


@app.delete("/movies/{id_movies}/qualifications/{qualification_id}", tags=["qualifications"])
def remove_qualification(id_movies: str, qualification_id: int):
    try:
        deleted = delete_qualification(id_movies, qualification_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Calificación no encontrada")
        return {"message": "Qualification deleted successfully"}
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudo eliminar la calificación") from error

#comentarios de las peliculas
@app.get("/movies/{id_movies}/comments", tags=["comments"])
def get_comments(id_movies: str):
    try:
        return select_comments(id_movies)
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudieron cargar los comentarios") from error
       

@app.post("/movies/{id_movies}/comments", tags=["comments"])
def add_comment(id_movies: str, body: Comment):
    try:
        insert_comment([id_movies, body.name, body.comment, body.date])
        return {"message": "Comment inserted successfully"}
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudo guardar el comentario") from error


@app.put("/movies/{id_movies}/comments/{comment_id}", tags=["comments"])
def edit_comment(id_movies: str, comment_id: int, body: Comment):
    if body.id_movies != id_movies:
        raise HTTPException(status_code=400, detail="La película del cuerpo no coincide con la ruta")
    try:
        updated = update_comment(
            id_movies,
            comment_id,
            [body.name, body.comment, body.date],
        )
        if not updated:
            raise HTTPException(status_code=404, detail="Comentario no encontrado")
        return {"message": "Comment updated successfully"}
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudo actualizar el comentario") from error


@app.delete("/movies/{id_movies}/comments/{comment_id}", tags=["comments"])
def remove_comment(id_movies: str, comment_id: int):
    try:
        deleted = delete_comment(id_movies, comment_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Comentario no encontrado")
        return {"message": "Comment deleted successfully"}
    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail="No se pudo eliminar el comentario") from error