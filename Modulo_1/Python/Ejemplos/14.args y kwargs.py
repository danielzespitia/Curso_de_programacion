# Son una forma avanzada de manejar un número variable de argumentos.
# args: Agrupa un número indefinido de argumentos posicionales en una tupla.
# kwargs: Agrupa un número indefinido de argumentos de palabra clave en un diccionario.

def funcion_con_args(*args):
    print("Argumentos posicionales:", args)
    for arg in args:
        print(f"Argumento: {arg}")

def funcion_con_kwargs(**kwargs):
    print("Argumentos de palabra clave:", kwargs)
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Ejemplo de uso de *args
funcion_con_args(1, 2, 3, "cuatro", True)
# Ejemplo de uso de **kwargs
funcion_con_kwargs(nombre="Juan", edad=30, ciudad="Madrid")


# Ejemplo combinado de *args y **kwargs
def funcion_combinada(*args, **kwargs):
    print("\nArgumentos posicionales:", args)
    print("Argumentos de palabra clave:", kwargs)
    for arg in args:
        print(f"Argumento posicional: {arg}")
    for clave, valor in kwargs.items():
        print(f" hola{clave}: {valor}")

# Llamada a la función combinada
funcion_combinada(1, 2, 3, nombre="Ana", edad=25, ciudad="Barcelona")
# Ejemplo de uso de *args y **kwargs en una función con parámetros fijos
def funcion_con_parametros_fijos(param1, *args, **kwargs):
    print(f"Parámetro fijo: {param1}")
    print("Argumentos posicionales:", args)
    print("Argumentos de palabra clave:", kwargs)

# Llamada a la función con un parámetro fijo, *args y **kwargs
funcion_con_parametros_fijos("fijo", 4, 5, nombre="Luis", edad=28)
# Ejemplo de uso de *args y **kwargs en una función que suma números
def sumar_numeros(*args):
    suma = sum(args)  # Suma todos los números en args
    return suma
def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        
# Llamada a la función sumar_numeros
resultado_suma = sumar_numeros(1, 2, 3, 4, 5)
print(f"La suma de los números es: {resultado_suma}")  # Imprime: La suma de los números es: 15

# Llamada a la función mostrar_informacion
mostrar_informacion(nombre="Carlos", edad=35, ciudad="Valencia")
# Ejemplo de uso de *args y **kwargs en una función que imprime una lista
def imprimir_lista(*args):
    print("Elementos de la lista:")
    for elemento in args:
        print(elemento)
