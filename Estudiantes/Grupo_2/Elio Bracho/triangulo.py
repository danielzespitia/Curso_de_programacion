def triangulo():
    while True:
        try:
            n = int(input("Escribe el nunmero de altura de triangulo: "))
            if n <= 0:
                print("Elige un numero positivo")
            else:
                break
        except ValueError:
            print("Te dije un numero w")
            print("\nEl triangulo:")
    for i in range(1, n + 1):
        print("*" * i)
triangulo()