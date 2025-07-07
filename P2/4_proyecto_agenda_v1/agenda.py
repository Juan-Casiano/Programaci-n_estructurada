agenda_contactos = {
    "RUBEN": ["6181234567", "ruben@example.com"] 
}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")

def menu_principal(): 
    print("\n\t\t 💾..::: Sistema de Gestión de Agenda de Contactos :::..💾 \n\n\t\t1️⃣  Agregar contacto\n\t\t2️⃣  Mostrar contactos\n\t\t3️⃣  Buscar contacto\n\t\t4️⃣  Modificar contacto\n\t\t5️⃣  Eliminar contacto\n\t\t6️⃣  SALIR")
    opcion = input("\n\t\t👉 Elige una opción (1-6): ")
    return opcion

def agregar_contacto(agenda_contactos):
    borrarPantalla()
    print("\n\t\t📥 ..::AGREGAR CONTACTO::..📥 ")
    nombre = input("\n\tNombre: ").upper().strip()
    if nombre in agenda_contactos:
        print("\n\t❌ El contacto ya existe.")
        esperarTecla()
    else:
            telefono = input("\tTeléfono: ")
            email = input("\tEmail: ").upper().strip()
            agenda_contactos[nombre] = [telefono, email]
            print("\n\t✅ Contacto agregado con éxito.")
            esperarTecla()


def mostrar_contactos(agenda_contactos):
    borrarPantalla()
    print("\n\t\t📋 ..::LISTA DE CONTACTOS::.. 📋 ")

    if not agenda_contactos:
        print("\n\t❌ No hay contactos registrados.")
        esperarTecla()
    else:
        for nombre,datos in agenda_contactos.items():
             print("-"*60)
             for nombre,datos in agenda_contactos.items():
                print(f"{'nombre':>15}   {'numero':>15}   {'email':>15}")
                print(f"{nombre}   {datos[0]:>15}   {datos[1]:>15}")
                esperarTecla
             print("-"*60)

#imprimir print(f"{i} agenda {agenda[0]:>15}")
            
def buscar_contactos(agenda_contactos):
    borrarPantalla()
    print("\n\t\t🔍 ..::BUSCAR CONTACTO::.. 🔍")
    nombre = input("\n\tNombre a buscar: ").upper().strip()
    if nombre in agenda_contactos:
        print(f"\n\t🔹 {nombre}:")
        print(f"\t   Teléfono: {agenda_contactos[nombre][0]}")
        print(f"\t   Email: {agenda_contactos[nombre][1]}")
        esperarTecla()
    else:
        print("\n\t❌ Contacto no encontrado.")
        esperarTecla()

def modificar_contacto(agenda_contactos):
    borrarPantalla()
    print("\n\t\t✏️ ..::MODIFICAR CONTACTO::..✏️")
    nombre = input("\n\tNombre del contacto a modificar: ").upper().strip()
    if nombre in agenda_contactos:
        print("\n\tDatos actuales:")
        print(f"\tTeléfono: {agenda_contactos[nombre][0]}")
        print(f"\tEmail: {agenda_contactos[nombre][1]}")
        nuevo_telefono = input("\n\tNuevo teléfono (dejar vacío para no cambiar): ").upper().strip
        nuevo_email = input("\tNuevo email (dejar vacío para no cambiar): ").upper().strip()
        if nuevo_telefono:
            agenda_contactos[nombre][0] = nuevo_telefono
        if nuevo_email:
            agenda_contactos[nombre][1] = nuevo_email
        print("\n\t✅ Contacto modificado con éxito.")
        esperarTecla()
    else:
        print("\n\t❌ Contacto no encontrado.")
        esperarTecla()

def eliminar_contacto(agenda_contactos):
    borrarPantalla()
    print("\n\t\t🗑️ ..::ELIMINAR CONTACTO::..🗑️")
    nombre = input("\n\tNombre del contacto a eliminar: ").upper().strip()
    if nombre in agenda_contactos:
        del agenda_contactos[nombre]
        print("\n\t✅ Contacto eliminado con éxito.")
        esperarTecla()
    else:
        print("\n\t❌ Contacto no encontrado.")
        esperarTecla()