"""
Ejemplo 2:
Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
"""
import os 
os.system("cls")

lista_palabras = ["hola","hi","quiuvo","hi","pato","claxon","agua","pato"]
busqueda = input("que palabra desea buscar?")
if busqueda in lista_palabras:
    print("Su palabra se encuentra en la lista")
else:
    print("Su palabra no esta en la lista ")

    