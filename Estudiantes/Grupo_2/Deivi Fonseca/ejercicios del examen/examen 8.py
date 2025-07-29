print("Elementos Comunes entre Dos Listas")
lista1 = [1, 2, 3, 4, 5, "hola"]
lista2 = [4, 5, 6, 7, 8, "hola"]
comunes = list(set(lista1) & set(lista2))
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Elementos comunes: {comunes}")