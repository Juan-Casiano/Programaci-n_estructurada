"""

 
 Sets.- 
  Es un tipo de datos tambien llamados conjuntos que sirven  para tener una coleccion de valores pero no tiene ni indice ni orden t

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")



paises = {"México","Brasil","Canada"} #conjunto que muestra en el orden que se le de la gana 

vario = {True,"Cadena",23,3.1416}
print(vario)

#operaciones de los sets
paises.add("Mexico")
print(paises)

vario.pop() #aqui no hay que ponerle el idice como en la lista (elimina uno aleatorio)
print(vario)
      
vario.remove("Cadena")
print(vario)


"""
Crear un programa qeu solicite los email de los alumnos de la UTD almacenar en uan lista posteriormente mostrar en pantalla
los email duplicados
"""
email = []
alumno = []
import os
os.system("cls")
resp = "SI"


while resp == "SI" :
  email.append(input("Escriba un emal: "))
  resp = input("deseas agregar otro email?: ")
  
  email_set = set(email)
  email = list(email_set)
  print(email)



        

