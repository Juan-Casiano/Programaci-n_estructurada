import os

#funciones mas ocmunes 

paises = ["Mexico","Brasil","España","Canada"]
numeros = [23,45,8,24,23,26]
varios = ["hola",3.1416,33,True]


#imprimir el contenido de lista
print(paises)
print(numeros)
print(varios)

#..::recorrer una lista e imprimir el contenido::..
#1er forma
for i in paises:
    print(i)

#para que salgan en el mismo renglos
lista = "["
for i in paises:
    lista += f"{i},"
print(lista)

#2da forma
for i in range(0,4):
    print(paises[i])

#para que salgan en el mismo renglon
for i in range (0,len(paises)):  #len sirve para medir el tamaño de cualqueier cosa en este caso el tamaño de la lsita
    lista = ""
    lsita += f"{paises[i]}"
    print(lista+"]")

#..::ordenar los elementos de una lista
os.system("clear")
print(paises)
print(numeros)
print(varios)

paises.sort
print (paises)
numeros.sort
print(numeros)
varios.sort
print(varios)

#dar vuelta a datos
varios.reverse
print(varios)
paises.reverse
print(paises)
numeros.reverse
print(numeros)