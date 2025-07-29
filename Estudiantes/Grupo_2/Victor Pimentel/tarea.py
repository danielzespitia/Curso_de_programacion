print("\n---Ejerciocio 1: Contador de letras y consonantes---")
frase = input("Ingresa una frase: ")
vocales = 0
consonantes = 0
vocales_lista = "aeiouáéíóú"
for letra in frase.lower():
    if letra in vocales_lista:
        vocales += 1
    elif letra.isalpha():
        consonantes += 1
print(f"La frase '{frase}' tiene {vocales} vocales y {consonantes} consonantes.")