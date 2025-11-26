# Lista para almacenar los contactos.
# Cada contacto será un diccionario.
contactos = []

print("--- Gestor de Contactos ---")

# Bucle principal del programa
while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Añadir un nuevo contacto")
    print("2. Buscar un contacto por nombre")
    print("3. Mostrar todos los contactos")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    # --- Opción 1: Añadir Contacto ---
    if opcion == '1':
        print("\n--- Añadir nuevo contacto ---")
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        
        # Crear el diccionario del contacto y añadirlo a la lista
        contactos.append({
            "nombre": nombre,
            "telefono": telefono
        })
        
        print(f"¡Contacto '{nombre}' añadido con éxito!")

    # --- Opción 2: Buscar Contacto ---
    elif opcion == '2':
        print("\n--- Buscar contacto ---")
        if not contactos:
            print("No hay contactos en la agenda para buscar.")
        else:
            nombre_buscado = input("Introduce el nombre del contacto a buscar: ")
            
            encontrado = False
            for contacto in contactos:
                # Comprueba si el nombre coincide (ignorando mayúsculas/minúsculas)
                if contacto["nombre"].lower() == nombre_buscado.lower():
                    print("\n¡Contacto encontrado!")
                    print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
                    encontrado = True
                    break # Detiene el bucle si ya lo encontró
            
            if not encontrado:
                print(f"No se encontró ningún contacto con el nombre '{nombre_buscado}'.")

    # --- Opción 3: Mostrar Todos los Contactos ---
    elif opcion == '3':
        print("\n--- Lista de contactos ---")
        if not contactos:
            print("No hay contactos en la agenda.")
        else:
            # Itera sobre la lista y muestra cada contacto
            for contacto in contactos:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")

    # --- Opción 4: Salir ---
    elif opcion == '4':
        print("¡Hasta luego!")
        break # Termina el bucle while y finaliza el programa

    # --- Opción no válida ---
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")