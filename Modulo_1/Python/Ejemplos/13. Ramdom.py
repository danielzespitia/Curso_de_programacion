# El uso del import Random
import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

print("Número aleatorio entre 1 y 10:", numero_aleatorio)

# Generar un número aleatorio entre 1 y 100
numero_aleatorio_100 = random.randint(1, 100)
print("Número aleatorio entre 1 y 100:", numero_aleatorio_100)

# Generar un número aleatorio entre 1 y 1000
numero_aleatorio_1000 = random.randint(1, 1000)
print("Número aleatorio entre 1 y 1000:", numero_aleatorio_1000)

"""
Ejemplo de uso del módulo random en Python

El .randint devuelve un numero aleatorio dentro de un rango especificado.
Puedes cambiar los valores del rango para obtener números aleatorios en diferentes intervalos.  

Puedes usar random.randint(a, b) para obtener un número entero aleatorio entre a y b, incluyendo ambos extremos.
Puedes usar random.random() para obtener un número de punto flotante aleatorio entre 0.0 y 1.0.

Puedes usar random.choice(lista) para seleccionar un elemento aleatorio de una lista.
Puedes usar random.shuffle(lista) para mezclar los elementos de una lista en su lugar.
Puedes usar random.sample(lista, k) para obtener una muestra aleatoria de k elementos de una lista.

"""