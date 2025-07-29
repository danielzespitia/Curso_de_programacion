def Mostrar_menú():
    print("\n¡Bienvenido a tu carrito de compras!")
    print("1. Agregar un nuevo producto al carrito.")
    print("2. Mostrar el contenido del carrito.")
    print("3. Eliminar un producto del carrito.")
    print("4. Calcular el total de tu compra.")
    print("5. Salir.")
    print("________________________________________")
def agregar_produto (carrito):
    nombre = input("ingresa el nombre del producto: ").strip().capitalize()
    while True:
        try:
            precio = float (input(f"ingresa el precio de {nombre}: "))
            if precio<=0:
                print("El precio tiene que ser un numero positivo, intenta de nuevo")
            else:
                break
        except ValueError:
            print("Entrada no reconocida, introduce un numero para el precio")
    carrito[nombre] = precio
    print(f"'{nombre}' agregado al carrito por ${precio:.2f}.")
def mostrar_carrito (carrito):
    if not carrito:
        print("tu carrito de compras esta vacio, agrega productos para continuar.")
        return
    print("\n>>>>>>Contenido de tu carrito<<<<<<")
    for nombre, precio in carrito.items():
        print(f"-{nombre}: ${precio:.2f}")
    print("________________________________________")
def eliminar_producto (carrito):
    if not carrito:
        print("El carrito esta vacio, no hay nada que eliminar.")
        return
    producto_a_eliminar = input("Ingresa el nombre del producto a eiminar:").strip().capitalize()
    if producto_a_eliminar in carrito:
        del carrito[producto_a_eliminar]
        print(f"'{producto_a_eliminar}' ha sido eliminado del carrito.")
    else:
        print("E producto no fue encontrado en la cesta.")
def calcular_total (carrito):
    if not carrito:
        print("El carrito esta vacio, el total es $0.00.")
        return
    total = sum(carrito.values())
    print(f"\n>>>>>>Resumen de compra<<<<<<")
    for nombre, precio in carrito.items():
        print(f">{nombre}: ${precio:.2f}")
    print(f"__________________________")
    print(f"Total: ${total:.2f}")
    print("__________________________")
def main():
     carrito_de_compras =  {}
     while True:
        Mostrar_menú()
        opcion = input("Elige una opcion (1-5): ").strip()
        if opcion == '1':
            agregar_produto(carrito_de_compras)
        elif opcion == '2':
            mostrar_carrito(carrito_de_compras)
        elif opcion == '3':
            eliminar_producto(carrito_de_compras)
        elif opcion == '4':
            calcular_total(carrito_de_compras)
        elif opcion == '5':
            print("¡Gracias por utilizar el simulador de carrito de compras!")
        else:
            print("Esta opcion no es valida, por favor, escribe un numero del 1 al 5.")
if __name__=="__main__":
    main() 
