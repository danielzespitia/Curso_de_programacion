# El encapsulamiento es el principio de ocultar los datos internos de un objeto y 
# exponer públicamente solo los métodos necesarios para interactuar con esos datos.
# Es como el panel de un coche: puedes usar el volante y los pedales (la interfaz pública) 
# sin necesidad de saber cómo funciona el motor o la transmisión (los detalles internos).
#
# Beneficios:
#
# Seguridad: Evita que el estado del objeto sea modificado de forma accidental o maliciosa 
# desde fuera.
#
# Integridad: Permite añadir lógica de validación. Por ejemplo, un saldo bancario no debería 
# poder ser negativo.
#
# Mantenimiento: Puedes cambiar la implementación interna de la clase sin que afecte al código 
# que la utiliza, siempre y cuando la interfaz pública no cambie.
#
# En Python, el encapsulamiento se logra por convención:
#
# _atributo: Se considera "protegido". Es una señal para otros programadores de que no deben acceder 
# a él directamente desde fuera de la clase, aunque técnicamente es posible.
#
# __atributo: Se considera "privado". Python realiza un proceso llamado name mangling (cambia el nombre 
# a _NombreDeClase__atributo), lo que hace muy difícil acceder a él desde fuera y previene colisiones de
# nombres en la herencia.
#
# Ejemplo Extendido:
# Una clase Termostato que mantiene una temperatura dentro de un rango válido.

class Termostato:
    """
    Un termostato que encapsula la temperatura para mantenerla
    dentro de un rango seguro (16°C a 30°C).
    """
    _TEMPERATURA_MINIMA = 16
    _TEMPERATURA_MAXIMA = 30

    def __init__(self, temperatura_inicial=21):
        # Usamos doble guion bajo para hacer el atributo 'privado'.
        # Nadie debería poder cambiar la temperatura sin usar los métodos.
        self.__temperatura_actual = self._TEMPERATURA_MINIMA

        # Usamos el método público para establecer la temperatura inicial,
        # así nos aseguramos de que cumpla las reglas.
        self.ajustar_temperatura(temperatura_inicial)

    def get_temperatura(self):
        """
        Método 'getter' para obtener de forma segura la temperatura actual.
        """
        return self.__temperatura_actual

    def ajustar_temperatura(self, nueva_temperatura):
        """
        Método 'setter' público para cambiar la temperatura.
        Contiene la lógica de validación.
        """
        if self._TEMPERATURA_MINIMA <= nueva_temperatura <= self._TEMPERATURA_MAXIMA:
            self.__temperatura_actual = nueva_temperatura
            print(f"Temperatura ajustada a {self.__temperatura_actual}°C.")
        else:
            print(f"⚠️ ¡Error! La temperatura debe estar entre "
                  f"{self._TEMPERATURA_MINIMA}°C y {self._TEMPERATURA_MAXIMA}°C.")

    def mostrar_estado(self):
        print(f"🌡️ Estado actual: {self.get_temperatura()}°C")

# --- Uso del termostato ---
mi_termostato = Termostato()
mi_termostato.mostrar_estado()

print("\n--- Intentando ajustar la temperatura ---")
mi_termostato.ajustar_temperatura(25)
mi_termostato.mostrar_estado()

# Intento de ajuste inválido (demasiado alta)
mi_termostato.ajustar_temperatura(35)
mi_termostato.mostrar_estado() # La temperatura no cambió

# Intento de acceso directo al atributo 'privado'
try:
    print(mi_termostato.__temperatura_actual)
except AttributeError as e:
    print(f"\nNo se puede acceder directamente: {e}")

# Python lo ha renombrado, así es como se vería (¡NO HACER ESTO!)
# print(mi_termostato._Termostato__temperatura_actual)