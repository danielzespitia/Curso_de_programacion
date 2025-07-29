def suma_numeros_pares(lista_numeros):
    suma_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma_pares += numero
    return suma_pares

if __name__ == "__main__":
    numeros = [40, 54, 23, 93, 247, 892, 1365, 1927, 2583, 3137]
    resultado = suma_numeros_pares(numeros)
    print(f"La suma de los números pares es: {resultado}")