"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("clear")

paises = ["México","España","Canada"]

paises = {"nombre":"México",
            "capital":"CDMX",
            "poblacion":"12000000",
            "idioma":"español",
            "status":"true"
          } #tambien se usan las llaves

paises2 = {"nombre":"Brasil",
            "capital":"Brasilia",
            "poblacion":"14000000",
            "idioma":"portugues",
            "status":"true"
          } #tambien se usan las llaves

paises3 = {"nombre":"Canda",
            "capital":"Otowa",
            "poblacion":"10000000",
            "idioma":["frances","ingles"],
            "status":"true"
          } #tambien se usan las llaves

#..::FUNCIONES U OPERACIONES CON LOS DICCIONARIOS ::..

print(paises)

for i in paises:
    print(f"{i} = {paises[1]}")

#AGREGAR UN ATRIBUTO A UN DICCIONARIO HASTA AL FINAL
paises["altitud"]=3000
for i in paises:
    print(f"{i} = {paises[1]}")
    
#QUITAR UN ATRIBUTO EN PARTICULAR
paises.pop("status")
for i in paises:
    print(f"{i} = {paises[1]}")