from conexionBD import *
import datetime #se obtien fecha y hora 

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha = datetime.datetime.now() #regresame la fecha actual y la guardas en una variable llamda fecha
        sql = "insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s)"
        val = (nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    except:
        return False
    
def iniciar_sesion(email,contrasena):
    try:
        sql = "selct * from usuarios where email = %s and password=%s"
        val = (email,contrasena)
        cursor.execute(sql,val)
        registro = cursor.fetchone
        if registro:
            return registro 
        else:
            return None

    except:
        return None