"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
import os
os.system("clear")

tupla1 = ("apple","banana","cherry")  #a la tupla no se le agregan valores ni se eliminan no pueden cmabiar se recomienda que solo ea 
print(tupla1)
print(tupla1[0])

tupla2 = ("abc",34,True,40,"male")
print(tupla2)

#Metodos de tuplas
#count() Returns the number of times specifed value occurs in a tuple
#index() Searches the tuple for a specified value and returns the position of where was found