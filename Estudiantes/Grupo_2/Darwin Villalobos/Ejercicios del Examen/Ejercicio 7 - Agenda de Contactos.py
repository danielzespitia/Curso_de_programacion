def desplegar_menu():
    print("\nAGENDA DE CONTACTOS")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Lista de todos los contactos")
    print("4. Salir")

def añadir_contacto(agenda):
    nombre = input("Nombre del contacto: ").strip()
    if nombre in agenda:
        print("Este contacto ya existe.")
    else:
        telefono = input("Numero de telefono: ").strip()
        agenda[nombre] = telefono
        print("El contacto ha sido añadido correctamente.")

def buscar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto a buscar: ").strip()
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print("Contacto no encontrado.")

def lista_de_contactos(agenda):
    if not agenda:
        print("No existen contactos guardados.")
    else:
        print("\nLISTA DE CONTACTOS:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

def agenda_contactos():
    agenda = {}
    while True:
        desplegar_menu()
        opcion = input("Selecciona una opción del 1-4: ").strip()

        if opcion == "1":
            añadir_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            lista_de_contactos(agenda)
        elif opcion == "4":
            print("Saliendo de la agenda de contactos...Adios!!")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")

agenda_contactos()
