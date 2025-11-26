# Son colecciones ordenadas pero inmutables (no se pueden cambiar una vez creadas). Son más rápidas y seguras para datos que no deben modificarse, como coordenadas (x, y).

# Son como un tren de vagones donde cada vagón tiene un número (índice) y no puedes cambiar lo que hay dentro, pero puedes ver lo que hay en cada vagón.

# Ejemplo de uso de tuplas en Python

# Definición de una tupla
mi_tupla = (1, 2, 3, 4, 5)
# Imprimir la tupla     
print("Tupla original:", mi_tupla)

# Acceso a elementos de la tupla
print("Primer elemento:", mi_tupla[0])  # Acceso al primer elemento
print("Último elemento:", mi_tupla[-1])  # Acceso al último elemento
# Intento de modificar un elemento de la tupla (esto generará un error)
try:
    mi_tupla[2] = 10  # Esto generará un error porque las tuplas son inmutables
except TypeError as e:  
    print("Error al intentar modificar un elemento de la tupla:", e)

# Añadir un elemento a una tupla (esto generará un error)
try:
    mi_tupla.append(6)  # Esto generará un error porque las tuplas no tienen el método append
except AttributeError as e:
    print("Error al intentar añadir un elemento a la tupla:", e)

# Longitud de la tupla
print("Longitud de la tupla:", len(mi_tupla))  # Imprime la cantidad de elementos en la tupla

# Concatenar tuplas
otra_tupla = (6, 7, 8)  # Otra tupla    
mi_tupla_concatenada = mi_tupla + otra_tupla  # Concatenación de tuplas
print("Tupla concatenada:", mi_tupla_concatenada)   

# Repetir una tupla
mi_tupla_repetida = mi_tupla * 2  # Repite la tupla dos veces
print("Tupla repetida:", mi_tupla_repetida)

# Comprobar si un elemento está en la tupla
print("¿El número 3 está en la tupla?", 3 in mi_tupla)

# Desempaquetado de tuplas
a, b, c, d, e = mi_tupla  # Asigna cada elemento de la tupla a una variable
print("Desempaquetado de tupla:", a, b, c, d, e)

# Iterar sobre una tupla
for elemento in mi_tupla:
    print("Elemento de la tupla:", elemento)    

# Comprobar el tipo de una tupla
print("Tipo de mi_tupla:", type(mi_tupla))  # Imprime el tipo de la tupla

# Comprobar si una tupla es igual a otra
otra_tupla_igual = (1, 2, 3, 4, 5)
print("¿mi_tupla es igual a otra_tupla_igual?", mi_tupla == otra_tupla_igual)  # Compara las dos tuplas

# Comprobar si una tupla es diferente de otra
print("¿mi_tupla es diferente de otra_tupla?", mi_tupla != otra_tupla)  # Compara las dos tuplas

# Comprobar el índice de un elemento en una tupla
print("Índice del número 3 en mi_tupla:", mi_tupla.index(3))  # Imprime el índice del número 3 en la tupla  

# Comprobar la cuenta de un elemento en una tupla
print("Número de veces que aparece el número 2 en mi_tupla:", mi_tupla.count(2))  # Imprime cuántas veces aparece el número 2 en la tupla

# Comprobar si una tupla es vacía
tupla_vacia = ()    
print("¿mi_tupla es vacía?", not mi_tupla)  # Comprueba si la tupla está vacía
print("¿tupla_vacia es vacía?", not tupla_vacia)  # Comprueba si la tupla vacía está vacía
