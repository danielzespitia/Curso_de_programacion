# Atributos de Instancia y de Clase
#
# Atributos de instancia: Son específicos de cada objeto. Se definen dentro de __init__ 
# usando self.atributo = valor.
# Cada instancia tiene su propia copia de estos atributos. En el ejemplo anterior, marca, 
# modelo, y ram_gb son atributos de instancia.
#
# Atributos de clase: Se definen directamente bajo la declaración de la clase, fuera de cualquier método.
# Estos atributos son compartidos por todas las instancias de la clase. Si cambias el valor 
# de un atributo de clase, el cambio se refleja en todos los objetos de esa clase.
# Son útiles para constantes o datos que deben ser consistentes para toda la clase.
#
# Ejemplo Extendido:
# Supongamos que estamos modelando productos en una tienda. Todos los productos tienen un 
# impuesto (IVA) que es el mismo para todos.

class Producto:
    """
    Representa un producto en una tienda.
    Usa un atributo de clase para el IVA.
    """
    # Atributo de clase: compartido por todos los productos.
    # Es una constante para la tienda.
    IVA = 0.16 # 16% de IVA

    def __init__(self, nombre, precio_base):
        # Atributos de instancia: únicos para cada producto.
        self.nombre = nombre
        self.precio_base = precio_base

    def calcular_precio_final(self):
        """
        Calcula el precio final incluyendo el IVA.
        Accede tanto al atributo de instancia 'precio_base' como al de clase 'IVA'.
        """
        return self.precio_base * (1 + self.IVA)

    def mostrar_detalle(self):
        precio_final = self.calcular_precio_final()
        print(f"Producto: {self.nombre}")
        print(f"  - Precio base: ${self.precio_base:,.2f}")
        print(f"  - Precio final (con {self.IVA*100}% IVA): ${precio_final:,.2f}")

# --- Uso de la clase ---
manzanas = Producto("Manzanas (kg)", 1.50)
televisor = Producto("Televisor 55\" 4K", 750.00)

manzanas.mostrar_detalle()
televisor.mostrar_detalle()

print("\n🚨 ¡URGENTE! El gobierno cambia el IVA al 18%.")
# Modificamos el atributo de clase. Este cambio afectará a TODAS las instancias.
Producto.IVA = 0.18

print("\n--- Recalculando precios con el nuevo IVA ---")
manzanas.mostrar_detalle()
televisor.mostrar_detalle()