# Métodos Especiales (Dunder Methods)
#
# Los métodos especiales, llamados "dunder" por el doble guion bajo (double underscore), permiten que tus objetos se integren
# con el comportamiento nativo de Python. Hacen que tus clases se sientan más "pitónicas". Por ejemplo, al definir __add__,
# puedes sumar dos objetos de tu clase usando el operador +.
#
# __str__(self): Define la representación "amigable" del objeto como cadena de texto. Se usa con print() y str().
#
# __repr__(self): Define la representación "oficial" o de depuración del objeto. Debería ser, idealmente, una cadena que pueda recrear el objeto.
#
# __len__(self): Permite usar len() en una instancia de la clase.
#
# __add__(self, other): Define el comportamiento para el operador +.
#
# __eq__(self, other): Define el comportamiento para el operador de igualdad ==.
#
# Ejemplo Extendido:
# Crearemos una clase Vector2D para operaciones matemáticas básicas.

import math

class Vector2D:
    """
    Representa un vector en un espacio 2D.
    Implementa varios métodos dunder para una integración natural con Python.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representación para desarrolladores (inequívoca)
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # Representación para usuarios (legible)
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Igualdad: v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Suma: v1 + v2
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented # Indica que la operación no está soportada

    # Magnitud: abs(v1)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

# --- Uso de la clase Vector2D ---
v1 = Vector2D(2, 3)
v2 = Vector2D(5, 1)
v3 = Vector2D(2, 3)

print(f"Representación oficial (repr): {repr(v1)}")
print(f"Representación amigable (str): {v1}") # print llama a __str__

# Usando el operador de igualdad (llama a __eq__)
print(f"¿v1 es igual a v2? {v1 == v2}") # False
print(f"¿v1 es igual a v3? {v1 == v3}") # True

# Usando el operador de suma (llama a __add__)
v_suma = v1 + v2
print(f"La suma de {v1} y {v2} es {v_suma}")

# Usando la función abs() (llama a __abs__)
print(f"La magnitud (longitud) de {v1} es {abs(v1):.2f}")