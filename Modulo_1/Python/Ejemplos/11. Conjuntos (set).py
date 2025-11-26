# Son colecciones desordenadas de elementos únicos. Son muy eficientes para comprobar si un elemento pertenece a una colección y para eliminar duplicados.

# # Ejemplo de uso de conjuntos (set) en Python
# Definición de un conjunto

mi_conjunto = {1, 2, 3, 4, 5}

# Imprimir el conjunto
print("Conjunto original:", mi_conjunto)

# Acceso a elementos del conjunto (no se puede acceder por índice)
# Los conjuntos no tienen un orden definido, por lo que no se puede acceder a elementos por índice
# Sin embargo, se puede verificar si un elemento está en el conjunto
print("¿El número 3 está en el conjunto?", 3 in mi_conjunto)  # Comprueba si el número 3 está en el conjunto

# Añadir un elemento al conjunto
mi_conjunto.add(6)  # Añade el número 6 al conjunto
print("Conjunto después de añadir el número 6:", mi_conjunto)

# Intento de añadir un elemento duplicado al conjunto
mi_conjunto.add(3)  # No se añadirá porque 3 ya está en el conjunto
print("Conjunto después de intentar añadir el número 3 de nuevo:", mi_conjunto)

# Eliminar un elemento del conjunto
mi_conjunto.remove(2)  # Elimina el número 2 del conjunto
print("Conjunto después de eliminar el número 2:", mi_conjunto)

# Intento de eliminar un elemento que no está en el conjunto (esto generará un error)
try:
    mi_conjunto.remove(10)  # Esto generará un error porque 10 no está en el conjunto   
except KeyError as e:
    print("Error al intentar eliminar un elemento que no está en el conjunto:", e)
    
# Eliminar un elemento del conjunto de forma segura (sin generar error si no existe)
mi_conjunto.discard(30)  # Elimina el número 3 del conjunto si existe, no genera error si no está
print("\nConjunto después de eliminar el número 30 de forma segura:", mi_conjunto)

# Longitud del conjunto
print("Longitud del conjunto:", len(mi_conjunto))  # Imprime la cantidad de elementos en el conjunto

# Comprobar si un elemento está en el conjunto
print("¿El número 4 está en el conjunto?", 4 in mi_conjunto)

# Iterar sobre los elementos del conjunto
for elemento in mi_conjunto:
    print("Elemento del conjunto:", elemento)  # Imprime cada elemento del conjunto
    
# Comprobar el tipo de un conjunto
print("Tipo de mi_conjunto:", type(mi_conjunto))  # Imprime el tipo del conjunto

# Comprobar si un conjunto es igual a otro
otro_conjunto = {1, 4, 5, 6}  # Otro conjunto
print("¿mi_conjunto es igual a otro_conjunto?", mi_conjunto == otro_conjunto)  # Compara los dos conjuntos

# Comprobar si un conjunto es diferente de otro
print("¿mi_conjunto es diferente de otro_conjunto?", mi_conjunto != otro_conjunto)  # Compara los dos conjuntos

# Operaciones de unión, intersección y diferencia entre conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
print("Unión de conjunto_a y conjunto_b:", conjunto_a | conjunto_b)  # Unión de conjuntos
print("Intersección de conjunto_a y conjunto_b:", conjunto_a & conjunto_b)  # Intersección de conjuntos
print("Diferencia de conjunto_a y conjunto_b:", conjunto_a - conjunto_b)  # Diferencia de conjuntos
