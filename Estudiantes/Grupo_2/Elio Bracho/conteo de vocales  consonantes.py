oracion = input("Escribe una frase: ")
vocales_conteo = 0
consonantes_conteo= 0
vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
for caracter in oracion:
    caracter_minuscula=caracter.lower()
    if "a" <= caracter_minuscula <= "z" or caracter_minuscula in "áéíóú":
        if caracter_minuscula in vocales:
            vocales_conteo +=1
        else:
            consonantes_conteo +=1
print(f"Numero de vocales: {vocales_conteo}")
print(f"Numero de consonantes: {consonantes_conteo}")