# Este es el concepto más abstracto de la POO en Python.
# Si una clase es un molde para crear objetos, una metaclase es un molde para crear clases.
# Las metaclases te permiten interceptar la creación de una clase (class MiClase: ...) y modificarla antes de que sea creada.
#
# Por defecto, la metaclase de todas las clases en Python es type.
# Cuando escribes class Foo: ..., Python internamente está llamando a type('Foo', (), {}).
# Al definir tu propia metaclase, puedes controlar cómo se construyen las clases.
#
# Usos:
#
# Validar o transformar automáticamente los atributos de una clase.
#
# Registrar automáticamente las clases creadas en un registro central (muy útil para frameworks de plugins o ORMs).
#
# Inyectar nuevos métodos en una clase de forma programática.
#
# Ejemplo Extendido (Metaclase que registra clases):
# Imaginemos que estamos creando un framework donde diferentes "plugins" pueden manejar diferentes tipos de datos.
# Queremos que cada clase de plugin se registre automáticamente al ser definida.

# El registro donde guardaremos las clases de plugins
PLUGIN_REGISTRY = {}

class PluginMeta(type):
    """
    Esta metaclase interceptará la creación de cualquier clase que la use.
    """
    def __new__(cls, name, bases, dct):
        # 'cls' es la metaclase misma (PluginMeta)
        # 'name' es el nombre de la clase que se está creando (ej. "ImagePlugin")
        # 'bases' es la tupla de clases padre
        # 'dct' es el diccionario con los atributos y métodos de la clase

        # Creamos la clase llamando al __new__ de la metaclase padre (type)
        new_class = super().__new__(cls, name, bases, dct)

        # No registraremos la clase base del plugin, solo sus hijas
        if name != "BasePlugin":
            # Usamos un atributo de la clase para obtener su clave de registro
            plugin_id = dct.get('plugin_id')
            if plugin_id:
                print(f"*** Metaclase: Registrando plugin '{name}' con ID '{plugin_id}' ***")
                PLUGIN_REGISTRY[plugin_id] = new_class
            else:
                print(f"*** Metaclase: ADVERTENCIA - La clase '{name}' no tiene 'plugin_id' y no será registrada. ***")

        return new_class

# Clase base que usa nuestra metaclase. Todas sus hijas también la usarán.
class BasePlugin(metaclass=PluginMeta):
    def ejecutar(self, datos):
        raise NotImplementedError

# --- Definición de Plugins ---
# Al definir estas clases, la metaclase se ejecuta automáticamente.

class ImagePlugin(BasePlugin):
    plugin_id = "image"
    def ejecutar(self, datos):
        print(f"Procesando datos de imagen: {datos}")

class AudioPlugin(BasePlugin):
    plugin_id = "audio"
    def ejecutar(self, datos):
        print(f"Procesando datos de audio: {datos}")

class VideoPlugin(BasePlugin):
    # Este no se registrará porque no tiene plugin_id
    def ejecutar(self, datos):
        print("Procesando video")


# --- Uso del registro de plugins ---
print("\n--- Registro de Plugins Creado ---")
print(PLUGIN_REGISTRY)

def procesar_archivo(tipo_archivo, datos):
    if tipo_archivo in PLUGIN_REGISTRY:
        # Obtenemos la CLASE del registro
        PluginClase = PLUGIN_REGISTRY[tipo_archivo]
        # Creamos una INSTANCIA y la usamos
        plugin_instancia = PluginClase()
        plugin_instancia.ejecutar(datos)
    else:
        print(f"No hay un plugin registrado para el tipo '{tipo_archivo}'")

print("\n--- Ejecutando plugins desde el registro ---")
procesar_archivo("image", "gato.jpg")
procesar_archivo("audio", "cancion.mp3")
procesar_archivo("video", "pelicula.mp4") # No se encuentra