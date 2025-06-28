#lista = [
#        ["Ruben",10.0,8.9,9.1],
#        ["Andres",10.0,10.0,10.0],
#        ["Maria",10.0,10.0,10.0]        
#        ]
lista = []
def borrarPantalla():
       import os 
       os.system("cls")

def esperarTecla():
        input("Oprima cualquier telca para continuar")

def menu_principal():
        accion = input("\t\t\t..::BIENVENIDO A ADMINISTRADOR DE CALIFICACIONES::..\n\t\#Escpja la accion que quiera realizar\n1.- Agregar calificación\n2.- Mostrar calificacioens\n3.- Calcular promedio de califiaciones\n4.- Salir")

        return accion

def agregar_calificaciones(datos):
    borrarPantalla()
    print("\n..::: AGREGAR CALIFICACIONES :::..\n")
    
    while True:
        opcion = input("¿Agregar nuevo alumno? (si/no): ").lower().strip()
        if opcion != "si" and opcion != "no":
            print("¡Error! Ingrese solo 'si' o 'no'")
            continue
            
        if opcion == 'no':
            return datos
            
        # Captura de datos
        alumno = []
        alumno.append(input("Nombre del alumno: ").upper().strip())
        
        # Validación de 3 calificaciones
        calif = []
        for i in range(3):
            while True:

                    calif = float(input(f"Calificación {i+1} (0-10): "))
                    if calif >= 0 and calif <= 10:
                        alumno.append(calif)
                        break
                    else:
                        print("¡Error! La calificación debe ser entre 0 y 10")

        datos.append([alumno])
        print(f"\n¡Alumno {alumno[0]} agregado con éxito!")
        print(f"Calificaciones: {alumno[1:]}")

        return datos

def mostrar_calificaciones(datos):
        borrarPantalla()
        print("\n..::: MOSTRAR CALIFICACIONES :::..\n")
        if len(datos) > 0:
                print(f"{'nombre'[0]:<15}   {'califiacion.1'[1]:<10}   {'califiacion.1'[2]:<10}   {'califiacion.1'[3]:<10}   ")
                print("-"*60)
                for fila in datos:
                 print(f"{fila[0]:<15}   {fila[1]:<10}   {fila[2]:<10}   {fila[3]:<10}")
                print("-"*60)
                print(f"son {len(datos)} alumnos")
        else:
                print("No hay califiacioens existenetes")

def calcular_promedios (datos):
        borrarPantalla()
        print("\n..::: PROMEDIOS DE ALUMNOS :::..\n")
        if len(datos) > 0:
                print(f"{'nombre'[0]:<15}   {'Promedio':<10}   ")
                print("-"*60)
                for fila in datos:
                 promedio = ({fila[1]}+{fila[2]}+{fila[3]})/3
                 nombre = fila[0]
                 print(f"{nombre:<15}  {promedio:.2f} ")
                 promedioGeneral += promedio
                print("-"*60)
                print(f"El promedio del grupo es: {promedio/3:.2f}")
        else:
                print("No hay califiacioens existenetes")