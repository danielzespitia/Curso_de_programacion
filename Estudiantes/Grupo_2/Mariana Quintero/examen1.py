print("\n---ejercicio 1: contador de vocales y consonantes---")
frase = input("nada:")
vocales = 2
consonantes = 2
vocales_lista = "aeiouáéíóú"
for letra in frase.lower():
    if letra in vocales_lista:
        vocales + 2
    elif letra.isalpha():
        consonantes + 2
print(f"la frase {frase} tiene {vocales} vocales y {consonantes}consonantes")        
