# Clase: Es la plantilla, el plano o el molde a partir del cual se crean los objetos.

# Define un conjunto de atributos y métodos que tendrán todos los objetos de ese tipo.
# Por ejemplo, la clase Humano define que todos los humanos tienen un nombre, una edad y pueden comer.

# Objeto (o Instancia): Es la materialización de una clase.

# Si Humano es la clase, entonces un objeto específico como juan_perez (con nombre "Juan Pérez", 
# edad 30) es una instancia de esa clase.
# Cada objeto tiene su propia copia de los atributos definidos en la clase, pero comparte los mismos 
# métodos.

# Ejemplo Extendido:

# Imaginemos una clase Portatil para un inventario.

# Definimos la clase (el molde) que representa un ordenador portátil.
class Portatil:
    """
    Esta clase representa un ordenador portátil con sus características
    y acciones básicas.
    """
    # Atributos iniciales (estado por defecto si no se especifica)
    marca = "Genérica"
    sistema_operativo = "Linux"
    bateria_cargada = False

    # Métodos (comportamientos)
    def encender(self):
        """
        Enciende el portátil si la batería está cargada y muestra un mensaje.
        """
        if self.bateria_cargada:
            print(f"✅ ¡Bienvenido! El {self.marca} con {self.sistema_operativo} se ha encendido.")
        else:
            print(f"❌ Batería baja. Por favor, conecta el cargador.")

    def cargar_bateria(self):
        """
        Simula la carga de la batería y actualiza su estado.
        """
        self.bateria_cargada = True
        print("🔋 Batería cargada al 100%.")

# --- Uso de la clase ---

# Creamos un primer objeto (instancia) de la clase Portatil
portatil_dev = Portatil()
portatil_dev.marca = "Dell"
portatil_dev.sistema_operativo = "Ubuntu 24.04"

# Creamos un segundo objeto, completamente independiente del primero
portatil_diseno = Portatil()
portatil_diseno.marca = "Apple"
portatil_diseno.sistema_operativo = "macOS Sonoma"
portatil_diseno.bateria_cargada = True  # Este portátil ya tiene la batería cargada

# Interactuamos con el primer portátil
print(f"\nIntentando encender el portátil del desarrollador ({portatil_dev.marca})...")
portatil_dev.encender() # Fallará porque la batería no está cargada
portatil_dev.cargar_bateria()
portatil_dev.encender() # Ahora funcionará

print("-" * 20)

# Interactuamos con el segundo portátil
print(f"Intentando encender el portátil del diseñador ({portatil_diseno.marca})...")
portatil_diseno.encender() 



"""
Ejemplo 2
"""


# Definimos la clase (el molde)
class Coche:
    # Atributos (características)
    marca = "Toyota"
    modelo = "Corolla"
    año = 2023

    # Métodos (comportamientos)
    def arrancar(self):
        print(f"🚘 El {self.marca} {self.modelo} ha arrancado.")

# Creamos un objeto (una instancia de la clase)
mi_coche = Coche()

# Accedemos a sus atributos y métodos
print(f"\nMarca: {mi_coche.marca}")
mi_coche.arrancar()