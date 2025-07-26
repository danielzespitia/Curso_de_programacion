# La herencia es un mecanismo que permite a una nueva clase (llamada clase hija o subclase)
# adquirir los atributos y métodos de una clase existente (llamada clase padre o superclase).
# La clase hija puede usar el código de la clase padre sin reescribirlo, y además puede añadir
# sus propios atributos y métodos o modificar los heredados.
#
# Beneficios:
#
# Reutilización de código (DRY - Don't Repeat Yourself): Define comportamientos comunes en una 
# clase padre
# y rehúsalos en múltiples clases hijas.
#
# Organización lógica: Crea una jerarquía de clases que refleja una relación "es un tipo de".
# Por ejemplo, un Perro es un tipo de Animal.
#
# Ejemplo Extendido:
# Modelaremos una jerarquía de empleados en una empresa.

class Empleado:
    """Clase Padre: define las características comunes a todos los empleados."""
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base

    def calcular_salario_mensual(self):
        """Por defecto, el salario es el base."""
        return self.salario_base

    def mostrar_ficha(self):
        print(f"--- Ficha de Empleado ---")
        print(f"Nombre: {self.nombre} (ID: {self.id_empleado})")
        print(f"Salario Mensual: ${self.calcular_salario_mensual():,.2f}")

# Clase Hija: Gerente hereda de Empleado
class Gerente(Empleado):
    """
    Clase Hija. Un Gerente 'es un tipo de' Empleado, pero con un bono adicional.
    """
    def __init__(self, nombre, id_empleado, salario_base, bono_gestion):
        # 'super()' llama al constructor de la clase padre (Empleado)
        # para inicializar los atributos comunes.
        super().__init__(nombre, id_empleado, salario_base)
        self.bono_gestion = bono_gestion

    # Sobrescritura de método: Modificamos el comportamiento heredado
    def calcular_salario_mensual(self):
        salario_padre = super().calcular_salario_mensual()
        return salario_padre + self.bono_gestion

# Clase Hija: Programador hereda de Empleado
class Programador(Empleado):
    """
    Clase Hija. Un Programador 'es un tipo de' Empleado, pero con pago por horas extra.
    """
    def __init__(self, nombre, id_empleado, salario_base, horas_extra, pago_por_hora):
        super().__init__(nombre, id_empleado, salario_base)
        self.horas_extra = horas_extra
        self.pago_por_hora = pago_por_hora

    # Sobrescritura de método
    def calcular_salario_mensual(self):
        salario_padre = super().calcular_salario_mensual()
        return salario_padre + (self.horas_extra * self.pago_por_hora)

# --- Uso de la jerarquía de clases ---
empleado_base = Empleado("Carlos Ruiz", "E101", 2000)
gerente_ana = Gerente("Ana López", "G202", 3500, 800)
programador_luis = Programador("Luis Torres", "P303", 2800, 20, 25)

empleado_base.mostrar_ficha()
print("\n")
gerente_ana.mostrar_ficha()
print("\n")
programador_luis.mostrar_ficha()