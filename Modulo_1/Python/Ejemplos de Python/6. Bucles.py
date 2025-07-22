# Bucle for: Se usa para "iterar" o recorrer una secuencia de elementos 
# (como una lista de nombres o un rango de números). Se sabe de antemano cuántas veces se va a repetir

# Imprimir los números del 0 al 4
for numero in range(5):
    print(f"Número actual: {numero}")

# Recorrer una lista de nombres
nombres = ["Ana", "Luis", "Marta"]

for nombre in nombres:
    print(f"Hola, {nombre}")
    
# Bucle for: Se usa para "iterar" o recorrer una secuencia de elementos
# (como una lista de nombres o un rango de números). Se sabe de antemano cuántas veces se va a repetir

# Bucle for con range: Se usa para repetir un bloque de código un número específico de veces
for i in range(5):  # Repite 5 veces
    print(f"Iteración {i + 1}")  # Imprime el número de iteración
    
    
    
    
    
    

# Bucle while: Se usa para repetir un bloque de código mientras una condición sea verdadera
contador = 0    
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa el contador en 1
# Nota: Asegúrate de que la condición eventualmente se vuelva falsa para evitar un bucle infinito.