#ejercicio 2
"""adivina el numero"""

import random

numero_secreto = random.randint(1, 200)
intentos = 0
print("¡Adivina el número! Está entre 1 y 200.")
while True:
    entrada = input("Ingresa tu número: ")
    if entrada.isdigit():
        suposicion = int(entrada)
        intentos += 1
    if suposicion < numero_secreto:
        print("El número secreto es MAYOR.")
    elif suposicion > numero_secreto:
        print("El número secreto es MENOR.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break
else:
                print("Por favor, ingresa solo números enteros.")