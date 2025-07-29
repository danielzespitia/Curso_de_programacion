def es (palabra):
    palabra_palindromo = palabra.lower().replace(" ","")
    if palabra_palindromo == palabra_palindromo[::-1]:
        return True
    else:
        return False
if __name__ == "__main__":
    Palabra_del_usuario = input("Por favor, escribe una palabra aqui y descubre si es un palindromo>")
    if es(Palabra_del_usuario):
        print(f"'{Palabra_del_usuario}' Si es un palindromo")
    else:
        print(f"'{Palabra_del_usuario}' No es un palindromo")

