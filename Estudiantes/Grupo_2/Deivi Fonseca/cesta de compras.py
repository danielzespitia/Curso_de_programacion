

def mostrar_menu():
    print("""
    menu de cesta de compra
    1. Agregar artículo
    2. Eliminar artículo
    3. Mostrar cesta
    4. Vaciar cesta
    5. Calcular total de la compra
    6. Salir
    
    """)

def agregar_Articulo(cesta, articulos_disponibles):
    print("agregar articulo")
    print("artículos disponibles para agregar:")
    for item, precio in articulos_disponibles.items():
        print(f"{item} (${precio:.2f})") 

    articulo_a_agregar = input("Nombre del artículo a agregar: ").lower() 

    if articulo_a_agregar in articulos_disponibles:
        cesta.append({"nombre": articulo_a_agregar, "precio": articulos_disponibles[articulo_a_agregar]})
        print(f"{articulo_a_agregar} agregado a la cesta.")
    else:
        print(f"'{articulo_a_agregar}' no es un artículo válido o no está disponible.")

def eliminar_Articulo(cesta):
    
    print("eliminar articulo")
    if not cesta:
        print("la cesta está vacía, no hay nada que eliminar.")
        
    mostrar_Cesta(cesta)
    articulo_a_eliminar = input("nombre del artículo a eliminar: ").lower()

    encontrado = False
    for i, item_en_cesta in enumerate(cesta):
        if item_en_cesta['nombre'].lower() == articulo_a_eliminar:
            cesta.pop(i)
            print(f"{articulo_a_eliminar}, eliminado de la cesta")
            encontrado = True
            break
    
    if not encontrado:
        print(f"{articulo_a_eliminar}'no se encontró en la cesta.")

def mostrar_Cesta(cesta):
    print("contenido de la cesta")
    if not cesta:
        print("La cesta está vacía.")

    for i, item in enumerate(cesta, 1):
        print(f"{i}. {item['nombre']} - ${item['precio']:.2f}")

def vaciar_Cesta(cesta):
    if not cesta:
        print("La cesta ya está vacía, no hay nada que vaciar.")
        
    cesta
    print("La cesta ha sido vaciada.")

def calcular_total(cesta):
    
    print("total de la compra")
    if not cesta:
        print("La cesta está vacía, el total es $0.00.")
        

    total = sum(item['precio'] for item in cesta)
    print(f" El total de tu compra es: ${total:.2f}")

def main():
   
    articulos_disponibles = {
        "arroz": 2.50,
        "harina": 1.80,
        "cafe": 5.20,
        "azucar": 3.00,
        "leche": 1.20,
        "mantequilla": 3.75
    }

    cesta_de_compra = []

    print("Bienvenido al Simulador de Cesta de Compra")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == '1':
            agregar_Articulo(cesta_de_compra, articulos_disponibles)
        elif opcion == '2':
            eliminar_Articulo(cesta_de_compra)
        elif opcion == '3':
            mostrar_Cesta(cesta_de_compra)
        elif opcion == '4':
            vaciar_Cesta(cesta_de_compra)
        elif opcion == '5': 
            calcular_total(cesta_de_compra)
        elif opcion == '6': 
            print("Gracias por usar el simulador de cesta de compra")
            break
        else:
            print("Opción no válida, elige un número del 1 al 6.")

main()