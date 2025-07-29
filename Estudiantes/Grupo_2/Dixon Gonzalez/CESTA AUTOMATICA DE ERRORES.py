productos_de_dragon_ball = {}
print()
def agregar_producto():
    nombre = input("Pon el juguete de accion que quieras agregar a la cesta: ").lower()
    precio = float(input(f"Ahora pon el precio de tu articulo coleccionable {nombre}: "))
    productos_de_dragon_ball[nombre] = precio
    print(f"El producto {nombre} ha sido agregado a tu cesta.")
    print()
def mostrar_productos():
    print("\nAqui tienes los productos que llevas en la cesta hasta ahora: ", productos_de_dragon_ball)
    print("1. Goku")
    print("2. Vegeta")
    print("3. Gohan")
    print("4. Broly")
    print("5. Bills\n")
print()
def eliminar_producto():
    producto = input("Que producto deseas eliminar? ").lower()
    if producto in productos_de_dragon_ball:
        productos_de_dragon_ball.pop(producto)
        print(f"{producto} ha sido eliminado de la cesta.")
    else:
        print("No se encontro el producto ingresado.")
print()
while True:
    print("Opciones: 1) Agregar Juguete de Accion  2) Mostrar Juguetes de Accion 3) Eliminar Juguetes de Accion  4) chao")
    print("Por aca tienes las opciones si no es que estas ciego")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        print("MUCHISIMAS GRACIAS POR UTILIZAR NUESTRO ASISTENTE DE COMPRAS, VUELVE PRONTO AL KIOSKITO DEL GORDO")
        break
    else:
        print("Opción no válida aprende a escribir.")