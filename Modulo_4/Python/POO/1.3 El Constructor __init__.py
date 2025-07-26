# El Constructor __init__
#
# Crear objetos y asignarles atributos uno por uno (como en el ejemplo anterior) 
# es tedioso y propenso a errores.
# El método constructor __init__ resuelve esto. Es un método especial que Python ejecuta 
# automáticamente cada vez que se crea una nueva instancia de una clase.
# Su propósito principal es inicializar los atributos del objeto con los valores que se le 
# pasan como argumentos en el momento de la creación.
#
# Ejemplo Extendido:
# Mejoraremos nuestro Portatil con un constructor para una inicialización más limpia.

class Portatil:
    """
    Clase mejorada con un constructor para inicializar los atributos
    de cada portátil de forma única al momento de su creación.
    """
    # El primer argumento 'self' siempre hace referencia a la instancia que se está creando.
    def __init__(self, marca, modelo, ram_gb, sistema_operativo="Linux"):
        """
        Constructor que se ejecuta al crear un nuevo objeto Portatil.
        """
        print(f"Creando nuevo portátil: {marca} {modelo}...")
        # Atributos de instancia (cada objeto tendrá los suyos)
        self.marca = marca
        self.modelo = modelo
        self.ram_gb = ram_gb
        self.sistema_operativo = sistema_operativo
        self.encendido = False # Por defecto, el portátil está apagado

    def estado(self):
        """Muestra el estado actual del portátil."""
        estado_str = "encendido" if self.encendido else "apagado"
        print(f"💻 {self.marca} {self.modelo} ({self.ram_gb}GB RAM) está {estado_str}.")

    def alternar_energia(self):
        """Cambia el estado de encendido a apagado y viceversa."""
        self.encendido = not self.encendido
        self.estado()

# --- Uso de la clase con __init__ ---

# Ahora creamos las instancias pasando los argumentos directamente.
# El sistema operativo es opcional; si no se pasa, usará "Linux".
portatil_ana = Portatil("HP", "Spectre x360", 16, "Windows 11")
portatil_carlos = Portatil("Lenovo", "ThinkPad T14", 32) # Usará el SO por defecto

portatil_ana.estado()
portatil_carlos.estado()

print("\n--- Operando los portátiles ---")
portatil_ana.alternar_energia() # Lo enciende
portatil_ana.alternar_energia() # Lo apaga

portatil_carlos.alternar_energia() # Lo enciende
