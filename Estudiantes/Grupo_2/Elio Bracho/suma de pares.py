def sumar_numeros_pares(lista_numeros):
    suma_pares = 0 
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma_pares += numero 
    return suma_pares
if __name__ == "__main__":
    numeros = [42, 50, 37, 85, 62, 48, 25, 23, 41, 10] 
    print(f"lista de numeros: {numeros}")
    pares = sumar_numeros_pares(numeros)
    print(f"suma de pares: {pares}") 