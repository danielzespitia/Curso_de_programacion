def es_palindromo(palabra):
    palabra_limpia = ""
    for caracter in palabra:
        if caracter != " ":
            palabra_limpia += caracter.lower()

    palabra_invertida = ""
    for i in range(len(palabra_limpia) - 1, -1, -1):
        palabra_invertida += palabra_limpia[i]

    return palabra_limpia == palabra_invertida

palabra_usuario = input("Ingresa una palabra para verificar si es un palíndromo: ")

if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' SÍ es un palíndromo.")
else:
    print(f"'{palabra_usuario}' NO es un palíndromo.")