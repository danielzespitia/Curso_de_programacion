# Un módulo no es más que un archivo .py que contiene funciones y variables. Puedes importar ese archivo en otro 
# para usar su contenido. Esto permite organizar proyectos grandes en múltiples archivos.

# Ejemplo de uso de módulos en Python
import math  # Importa el módulo math para usar funciones matemáticas   
def calcular_raiz_cuadrada(numero):
    """Función que calcula la raíz cuadrada de un número."""
    return math.sqrt(numero)  # Usa la función sqrt del módulo math para calcular la raíz cuadrada

# Llamada a la función calcular_raiz_cuadrada
resultado_raiz = calcular_raiz_cuadrada(16)  # Calcula la raíz cuadrada de 16
print(f"La raíz cuadrada de 16 es: {resultado_raiz}")  # Imprime: La raíz cuadrada de 16 es: 4.0
def calcular_area_circulo(radio):
    """Función que calcula el área de un círculo."""
    import math  # Importa el módulo math para usar la constante pi
    return math.pi * (radio ** 2)  # Calcula el área usando la fórmula π * r^2

# Llamada a la función calcular_area_circulo
area_circulo = calcular_area_circulo(5)  # Calcula el área de un círculo con radio 5
print(f"El área del círculo con radio 5 es: {area_circulo}")  # Imprime: El área del círculo con radio 5 es: 78.53981633974483

numero1 = math.pow(2, 3)  # Calcula 2 elevado a la potencia de 3
numero2 = math.cos(math.pi / 4)  # Calcula el coseno de π/4
print(f"2 elevado a la potencia de 3 es: {numero1}")  # Imprime: 2 elevado a la potencia de 3 es: 8.0
print(f"El coseno de π/4 es: {numero2}")  # Imprime: El coseno de π/4 es: 0.7071067811865476
