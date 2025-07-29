def comunes(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    elementos_comunes = set1 & set2
    return list(elementos_comunes)
lista1 = [5, 6, 7, 8, 9, 12]
lista2 = [8, 9, 10, 11, 12, 6]
resultado = comunes(lista1, lista2)
print(f"lista 1: {lista1}")
print(f"lista 2: {lista2}")
print(f"elementos comunes: {resultado}")