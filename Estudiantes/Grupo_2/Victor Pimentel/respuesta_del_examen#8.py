
def elementos_comunes(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    elementos_comunes_set = set1.intersection(set2)
    return list(elementos_comunes_set)

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]
    resultado = elementos_comunes(lista1, lista2)
    print(resultado)

    lista_a = [10, 20, 30, 40]
    lista_b = [30, 40, 50, 60]
    resultado_2 = elementos_comunes(lista_a, lista_b)
    print(resultado_2)