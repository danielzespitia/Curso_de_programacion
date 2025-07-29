import random
secreto = random.randint(1, 100)
intentos = 0
adivinado = False
print("Este es un juego llamado 'adivina el numero'")
print("Esoy pensando en un numero entre el 1 y el 100.")
print("¿Crees poder adivinarlo?")
while not adivinado:
    try:
        entrada = int(input("Intenta adivinar> "))
        intentos +=1
        if entrada < 1 or entrada > 100:
            print("Te dije q es entre e 1 y el 100, deja la guachafita")
        elif entrada > secreto:
            print("Te pasaste manin,usa un numero menor")
        elif entrada < secreto:
            print("Te falto manao, usa un numero mayor")
        else:
            print(f"EEEEEEERGAAAA LA PEGASTE, el numero era: ({secreto}) lo lograste en: ({intentos} intentos)")

    except ValueError:
        print("Por favor, coloca un numero entero.")