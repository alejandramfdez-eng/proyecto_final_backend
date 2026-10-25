import sqlite3

class Conexion:
    def __init__(self, sql_query, parametro=None):
        self.con = sqlite3.connect("bd_movies.db")
        self.con.row_factory = sqlite3.Row
        self.cursor = self.con.cursor()
        try:
            self.res = self.cursor.execute(sql_query, parametro or [])
        except sqlite3.Error:
            self.con.close()
            raise

    
