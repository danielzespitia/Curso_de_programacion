#ejercicio 1

"""contador de vocales y consonantes"""
#objetivo: practicar bucles for y condicionales if-elif y else con cadenas de texto

print("\n--- Ejercicio 1: Contador de Vocales y Consonantes ---")
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