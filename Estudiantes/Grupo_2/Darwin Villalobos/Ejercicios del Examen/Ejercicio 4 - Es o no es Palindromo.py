def es_palindromo(palabra):
    palabra_limpia = palabra.replace(" ", "").lower()
    
    invertida = ""
    for letra in palabra_limpia:
        invertida = letra + invertida

    return palabra_limpia == invertida

palabra_del_usuario = input("Ingresa una palabra o frase para verificar si es un palindromo: ")

if es_palindromo(palabra_del_usuario):
    print("Si es un palindromo.")
else:
    print("No es un palindromo.")
