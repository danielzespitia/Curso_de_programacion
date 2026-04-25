"""Bucles for

Un bucle for es una estructura de control que se utiliza para repetir un 
bloque de código un número determinado de veces.

O sea sabemos cuantas veces se va a ejecutar el bloque de código."""

# For con range
for variable_vacia in range(5):
    print(f"Numero: {variable_vacia}")
     
# For con range y paso
for variable_vacia in range(0, 10, 2): # 0 Es el inicio, 10 es el final y 2 es el paso o sea contara de 2 en 2
    print(f"Numero: {variable_vacia}")    
  
# For con range y paso negativo
for variable_vacia in range(10, 0, -1): # 10 Es el inicio, 0 es el final y -1 es el paso o sea contara de 1 en 1 hacia atras
    print(f"Numero: {variable_vacia}")
    
# For con range inicio y final
for variable_vacia in range(5, 10): # 5 Es el inicio, 10 es el final
    print(f"Numero: {variable_vacia}")    
    
# For con variables
nombre = "Python"
for letra in nombre:
    print(letra)
   
# For con listas
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
   
# For con tuplas
tupla = (1, 2, 3, 4, 5)
for numero in tupla:
    print(numero)
    
# For con conjuntos
conjunto = {1, 2, 3, 4, 5}
for numero in conjunto:
    print(numero)
       
# For con diccionarios
persona = {
    "nombre": "Juan", 
    "edad": 30, 
    "ciudad": "Madrid"
    }
for clave in persona:
# for clave in persona.keys(): # Otra forma de iterar sobre las claves del diccionario
# for valor in persona.values(): # Otra forma de iterar sobre los valores del diccionario
# for clave, valor in persona.items(): # Otra forma de iterar sobre las claves y valores del diccionario
    print(clave) # Imprime las claves del diccionario
    
#-------------------------------------------------------------------------------------------------------#

"""Bucles while:
Un bucle while es una estructura de control que se utiliza para repetir un
bloque de código mientras una condición sea verdadera.

O sea no sabemos cuantas veces se va a ejecutar el bloque de código."""

# While con contador
contador = 0
while contador < 5:
    print(f"Numero: {contador}")
    contador += 1 # Incrementamos el contador para evitar un bucle infinito
  
# While con variables
nombre = "Python"
i = 0
while i < len(nombre):
    print(nombre[i])
    i += 1 # Incrementamos el contador para evitar un bucle infinito
    
# While con booleanos
condicion = True
while condicion:
    print("La condición es verdadera")
    condicion = False # Cambiamos la condición a falsa para evitar un bucle infinito
    
# While con break
contador = 0
while True: # Bucle infinito
    print(f"Numero: {contador}")
    contador += 1
    if contador >= 5:
        break # Salimos del bucle cuando el contador sea mayor o igual a 5