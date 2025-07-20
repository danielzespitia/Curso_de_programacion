# La abstracción consiste en ocultar la complejidad y mostrar solo las características esenciales.
# En POO, esto se logra a menudo con Clases Base Abstractas (ABC - Abstract Base Classes).
#
# Una ABC es una clase que no puede ser instanciada directamente. Su propósito es servir como una plantilla o un contrato para sus clases hijas.
# Define métodos que las subclases deben implementar. Si una subclase no implementa todos los métodos abstractos definidos en la clase padre, no se podrá crear un objeto de esa subclase.
#
# Ejemplo Extendido:
# Imaginemos un sistema para procesar diferentes tipos de archivos multimedia. Todos los archivos se pueden "procesar", pero la forma de hacerlo es diferente para cada tipo.

from abc import ABC, abstractmethod

# Clase Base Abstracta que define el contrato
class ArchivoProcesable(ABC):
    """
    Define un 'contrato': cualquier clase que herede de esta
    DEBE implementar los métodos 'cargar_datos' y 'procesar'.
    """
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo
        self.datos_cargados = False

    @abstractmethod
    def cargar_datos(self):
        """Método abstracto para cargar el contenido del archivo."""
        pass

    @abstractmethod
    def procesar(self):
        """Método abstracto para realizar la acción principal sobre los datos."""
        pass

    def ejecutar_flujo(self):
        """
        Este es un método concreto que define un flujo de trabajo común.
        Utiliza los métodos abstractos que serán implementados por las hijas.
        """
        print(f"\nIniciando procesamiento para {self.ruta}...")
        self.cargar_datos()
        if self.datos_cargados:
            self.procesar()
        print("Procesamiento finalizado.")


# Implementación concreta para archivos de texto
class ArchivoTexto(ArchivoProcesable):
    def cargar_datos(self):
        print(f"Leyendo contenido del archivo de texto: {self.ruta}")
        self._contenido = "Este es el texto del archivo." # Simulación
        self.datos_cargados = True

    def procesar(self):
        num_palabras = len(self._contenido.split())
        print(f"-> Proceso: Contando palabras. Total: {num_palabras} palabras.")


# Implementación concreta para archivos de imagen
class ArchivoImagen(ArchivoProcesable):
    def cargar_datos(self):
        print(f"Cargando píxeles de la imagen: {self.ruta}")
        self._dimensiones = (1920, 1080) # Simulación
        self.datos_cargados = True

    def procesar(self):
        print(f"-> Proceso: Aplicando filtro de blanco y negro a imagen de {self._dimensiones[0]}x{self._dimensiones[1]}.")


# --- Uso del sistema ---

# No se puede instanciar la clase abstracta directamente
# procesador_fallido = ArchivoProcesable("ruta.txt") # Esto daría un TypeError

procesador_texto = ArchivoTexto("documento.txt")
procesador_imagen = ArchivoImagen("paisaje.jpg")

procesador_texto.ejecutar_flujo()
procesador_imagen.ejecutar_flujo()