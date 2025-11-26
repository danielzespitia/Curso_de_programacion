# break: Rompe y sale del bucle inmediatamente.
# continue: Salta el resto del código de la iteración actual y pasa a la siguiente.

# Ejemplo de uso de break y continue en bucles

# Bucle for con break
for numero in range(10):
    if numero == 5:
        print("Número 5 encontrado, saliendo del bucle.")
        break  # Sale del bucle cuando encuentra el número 5
    print(f"Número actual: {numero}")   

# Bucle for con continue
for numero in range(10):
    if numero % 2 == 0:
        print(f"{numero} es par, saltando a la siguiente iteración.")
        continue 
        print("Hola") 
        # Salta el resto del código y pasa al siguiente número
    print(f"{numero} es impar, procesando este número.")
    
# Bucle while con break
contador = 0
while contador < 10:
    if contador == 7:
        print("Contador ha llegado a 7, saliendo del bucle.")
        break  # Sale del bucle cuando el contador llega a 7
    print(f"Contador actual: {contador}")
    contador += 1

# Bucle while con continue
contador = 0
while contador < 10:
    contador += 1  # Incrementa el contador al inicio de la iteración
    if contador % 3 == 0:
        print(f"{contador} es múltiplo de 3, saltando a la siguiente iteración.")
        continue  # Salta el resto del código y pasa al siguiente número
        print("Hola")
    print(f"Contador actual: {contador}")
    
# Bucle for con break y continue
for numero in range(10):
    if numero == 3:
        print("Número 3 encontrado, saliendo del bucle.")
        break  # Sale del bucle cuando encuentra el número 3
    if numero % 2 == 0:
        print(f"{numero} es par, saltando a la siguiente iteración.")
        continue  # Salta el resto del código y pasa al siguiente número
    print(f"Número impar: {numero}")
    
# Bucle while con break y continue
contador = 0
while contador < 10:
    contador += 1  # Incrementa el contador al inicio de la iteración
    if contador == 5:
        print("Contador ha llegado a 5, saliendo del bucle.")
        break  # Sale del bucle cuando el contador llega a 5
    if contador % 2 == 0:
        print(f"{contador} es par, saltando a la siguiente iteración.")
        continue  # Salta el resto del código y pasa al siguiente número
    print(f"Contador impar: {contador}")
