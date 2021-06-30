from connection import *

class Model(Connection):
    def __init__(self):
        super().__init__()

    def select(self):
        try:
            cur = self.conn().cursor()
            cur.execute("SELECT * FROM producto")
            return cur.fetchall()
        except sqlite3.Error as err:
            print(f"Hubo un problema {err}")
        finally:
            self.con.close()

    def add(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("INSERT INTO producto(nombre_producto, cantidad_producto, precio_producto) VALUES(?,?,?)",args)
            con.commit()
            return "Producto añadido correctamente"
        except sqlite3.Error as err:
            print(f"Hubo un problema {err}")
        finally:
            self.con.close()
    
    def update(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("UPDATE producto SET nombre_producto = ?, cantidad_producto = ?, precio_producto = ? WHERE codigo_producto = ?",args)
            con.commit()
            return "Producto actualizado correctamente"
        except sqlite3.Error as err:
            print(f"Hubo un problema {err}")
        finally:
            self.con.close()

    def delete(self,*args):
        try:
            con = self.conn()
            cur = con.cursor()
            cur.execute("DELETE FROM producto WHERE codigo_producto = ?",args)
            con.commit()
            return "Producto eliminado correctamente"
        except sqlite3.Error as err:
            print(f"Hubo un problema {err}")
        finally:
            self.con.close()