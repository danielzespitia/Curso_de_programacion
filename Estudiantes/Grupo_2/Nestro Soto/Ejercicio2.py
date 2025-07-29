 # --- Opción 2: Adivina el Número ---
import random

print("\n--- Ejercicio 2: Adivina el Número ---")
numero_secreto = random.randint(1,100)
intentos = 0
print("¡Adivina el número! Está entre 1 y 100.")
while True:
            entrada =int (input("Ingresa tu número: "))
            if entrada :
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
