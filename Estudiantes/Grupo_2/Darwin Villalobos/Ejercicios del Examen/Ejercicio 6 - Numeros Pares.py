numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero

print("El resultado de la suma de los numeros pares es: ", suma_pares)