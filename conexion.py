import sqlite3
from sqlite3.dbapi2 import connect
class contactos:
    def iniciarConexion(self):
        conexion=sqlite3.connect('sistema.s3db')
        conexion.text_factory=lambda b: b.decode(errors='ignore')
        return conexion

    def leerContactos(self):
        conexion=self.iniciarConexion()
        cursor = conexion.cursor()
        sentencialSQL="SELECT * FROM contactos"
        cursor.execute(sentencialSQL)
        return cursor.fetchall()

    def crearContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="INSERT INTO contactos(nombre,correo) VALUES(?,?)"
        cursor.execute(sentencialSQL,datosContacto)
        conexion.commit()
        conexion.close()
    
    def borrarContacto(self,idContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="DELETE FROM contactos WHERE id=(?)"
        cursor.execute(sentencialSQL,[idContacto])
        conexion.commit()
        conexion.close()

    def modificarContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="UPDATE contactos SET nombre=? ,correo=? WHERE id=?"
        cursor.execute(sentencialSQL, datosContacto)
        conexion.commit()
        conexion.close()
    