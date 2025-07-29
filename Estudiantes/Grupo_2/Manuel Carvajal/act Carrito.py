
def mostrar_menu():
    print("bienvenido al simulador de tienda \n")
    input("agg un articulo")
    agregar_articulo 

def agregar_articulo():
    nombre=input("nombre del producto a agrergar: ")
    precio = float (input("precio del prodducto a agregar: "))
    cesta_de_compra.append({"producto": nombre, "precio": precio})
    print(f"el producto {nombre} a sido agregado de manera efectiva")

def mostrar_cesta():
    if len(cesta_de_compra)==0:
        print("cesta vacia empieza a llenarla! \n")
    else:
        print("Lista de compra")
        for item in cesta_de_compra:
            print(f"{item ['producto']} / {item['precio']}$")

def gestionar():
    while True:
        
        opcion=input("seleciona una obcion (1-3) \n 1= agregar producto \n 2= mostrar cesta \n 3= mostrar menu \n escoje! :    \n")

        if opcion == '1':
            agregar_articulo()
        elif opcion == '2':
            mostrar_cesta()
        elif opcion == '3':
            mostrar_menu()
        else:
            print("obcion no valida esjoge (1-3)")

        






print("bienvenido al simulador de tienda llenemos la cesta  \n")

cesta_de_compra= []

nombre=input("nombre del producto a agrergar: ")
precio = float (input("precio del prodducto a agregar: "))
cesta_de_compra.append({"producto": nombre, "precio": precio})
print(f"el producto {nombre} a sido agregado de manera efectiva")

opcion=input("pon gestionar :  ")
if opcion == gestionar:
   gestionar()
else:
    gestionar()











































































































































































































