import random

def adivina_el_numero():
    num_secreto = random.randint(1, 100)
    intentos = 0
    num_adivinado = False

    print("JUEGO: ADIVINA EL NUMERO SECRETO")
    print("Se ha generado un numero entre 1 y 100. A ver si adivinas cual es!!\n")

    while num_adivinado == False:
        intentos += 1
        try:
            num_usuario = int(input("Ingresa tu numero: "))
            if num_usuario < 1 or num_usuario > 100:
                print("Ingresa un numero entre el 1 y 100.\n")
                continue
        except ValueError:
            print("Entrada no valida. Debes ingresar un numero entero por intento.\n")
            continue

        if num_usuario < num_secreto:
            print("El numero que ingresaste es menor que el que debes adivinar. Intentalo con un numero mas alto.\n")
        elif num_usuario > num_secreto:
            print("El numero que ingresaste es mayor que el que debes adivinar. Intentalo con un numero mas bajo.\n")
        else:
            num_adivinado = True
            print(f"¡Felicidades. Lo lograste! Haz adivinado el numero {num_secreto} en {intentos} intentos.\n")

adivina_el_numero()
