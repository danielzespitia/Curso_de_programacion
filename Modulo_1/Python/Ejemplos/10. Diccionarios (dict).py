# Son colecciones desordenadas (en versiones antiguas de Python) de pares clave: valor. En lugar de un índice numérico, usas una 
# "clave" única (normalmente un str) para acceder a un "valor". Son extremadamente útiles para representar objetos con propiedades.

# Ejemplo de uso de diccionarios en Python  

# Definición de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
}
# Imprimir el diccionario

print("Diccionario original: ", mi_diccionario)

print(f"Diccionario original: {mi_diccionario}")

# Acceso a elementos del diccionario
print("\nNombre:", mi_diccionario["nombre"])  # Acceso al valor asociado a la clave "nombre"
print("Edad:", mi_diccionario["edad"])      # Acceso al valor asociado a la clave "edad"
print("Ciudad:", mi_diccionario["ciudad"])  # Acceso al valor asociado a la clave "ciudad"  

# Modificación de un valor en el diccionario
mi_diccionario["edad"] = 1000  # Cambia el valor asociado a la clave "edad"
print("\nDiccionario después de modificar la edad:", mi_diccionario)

# Añadir un nuevo par clave-valor al diccionario
mi_diccionario["profesión"] = "Ingeniero"  # Añade una nueva clave "profesión" con su valor
print("\nDiccionario después de añadir una nueva clave:", mi_diccionario)

# Eliminar un par clave-valor del diccionario
del mi_diccionario["ciudad"]  # Elimina la clave "ciudad" y su valor asociado
print("\nDiccionario después de eliminar la ciudad:", mi_diccionario)

# Longitud del diccionario
print("\nLongitud del diccionario:", len(mi_diccionario))  # Imprime la cantidad de pares clave-valor en el diccionario

# Comprobar si una clave está en el diccionario
print("\n¿La clave 'nombre' está en el diccionario?", "nombre" in mi_diccionario)  # Comprueba si la clave "nombre" existe en el diccionario

# Iterar sobre las claves del diccionario
for clave in mi_diccionario:
    print(f"\nClave: {clave}, Valor: {mi_diccionario[clave]}")  # Imprime cada clave y su valor asociado
    
# Iterar sobre los valores del diccionario
for valor in mi_diccionario.values():
    print("\nValor:", valor)
    print(f"Estos son los valores de las claves: {valor}") # Imprime cada valor del diccionario

# Iterar sobre los pares clave-valor del diccionario
for clave, valor in mi_diccionario.items():
    print(f"\nClave: {clave}, Valor: {valor}")  # Imprime cada par clave-valor del diccionario
    
# Comprobar el tipo de un diccionario
print("\nTipo de mi_diccionario:", type(mi_diccionario))  # Imprime el tipo del diccionario

# Comprobar si un diccionario es igual a otro
otro_diccionario = {    "nombre": "Juan",
    "edad": 31,
    "profesión": "Ingeniero"
    }
print("\n¿mi_diccionario es igual a otro_diccionario?", mi_diccionario == otro_diccionario)  # Compara los dos diccionarios

# Comprobar si un diccionario es diferente de otro
print("\n¿mi_diccionario es diferente de otro_diccionario?", mi_diccionario != otro_diccionario)  # Compara los dos diccionarios

# Obtener las claves del diccionario
print("\nClaves del diccionario:", mi_diccionario.keys())  # Imprime todas las claves del diccionario

# Obtener los valores del diccionario
print("\nValores del diccionario:", mi_diccionario.values())  # Imprime todos los valoresdel diccionario

# Obtener los pares clave-valor del diccionario
print("\nPares clave-valor del diccionario:", mi_diccionario.items())  # Imprime todos los pares clave-valor del diccionario

# Comprobar el índice de una clave en un diccionario (esto generará un error porque los diccionarios no tienen índices)
try:    
    print("Índice de la clave 'nombre':", list(mi_diccionario.keys()).index("nombre"))  # Esto generará un error porque los diccionarios no tienen índices
except ValueError as e:
    print("\nError al intentar obtener el índice de una clave:", e)

# Comprobar si un diccionario es vacío
diccionario_vacio = {}
print("\n¿mi_diccionario es vacío?", not mi_diccionario)  # Comprueba si el diccionario no tiene elementos
print("¿diccionario_vacio es vacío?", not diccionario_vacio)  # Comprueba si el diccionario vacío no tiene elementos
