palabra = input("escribe una palabra: ")
vocal_conteo = 0
consonante_conteo = 0
letra = "aeiouAEIOUáéíóúÁÉÍÓÚ"
for  letra in palabra:
    caracter_minuscula=letra.lower()
    if "a" <= caracter_minuscula <= "z" or caracter_minuscula in "àèìòù":
        if caracter_minuscula in letra:
            vocal_conteo +=1
        else:
            consonante_conteo +=1
print(f"Vocales: {vocal_conteo}")
print(f"consonantes: {consonante_conteo}")
