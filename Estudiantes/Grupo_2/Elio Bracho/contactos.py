def mostrar_menu():
    print("\nContactos")
    print("1. añadir")
    print("2. buscar")
    print("3. lista de contactos")
    print("4. salir")
def añadir_contactos(lista):
    nombre = input("\nNombre de tu contacto> ").strip().capitalize()
    numero = input(f"\nnumero de {nombre}> ").strip()
    if numero and nombre:
        lista[nombre] = numero
        print(f"\n{nombre} ha sido añadido con exito")
    else:
        print("\nError, escribe un nombre y un numero para poder buscarlo")
def buscar(lista):
    if not lista:
        print("\nAun no tienes contactos, agrega alguno para ver la lista de conactos")
        return
    buscar_contacto = input("Introduce el nombre del contacto a que quieres buscar> ").strip().capitalize()
    if buscar_contacto in lista:
        print(f"\nTu contacto es {buscar_contacto}-{lista[buscar_contacto]}")
    else:
        print(f"\nel contacto '{buscar_contacto} no existe")
def lista_de_contactos (lista):
    if not lista:
        print("\nAun no tienes contactos para ver")
        return
    print("\n>>>>Contactos<<<<")
    for nombre, numero, in sorted(lista.items()):
        print(f"{nombre}:{numero}")
def main():
    lista_contactos = {}
    while True:
        mostrar_menu ()
        opcion = input("elige una opcion (1-4)> ").strip()
        if opcion == "1":
            añadir_contactos (lista_contactos)
        elif opcion == "2":
            buscar (lista_contactos)
        elif opcion == "3":
            lista_de_contactos (lista_contactos) 
        elif opcion == "4":
            print("\nGracias por usar")
            break
        else:
            print("\nopcion no valida, intenta de nuevo con un numero del 1 al 4")
if __name__ == "__main__":
    main()
