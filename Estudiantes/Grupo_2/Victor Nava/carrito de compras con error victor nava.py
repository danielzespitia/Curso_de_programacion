#carrito


print("Bienvenido a panaderia Jurassic Pan\nQue desea llevar?")

lista_productos = []
lista_precios = []
carrito = []
print (f"lista de productos: {lista_productos}")
print (f"lista de precios: {lista_precios}")

def acciones():
    print("\nmenu principal")
    print("1 agregar producto")
    print("2 devolver producto")
    print("3 ver productos en el carrito")
    print("4 precio total en productos")
    print("5 mejor no compro nada")

def agregar_producto(carrito):
    articulo = input("nombre del producto")
    print(f"producto agregado {articulo}")
    if not carrito:
        precio = (input("cuanto cuesta"))
        carrito[articulo] = precio
        print(f"{articulo} agregado con precio ${precio:.2f}")
        print("no agregaste productos")
    else:
        for i, articulo in enumerate(carrito, 1):
            print(f"{i}. {articulo["nombre"]}: ${articulo["precio"]:.2f}")
    print("--------------")
def devolver_producto(carrito):
    carrito = input("eliminaste este producto")
    print(f"devuelves el producto {articulo}")
    if not carrito:
        print("no devuelves el producto")
    else:
        for i, articulo in enumerate(carrito, 1):
            print(f"{i}. {articulo["nombre"]}: ${articulo["precio"]:.2f}")
    print("--------------")
def ver_productos_en_el_carrito(carrito):
    print("llevas en el carrito")
    if not carrito:
        print("no llevas nada aun")
    else:
        for i, articulo in enumerate(carrito, 1):
            print(f"{i}. {articulo["nombre"]}: ${articulo["precio"]:.2f}")
    print("--------------")
def precio_total_en_productos(carrito):
    print("precio en total de productos")
    if not carrito:
        print("no llevas nada aun, total $0")
    else:
        total = sum(articulo["precio"] for articulo in carrito)
        print(f"el total de tu compra es: ${total:.2f}")
    print("--------------")
def main():
    while True:
        acciones()
        opcion = input("que quieres? (1-5): ")

        if opcion == "1":
            agregar_producto(carrito)
        elif opcion == "2":
            devolver_producto(carrito)
        elif opcion == "3":
            ver_productos_en_el_carrito(carrito)
        elif opcion == "4":
            precio_total_en_productos(carrito)
        elif opcion == "5":
            print("mejor no compro nada")
            break
        else:
            print("intenta de nuevo")

main()
