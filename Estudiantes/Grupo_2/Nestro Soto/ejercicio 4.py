print("\n--- Ejercicio 4: Verificador de Palíndromos ---")
palabra = input("Ingresa una palabra o frase para verificar si es un palíndromo: ")
texto_limpio = palabra.lower().replace(" ", "")
if texto_limpio == texto_limpio[::-1]:
   print(f"'{palabra}' SÍ es un palíndromo.")
else:
   print(f"'{palabra}' NO es un palíndromo.")