# Cesta de compra en python 
def Menu_Cesta_de_Compra():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Bienvenido a tu Cesta de Compra ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ver cesta de compra")
    print("4. Modificar cantidad")
    print("5. Calcular total")
    print("6. Renunciar (salir)")
    print("---------------------------------------")

def main():
    """Función principal del programa de cesta de compras."""
    
    cesta_de_compra = {}
    

    precio_productos = {
        "manzana": 1.0,
        "platano": 0.5,
        "queso": 2.0,
        "pan": 1.5,
        "leche": 1.2,
        "arroz": 0.8,
        "pollo": 3.0,
        "pescado": 4.0,
        "huevo": 0.2,
        "tomate": 0.7,
        "cebolla": 0.6,
        "pasta": 0.8,
        "aceite": 1.5,
        "cafe": 2.5,
        "azucar": 1.0,
        "sal": 0.5
    }

    while True:
        Menu_Cesta_de_Compra()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            
            producto = input("Introduce el nombre del producto que quieres añadir: ").lower()
            if producto in precio_productos:
                
                while True:
                    cantidad = input(f"¿Cuántas unidades de {producto} quieres añadir? ")
                    if cantidad.isdigit():
                        cantidad = int(cantidad)
                        if cantidad <= 0:
                            print("La cantidad debe ser un número positivo.")
                        else:
                            cesta_de_compra[producto] = cesta_de_compra.get(producto, 0) + cantidad
                            print(f"{cantidad} unidades de {producto} añadidas a la cesta. Cantidad total: {cesta_de_compra[producto]}")
                            break
                    else:
                        print("Entrada no válida. Por favor, introduce un número entero para la cantidad.")
                
            else:
                print("Producto no disponible o mal escrito. Por favor, revisa la lista de productos.")

        elif opcion == "2":
            
            if not cesta_de_compra:
                print("La cesta está vacía. No hay productos para eliminar.")
                continue

            producto_a_eliminar = input("Introduce el nombre del producto que quieres eliminar: ").lower()
            if producto_a_eliminar in cesta_de_compra:
                del cesta_de_compra[producto_a_eliminar]
                print(f"{producto_a_eliminar} eliminado de la cesta.")
            else:
                print("Producto no encontrado en la cesta.")

        elif opcion == "3":
            
            print("\n--- Tu Cesta de Compra Actual ---")
            if not cesta_de_compra:
                print("La cesta de compra está vacía.")
            else:
                for producto, cantidad in cesta_de_compra.items():
                    print(f"- {producto}: {cantidad} unidades")

        elif opcion == "4":
            
            if not cesta_de_compra:
                print("La cesta está vacía. No hay productos para modificar.")
                continue

            producto_a_modificar = input("Introduce el nombre del producto que quieres modificar: ").lower()
            if producto_a_modificar in cesta_de_compra:
                while True:
                    nueva_cantidad = input(f"Introduce la nueva cantidad para {producto_a_modificar} (actualmente {cesta_de_compra[producto_a_modificar]}): ")
                    if nueva_cantidad.isdigit():
                        nueva_cantidad = int(nueva_cantidad)
                        if nueva_cantidad < 0:
                            print("La cantidad no puede ser negativa.")
                        elif nueva_cantidad == 0:
                            del cesta_de_compra[producto_a_modificar]
                            print(f"{producto_a_modificar} eliminado de la cesta al establecer la cantidad en 0.")
                            break
                        else:
                            cesta_de_compra[producto_a_modificar] = nueva_cantidad
                            print(f"Cantidad de {producto_a_modificar} actualizada a {nueva_cantidad}.")
                            break
                    else:
                        print("Entrada no válida. Por favor, introduce un número entero para la cantidad.")
            else:
                print("Producto no encontrado en la cesta.")

        elif opcion == "5":
            
            print("\n--- Cálculo del Total ---")
            if not cesta_de_compra:
                print("La cesta de compra está vacía. El total es $0.00.")
                continue
            
            total = 0
            productos_sin_precio = []
            print("Detalle de la compra:")
            for producto, cantidad in cesta_de_compra.items():
                if producto in precio_productos:
                    precio_unitario = precio_productos[producto]
                    costo_producto = cantidad * precio_unitario
                    total += costo_producto
                    print(f"- {producto}: {cantidad} unidades x ${precio_unitario:.2f} = ${costo_producto:.2f}")
                else:
                    
                    productos_sin_precio.append(producto)
                    print(f"- {producto}: {cantidad} unidades (Precio no disponible)")
            
            print(f"\nTotal a pagar: ${total:.2f}")
            if productos_sin_precio:
                print(f"Nota: Los siguientes productos no tienen precio definido y no se incluyeron en el total: {producto in productos_sin_precio}") 

        elif opcion == "6":
            
            print("Gracias por usar la cesta de compra. ¡Esperamos verte pronto!")
            break 
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú (1-6).")
main () 

