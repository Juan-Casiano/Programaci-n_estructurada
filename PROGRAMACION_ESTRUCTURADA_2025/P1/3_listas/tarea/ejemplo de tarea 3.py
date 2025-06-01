"""
Ejemlo 1:
Crear una lista de numeros e imrimir el contenido
"""
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
print(lista_numeros)


#ejemplo de profe
variable = "["
for i in lista_numeros:
 variable += f"{i},"    #acomulador de cadenas
 print(f"{variable}]")

 variable = "["
 for i in range (0,len(lista_numeros)):
     variable += f"{i},"
     print(f"{variable}]")



#---------------------------------------------------------------------------------------------


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


#2da forma de ahcerlo (ejemplo del profe)
encontro = False
cuantas = 0
posiciones = []
for i in lista_palabras:
    lista_palabras = ["hola","hi","quiuvo","hi","pato","claxon","agua","pato"]
busqueda = input("que palabra desea buscar?")
if i == busqueda:
    encontro = True
    cuantas += 1
    posiciones.append(lista_palabras.index(i))
    print(f"la posicion de la palabra es: {posiciones}")
    
if encontro==True:
    print("si encontro la variable")
else:
    print("no encontro la palabra")



#3er forma (ejemplo de profe )
encontro = False
cuantas = 0
posiciones = []
lista_palabras = ["hola","hi","quiuvo","hi","pato","claxon","agua","pato"]
busqueda = input("que palabra desea buscar?")
for i in range(0,len(lista_palabras)):

 if i :
    encontro = True
    cuantas += 1
    posiciones.append(lista_palabras.index(i))
    print(f"la posicion de la palabra es: {posiciones}")
    
if encontro==True:
    print("si encontro la variable")
else:
    print("no encontro la palabra")
#-------------------------------------------------------------------------------------

"""
ejemplo 3:
añadir elementos a la lista
"""
lista_palabras.insert(1,"México")
print(lista_palabras)

"""
ejemplo 4:
crear una lista para almacenar numeros y nombres de personas (agenda)
"""
os.system("cls")
opcion = 1
agenda_num = []
agenda_name = []
while opcion == 1 :
    opcion = int(input("\t\t..::Bienvenido a su agenda::..\n\tSeleccione el numero de la opcion qeu desea:\n1.-Agregar persona\n2.-Buscar perosna\n3.-Finalizar"))
    if opcion == 1:
        nombre1 = input("\tIngrese el nombre de la persona qeu desea aggregar a su agenda")
        numero1 = input("\tIngrese el numero de la persona qeu desea aggregar a su agenda")
        agenda_name.append(nombre1)
        agenda_num.append(numero1)
        input("agregado de manera adecuada, presione enter para continuar")
    elif opcion == 2:
        persona = input("ingrese el nommbre de la persona que busca: ")
        if persona in agenda_name:
            posiocon = agenda_name.index(persona)
            print(f"El nombre es: {agenda_name[posiocon]}\t\tEl numero es: {agenda_num[posiocon]}")
            


#ejemplo del profe
agenda = [
    "carlos","6182904416"
    "carlos V","6182904415"
    "carlos Vl","6182904417"
]
for i in agenda:
    print(i)

for r in range (0,3):
    for c in range (0,2):
        lista += print(f"(agenda{r}{c}),") #r c son como las cordenadas de como esta la posicon de la agenda
        lista+="\n\t"