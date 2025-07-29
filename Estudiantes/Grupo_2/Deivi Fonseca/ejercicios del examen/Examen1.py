
# primera pregunta del examen

print("\n --- ejercicio 1: contador de vocales y consonantes ---")
frase = input ("ingresa una frase:")
vocales = 0
consonantes = 0
vocales_lista = "aeiouáéíóú"
for letra in frase.lower ():
    if letra in vocales_lista:
        vocales += 1
    elif letra.isalpha():
        consonantes += 1
print(f"la frase {frase}, tiene {vocales} vocales y {consonantes} consonantes") 