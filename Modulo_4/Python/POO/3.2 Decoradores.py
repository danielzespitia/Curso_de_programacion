# Decoradores (@property, @staticmethod, @classmethod)
#
# Los decoradores son una forma de modificar o mejorar funciones o métodos. En POO, los más comunes son:
#
# @property: Transforma un método en un "atributo de solo lectura calculado". Permite acceder al resultado del método como si fuera un atributo, sin paréntesis. Es la forma pitónica de crear getters.
#
# @classmethod: Un método que recibe la clase misma como primer argumento (convencionalmente llamado cls) en lugar de la instancia (self). Es útil para métodos que trabajan con la clase, como los métodos de fábrica (factory methods) que crean instancias de la clase de maneras alternativas.
#
# @staticmethod: Un método que no recibe ni la instancia ni la clase como primer argumento. Es esencialmente una función normal que vive dentro del namespace de la clase por razones de organización. No puede modificar el estado del objeto ni de la clase.
#
# Ejemplo Extendido:
# Una clase Persona con edad calculada y un método de fábrica.

from datetime import date

class Persona:
    """
    Representa una persona con atributos calculados y métodos de fábrica.
    """
    def __init__(self, nombre, anio_nacimiento):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento

    @property
    def edad(self):
        """
        Propiedad calculada. Se accede como 'persona.edad', no 'persona.edad()'.
        Calcula la edad dinámicamente cada vez que se accede.
        """
        anio_actual = date.today().year
        return anio_actual - self.anio_nacimiento

    @classmethod
    def desde_edad(cls, nombre, edad):
        """
        Método de fábrica (factory method).
        Crea una instancia de Persona a partir del nombre y la edad,
        en lugar del año de nacimiento. 'cls' se refiere a la clase 'Persona'.
        """
        anio_actual = date.today().year
        anio_nacimiento = anio_actual - edad
        return cls(nombre, anio_nacimiento) # Equivale a Persona(nombre, anio_nacimiento)

    @staticmethod
    def es_mayor_de_edad(edad):
        """
        Método estático. No tiene acceso a 'self' ni 'cls'.
        Es una función de utilidad relacionada con la clase.
        """
        return edad >= 18

    def presentar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        if self.es_mayor_de_edad(self.edad):
            print("Soy mayor de edad.")
        else:
            print("Soy menor de edad.")


# --- Uso de la clase Persona ---

# Creación estándar a través del constructor
p1 = Persona("Elena", 1990)
p1.presentar()

print("\n--- Creación a través del método de fábrica ---")
# Creación alternativa usando el classmethod
p2 = Persona.desde_edad("Juan", 15)
p2.presentar()

print("\n--- Usando el método estático directamente ---")
print(f"¿Alguien de 25 años es mayor de edad? {Persona.es_mayor_de_edad(25)}")