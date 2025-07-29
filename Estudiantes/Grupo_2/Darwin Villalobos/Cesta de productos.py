cesta_productos = []

def agregar_producto():
    nombre = input("Ingresa el nombre del producto que quieres agregar a la cesta: ")
    precio = float(input(f"Ahora ingresa el precio para el producto {nombre}: "))
    cesta_productos.append({"producto": nombre, "precio": precio})
    print(f"El producto {nombre} ha sido agregado a la cesta correctamente.\n")

def mostrar_cesta():
    if len(cesta_productos) == 0:
        print("La cesta de productos esta vacia ¡Que esperas para llenarla!.\n")
    else:
        print("Contenido de la cesta de compras:")
        for item in cesta_productos:
            print(f"{item['producto']} - Bs.{item['precio']}")
        print("")

def eliminar_producto():
    mostrar_cesta()
    producto = input("Que producto deseas eliminar? ")
    for item in cesta_productos:
        if item['producto'].lower() == producto.lower():
            cesta_productos.remove(item)
            print(f"{producto} ha sido eliminado de la cesta.\n")
            return
    print("No se encontro el producto ingresado.\n")

def calcular_total():
    total = sum(item['precio'] for item in cesta_productos)
    print(f"El total de la compra es: Bs.{total}\n")

def mostrar_menu():
    print("CESTA DE PRODUCTOS")
    print("1. Agregar nuevo producto")
    print("2. Mostrar cesta de compras")
    print("3. Eliminar un producto")
    print("4. Calcular el total de la compra hasta ahora")
    print("5. Salir\n")

def gestionar_cesta():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_cesta()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            calcular_total()
        elif opcion == "5":
            print("Saliendo del programa... Que pases un excelente dia.")
            break
        else:
            print("Opcion no valida. Intenta con una de las disponibles.\n")

gestionar_cesta()
