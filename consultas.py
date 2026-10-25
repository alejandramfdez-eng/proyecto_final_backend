from conexion import Conexion
import sqlite3

def formato (respuesta):
    lista_final = []
    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))
    return lista_final

#consultas calificaciones
def select_qualifications(id_movies: str):
    conexionSelect = Conexion("SELECT id, name, qualification, date FROM qualifications WHERE id_movies = ? ORDER BY id DESC", [id_movies])
    try:
        return formato(conexionSelect.res)
    finally:
        conexionSelect.con.close()
    

def insert_qualifications(data):
    conexionInsert = Conexion("INSERT INTO qualifications (id_movies, name, qualification, date) VALUES (?, ?, ?, ?)", data)
    try:
        conexionInsert.con.commit()
    finally:
        conexionInsert.con.close()


def update_qualification(id_movies: str, qualification_id: int, data):
    conexionUpdate = Conexion(
        "UPDATE qualifications SET name = ?, qualification = ?, date = ? WHERE id = ? AND id_movies = ?",
        [*data, qualification_id, id_movies],
    )
    try:
        conexionUpdate.con.commit()
        return conexionUpdate.cursor.rowcount > 0
    finally:
        conexionUpdate.con.close()


def delete_qualification(id_movies: str, qualification_id: int):
    conexionDelete = Conexion(
        "DELETE FROM qualifications WHERE id = ? AND id_movies = ?",
        [qualification_id, id_movies],
    )
    try:
        conexionDelete.con.commit()
        return conexionDelete.cursor.rowcount > 0
    finally:
        conexionDelete.con.close()

#consultas comentarios
def select_comments(id_movies: str):
    conexionSelect = Conexion("SELECT id, name, comment, date FROM comments WHERE id_movies = ? ORDER BY id DESC", [id_movies])
    try:
        return formato(conexionSelect.res)
    finally:
        conexionSelect.con.close()

def insert_comment(data):
    conexionInsert = Conexion("INSERT INTO comments (id_movies, name, comment, date) VALUES (?, ?, ?, ?)", data)
    try:
        conexionInsert.con.commit()
    finally:
        conexionInsert.con.close()


def update_comment(id_movies: str, comment_id: int, data):
    conexionUpdate = Conexion(
        "UPDATE comments SET name = ?, comment = ?, date = ? WHERE id = ? AND id_movies = ?",
        [*data, comment_id, id_movies],
    )
    try:
        conexionUpdate.con.commit()
        return conexionUpdate.cursor.rowcount > 0
    finally:
        conexionUpdate.con.close()


def delete_comment(id_movies: str, comment_id: int):
    conexionDelete = Conexion(
        "DELETE FROM comments WHERE id = ? AND id_movies = ?",
        [comment_id, id_movies],
    )
    try:
        conexionDelete.con.commit()
        return conexionDelete.cursor.rowcount > 0
    finally:
        conexionDelete.con.close()

  