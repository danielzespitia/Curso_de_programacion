def mostrar_menu_principal():
    """Muestra el menú principal de opciones para el carrito."""
    print("\n--- Menú Principal del Carrito de Compras ---")
    print("1. Ver productos disponibles")
    print("2. Añadir producto al carrito")
    print("3. Ver mi carrito y total")
    print("4. Comprar (Finalizar compra)")
    print("5. Salir")
    print("--------------------------------------------")

def mostrar_productos_disponibles():
    """Muestra la lista de productos que la tienda ofrece."""
    print("\n--- Productos Disponibles ---")
    print("ID | Producto       | Precio")
    print("--------------------------------")
    print("1  | Camiseta       | $20.00")
    print("2  | Pantalón       | $45.00")
    print("3  | Zapatillas     | $70.00")
    print("4  | Gorra          | $15.00")
    print("5  | Libro          | $25.00")
    print("----------------------------\n")

def obtener_info_producto(id_producto):
    """Devuelve el nombre y precio de un producto según su ID."""
    productos = {
        1: {"nombre": "Camiseta", "precio": 20.00},
        2: {"nombre": "Pantalón", "precio": 45.00},
        3: {"nombre": "Zapatillas", "precio": 70.00},
        4: {"nombre": "Gorra", "precio": 15.00},
        5: {"nombre": "Libro", "precio": 25.00},
    }
    return productos.get(id_producto)

def añadir_al_carrito(carrito):
    """Permite al usuario añadir productos al carrito."""
    mostrar_productos_disponibles()
    while True:
        try:
            id_seleccionado = int(input("Ingresa el ID del producto que deseas añadir: "))
            if 1 <= id_seleccionado <= 5:
                break
            else:
                print("ID de producto no válido. Por favor, ingresa un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    producto = obtener_info_producto(id_seleccionado)
    if producto:
        while True:
            try:
                cantidad = int(input(f"¿Cuántas unidades de '{producto['nombre']}' quieres añadir? "))
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser un número positivo.")
            except ValueError:
                print("Cantidad inválida. Por favor, ingresa un número.")

        if producto['nombre'] in carrito:
            carrito[producto['nombre']]['cantidad'] += cantidad
        else:
            carrito[producto['nombre']] = {"precio": producto['precio'], "cantidad": cantidad}
        print(f"'{cantidad}x {producto['nombre']}' añadido(s) a tu carrito.")
    else:
        print("Error: Producto no encontrado.")

def ver_carrito(carrito):
    """Muestra el contenido actual del carrito y el total."""
    if not carrito:
        print("\nTu carrito está vacío.")
        return

    print("\n--- Contenido de tu Carrito ---")
    total_compra = 0.0
    for nombre_producto, detalles in carrito.items():
        subtotal = detalles['precio'] * detalles['cantidad']
        print(f"- {nombre_producto} (x{detalles['cantidad']}) @ ${detalles['precio']:.2f} c/u = ${subtotal:.2f}")
        total_compra += subtotal
    print("---------------------------------")
    print(f"Total a pagar: ${total_compra:.2f}")
    print("---------------------------------\n")

def finalizar_compra(carrito):
    """Procesa la compra y muestra el total final."""
    if not carrito:
        print("\nTu carrito está vacío, no hay nada que comprar.")
        return False # Indica que la compra no se realizó

    ver_carrito(carrito) # Muestra el carrito una última vez antes de confirmar
    confirmacion = input("¿Estás seguro de que quieres finalizar la compra? (s/n): ").lower()
    if confirmacion == 's':
        total_final = sum(item['precio'] * item['cantidad'] for item in carrito.values())
        print(f"\n¡Compra realizada con éxito! El total final es: ${total_final:.2f}")
        print("¡Gracias por tu compra! Esperamos verte de nuevo.")
        return True # Indica que la compra se realizó
    else:
        print("Compra cancelada. Puedes seguir añadiendo productos.")
        return False # Indica que la compra no se realizó

# --- Lógica principal del programa ---
def iniciar_carrito():
    """Función principal que ejecuta el sistema del carrito de compras."""
    carrito_actual = {} # Este diccionario guardará los productos y cantidades en la cesta

    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_productos_disponibles()
        elif opcion == '2':
            añadir_al_carrito(carrito_actual)
        elif opcion == '3':
            ver_carrito(carrito_actual)
        elif opcion == '4':
            if finalizar_compra(carrito_actual):
                break # Sale del bucle si la compra se confirma
        elif opcion == '5':
            print("Saliendo de la tienda virtual. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 5.")

# Para ejecutar el carrito, llama a la función principal:
if __name__ == "__main__":
    iniciar_carrito()