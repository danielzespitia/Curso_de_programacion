print("\n--- Ejercicio 7: Agenda de Contactos ---")
agenda = {}
while True:
            print("\n--- MENÚ AGENDA ---")
            print("1. Añadir un contacto")
            print("2. Buscar un contacto")
            print("3. Listar todos los contactos")
            print("4. Volver al menú principal")
            opcion_agenda = input("Elige una opción: ")
            if opcion_agenda == '1':
                nombre = input("Nombre del contacto: ")
                telefono = input("Teléfono del contacto: ")
                agenda[nombre] = telefono
                print(f"Contacto '{nombre}' añadido.")
            elif opcion_agenda == '2':
                nombre = input("Nombre del contacto a buscar: ")
                telefono = agenda.get(nombre, "Contacto no encontrado.")
                print(f"Teléfono: {telefono}")
            elif opcion_agenda == '3':
                if agenda:
                    print("Lista de contactos:")
                    for nombre, telefono in agenda.items():
                        print(f"- {nombre}: {telefono}")
                else:
                    print("La agenda está vacía.")
            elif opcion_agenda == '4':
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
