def draw_triangle():
    while True:
        try:
            n = int(input("Ingrese un número entero plis :v : "))
            if n <= 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    for i in range(1, n + 1):
        print("*" * i)

draw_triangle()