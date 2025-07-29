def elementos_comunes(lista1, lista2):
    comunes = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in comunes:
            comunes.append(elemento)
    return comunes

lista1 = [12, 23, 56, 31, 167]
lista2 = [56, 2, 83, 7, 31]
resultado = elementos_comunes(lista1, lista2)
print("Los elementos que hay en comun entre las dos listas son: ", resultado)
