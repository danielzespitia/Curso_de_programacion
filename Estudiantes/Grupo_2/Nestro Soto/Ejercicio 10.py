print("\n--- Ejercicio 10: Dibujando un Triángulo con Asteriscos ---")
entrada = input("Ingresa la altura del triángulo (un número entero): ")
if entrada.isdigit():
    altura = int(entrada)
    if altura <= 0:
        print("Por favor, ingresa un número positivo.")
    else:
        print(f"Triángulo de altura {altura}:")
        for i in range(1, altura + 1):
            print('*' * i)
else:
    print("Entrada no válida. Debes ingresar un número entero positivo.")