import random

print("Adivina el número secreto")
numero_secreto = random.randint(1, 100)
intentos = 0
print("Adivina el número secreto que está entre 1 y 100.")
while True:
    intento_usuario = input("Ingresa tu número: ")
    if intento_usuario.isdigit(): 
        numero_aleatorio = int(intento_usuario)
        
        
        if numero_aleatorio < 1 or numero_aleatorio > 100:
            print("El número debe estar entre 1 y 100. Intenta de nuevo.")
            continue        
        intentos += 1 
        
        if numero_aleatorio < numero_secreto:
            print("El número secreto es MAYOR.")
        elif numero_aleatorio > numero_secreto:
            print("El número secreto es MENOR.")
        else:
            print(f"Felicidades adivinaste el número {numero_secreto} en {intentos} intentos.")
            break
    else:
        print("Ingresa solo números.")