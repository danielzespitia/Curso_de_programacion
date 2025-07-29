ef calculadora_promedio_sin_comentarios_ni_try_except():
    numeros = []
    print("Calculadora de Promedio")
    print("Ingresa números uno por uno. Escribe 'fin' (o 'done') cuando hayas terminado.")

    while True:
        entrada = input("Introduce un número (o 'fin' para terminar): ")

        if entrada.lower() == 'fin' or entrada.lower() == 'done':
            break
        else:
            numero = float(entrada)
            numeros.append(numero)

    if numeros:
        suma = sum(numeros)
        promedio = suma / len(numeros)
        print(f"\nHas ingresado {len(numeros)} números.")
        print(f"La suma de los números es: {suma}")
        print(f"El promedio de los números es: {promedio:.2f}")
    else:
        print("No se ingresaron números para calcular el promedio.")

calculadora_promedio_sin_comentarios_ni_try_except()