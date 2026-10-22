from conexion import Conexion
import sqlite3

def formato (respuesta):
    lista_final = []
    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))
    return lista_final

#consultas calificaciones
def select_qualifications(id_movies: str):
    conexionSelect = Conexion("SELECT person, qualification, date FROM qualifications WHERE id_movies = ? ORDER BY id DESC", [id_movies])
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.close()
    return resp

def insert_qualifications(data):
    try:
        conexionInsert = Conexion("INSERT INTO qualifications (id_movies, person, qualification, date) VALUES (?, ?, ?, ?)", data)
        conexionInsert.close()
    except sqlite3.Error as error:
        print("Error:", error)

#consultas comentarios
def select_comments(id_movies: str):
    conexionSelect = Conexion("SELECT person, comment, date FROM comments WHERE id_movies = ? ORDER BY id DESC", [id_movies])
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.close()
    return resp

def insert_comment(data):
    try:
        conexionInsert = Conexion("INSERT INTO comments (id_movies, person, comment, date) VALUES (?, ?, ?, ?)", data)
        conexionInsert.close()
    except sqlite3.Error as error:
        print("Error:", error)

  