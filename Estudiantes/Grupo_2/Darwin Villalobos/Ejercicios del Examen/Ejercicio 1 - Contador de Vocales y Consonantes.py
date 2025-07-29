def contar_vocales_consonantes():
    frase = input("Ingresa una frase: ")
    frase = frase.lower()

    vocales = "aeiou"
    contador_vocales = 0
    contador_consonantes = 0

    for letra in frase:
        if letra.isalpha():
            if letra in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    print(f"La frase '{frase}' tiene {contador_vocales} vocales y {contador_consonantes} consonantes.")

contar_vocales_consonantes()