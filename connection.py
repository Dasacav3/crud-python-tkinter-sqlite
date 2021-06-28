import sqlite3

class Connection:

    def __init__(self):
        pass

    def conn(self):
        try:
            self.con = sqlite3.connect('database/database.db')
            #print(f"Conexion exitosa a SQLite v{sqlite3.sqlite_version}");
            return self.con
        except sqlite3.Error as err:
            print("Conexion fallida")