# Son colecciones ordenadas y mutables (se pueden cambiar). Son como un tren de vagones donde cada vagón tiene un número (índice) y puedes cambiar lo que hay dentro.

# Ejemplo de uso de listas en Python

# Definición de una lista
mi_lista = [1, 2, 3, 4, 5]  
# Imprimir la lista
print("Lista original:", mi_lista)  
print(f"Lista original: {mi_lista}")

# Acceso a elementos de la lista
print("Primer elemento:", mi_lista[0])  # Acceso al primer elemento (índice 0)
print("Último elemento:", mi_lista[-1])  # Acceso al último elemento (índice -1)    

# Modificación de un elemento de la lista
mi_lista[2] = 10  # Cambia el tercer elemento (índice    2) a 10
print("Lista después de modificar el tercer elemento:", mi_lista)   

# Añadir elementos a la lista
mi_lista.append(6)  # Añade el número 6 al final de la lista
print("Lista después de añadir un elemento:", mi_lista)

# Insertar un elemento en una posición específica
mi_lista.insert(1, 7)  # Inserta el número 7 en la posición 1
print("Lista después de insertar un elemento en la posición 1:", mi_lista)  

# Eliminar elementos de la lista
mi_lista.remove(4)  # Elimina el primer elemento con valor 4
print("Lista después de eliminar el número 4:", mi_lista)

# Eliminar un elemento por su índice
del mi_lista[0]  # Elimina el primer elemento (índice 0)    
print("Lista después de eliminar el primer elemento:", mi_lista)

# Longitud de la lista
print("Longitud de la lista:", len(mi_lista))  # Imprime la cantidad de elementos en la lista

# Ordenar la lista
mi_lista.sort()  # Ordena la lista en orden ascendente
print("Lista ordenada:", mi_lista)

# Invertir la lista
mi_lista.reverse()  # Invierte el orden de los elementos en la lista
print("Lista invertida:", mi_lista)

# Copiar una lista
mi_lista_copia = mi_lista.copy()  # Crea una copia de la lista
print("Copia de la lista:", mi_lista_copia)

# Concatenar listas
otra_lista = [8, 9, 10]  # Otra lista para concatenar
mi_lista_concatenada = mi_lista + otra_lista  # Concatenación de listas
print("Lista concatenada:", mi_lista_concatenada)

# Repetir una lista
mi_lista_repetida = mi_lista * 2  # Repite la lista dos veces
print("Lista repetida:", mi_lista_repetida)

# Comprobar si un elemento está en la lista
print("¿El número 3 está en la lista?", 3 in mi_lista)  

# Comprobar si un elemento no está en la lista
print("¿El número 10 no está en la lista?", 10 not in mi_lista)

# Listas anidadas (listas dentro de listas)
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lista anidada:", lista_anidada)

# Acceso a elementos en listas anidadas
print("Primer elemento de la primera lista anidada:", lista_anidada[0][0])  # Acceso al primer elemento de la primera lista anidada 

# Recorrer una lista con un bucle for
for numero in mi_lista:
    print(f"Número en la lista: {numero}")  # Imprime cada número en la lista

# Recorrer una lista con un bucle while
contador = 0
while contador < len(mi_lista):
    print(f"Número en la lista (while): {mi_lista[contador]}")  # Imprime cada número en la lista
    contador += 1  # Incrementa el contador
    

