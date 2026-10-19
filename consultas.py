from conexion import Conexion
import sqlite3

def formato (respuesta):
    lista_final = []
    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))
    return lista_final

#consultas historial
def select_all_history():
    conexionSelect = Conexion("SELECT * FROM record ORDER BY id DESC")
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.con.close()
    return resp

def select_id(id: int):
    conexionSelectid = Conexion("SELECT * FROM record WHERE id = ?", [id])
    respuesta = conexionSelectid.res
    resp = formato(respuesta)
    conexionSelectid.con.close()
    return resp

def insert_data(data):
    try:
        conexionInsert = Conexion("INSERT INTO record (id_movies, title, year, gender) VALUES (?, ?, ?, ?)", data)
        conexionInsert.res
        conexionInsert.con.commit()
    except sqlite3.Error as error:
        print("Error:", error)

    conexionInsert.con.close()

def update_data(id, data):
    try:
        conexionUpdate = Conexion("UPDATE record SET id_movies = ?, title = ?, year = ?, gender = ? WHERE id = ?", data + [id])
        conexionUpdate.res
        conexionUpdate.con.commit()
    except sqlite3.Error as error:
        print("Error:", error)

    conexionUpdate.con.close()

def delete_data(id:int):
    try:
        conexionDelete = Conexion("DELETE FROM record WHERE id = ?", [id])
        conexionDelete.res
        conexionDelete.con.commit()
    except sqlite3.Error as error:
        print("Error:", error)

    conexionDelete.con.close()

#consultas calificaciones
def select_qualifications(id_movies: str):
    conexionSelect = Conexion("SELECT person, qualification, date FROM qualification WHERE id_movies = ? ORDER BY id DESC", [id_movies])
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.con.close()
    return resp

def insert_qualifications(data):
    try:
        conexionInsert = Conexion("INSERT INTO qualification (id_movies, person, qualification, date) VALUES (?, ?, ?, ?)", data)
        conexionInsert.res
        conexionInsert.con.commit()
    except sqlite3.Error as error:
        print("Error:", error)

    conexionInsert.con.close()

#consultas comentarios
def select_comments(id_movies: str):
    conexionSelect = Conexion("SELECT person, comment, date FROM comments WHERE id_movies = ? ORDER BY id DESC", [id_movies])
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.con.close()
    return resp

def insert_comment(data):
    try:
        conexionInsert = Conexion("INSERT INTO comments (id_movies, person, comment, date) VALUES (?, ?, ?, ?)", data)
        conexionInsert.res
        conexionInsert.con.commit()
    except sqlite3.Error as error:
        print("Error:", error)

    conexionInsert.con.close()