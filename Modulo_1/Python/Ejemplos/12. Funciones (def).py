# Una función es un bloque de código con un nombre que realiza una tarea específica. 
# Se "define" una vez y se puede "llamar" o ejecutar cuantas veces se quiera. Esto evita repetir código.
# Las funciones pueden recibir "parámetros" (datos de entrada) y devolver "resultados" (datos de salida).
# Las funciones son útiles para organizar el código, hacerlo más legible y reutilizable.

# Ejemplo de uso de funciones en Python
def saludar(nombre):
    """Función que saluda a una persona."""
    print(f"¡Hola, {nombre}!")
# Llamada a la función saludar
saludar("Juan")  # Imprime: ¡Hola, Juan!

def sumar(a, b):
    """Función que suma dos números y devuelve el resultado."""
    return a + b
# Llamada a la función sumar
resultado = sumar(5, 30)  # Llama a la función y guarda el resultado en la variable resultado
print(f"La suma de 5 y 3 es: {resultado}")  # Imprime: La suma de 5 y 3 es: 8


def multiplicar(a, b=2):
    """Función que multiplica dos números. El segundo número es opcional y por defecto es 2."""
    return a * b    

# Llamada a la función multiplicar con un solo argumento
resultado_multiplicacion = multiplicar(40)  # Usa el valor por defecto para b
print(f"4 multiplicado por 2 es: {resultado_multiplicacion}")  # Imprime: 4 multiplicado por 2 es: 8

# Llamada a la función multiplicar con dos argumentos   
resultado_multiplicacion_con_dos = multiplicar(4, 3)  # Usa 3 como segundo argumento
print(f"4 multiplicado por 3 es: {resultado_multiplicacion_con_dos}")  # Imprime: 4 multiplicado por 3 es: 12

def calcular_area_rectangulo(base, altura):
    """Función que calcula el área de un rectángulo."""
    return base * altura
# Llamada a la función calcular_area_rectangulo
area = calcular_area_rectangulo(5, 3)  # Calcula el área de un rectángulo de base 5 y altura 3
print(f"El área del rectángulo es: {area}")  # Imprime: El área del rectángulo es: 15

def calcular_area_circulo(radio):
    """Función que calcula el área de un círculo."""
    import math  # Importa el módulo math para usar la constante pi
    return math.pi * (radio ** 2)  # Calcula el área usando la fórmula π * r^2
radio2 = calcular_area_circulo(4)  
print(f"El area del circulo es: {radio2:.2f}") 

