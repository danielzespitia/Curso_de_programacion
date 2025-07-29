# Escribe un programa que le pida al usuario que ingrese numeros uno por uno.
# Los numeros se deben almacenar en una lista, El usuario indicara que ha terminado de ingresar numeros con la palabra "fin".
# En ese momento el programa debe calcular y mostrar el promedio de los numeros ingresados.
print("\n--- Ejercicio 3: Calculadora de Promedio ---")
numeros = []
print("Ingresa números para promediar. Escribe 'fin' para terminar.")
while True:
            entrada = input("Ingresa un número o 'fin': ")
            if entrada.lower() == 'fin':
                break
            # Validar si la entrada es un número (entero o decimal)
            try_float = entrada.replace('.', '', 1).replace('-', '', 1)
            if try_float.isdigit():
                numeros.append(float(entrada))
            else:
                print("Entrada no válida. Por favor, ingresa un número o 'fin'.")
            if numeros:
             promedio = sum(numeros) / len(numeros)
            print(f"Los números ingresados son: {numeros}")
            print(f"El promedio es: {promedio:.2f}")
else:
     print("No se ingresaron números para calcular el promedio.")


    