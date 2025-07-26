# Polimorfismo
#
# La palabra polimorfismo significa "muchas formas". En POO, se refiere a la capacidad 
# de objetos de diferentes clases
# de responder a la misma llamada de método de manera específica para su clase. En el ejemplo 
# anterior, tanto Gerente
# como Programador tienen un método calcular_salario_mensual(), pero cada uno lo ejecuta de forma diferente.
#
# El polimorfismo permite escribir código más genérico y desacoplado. Puedes tener una función que 
# trabaje con objetos
# de la clase padre, y funcionará correctamente con cualquier objeto de sus clases hijas sin necesidad 
# de saber de qué tipo específico son.
#
# Ejemplo Extendido:
# Usando las clases del ejemplo anterior, podemos crear una función que procese la nómina de todos 
# los empleados, sin importar su cargo.

# (Continuación del código de Empleado, Gerente, Programador)

# Lista de empleados de diferentes tipos (diferentes formas)
lista_empleados = [
    Empleado("Carlos Ruiz", "E101", 2000),
    Gerente("Ana López", "G202", 3500, 800),
    Programador("Luis Torres", "P303", 2800, 20, 25),
    Programador("Maria Sol", "P304", 2800, 10, 25)
]

def procesar_nomina_anual(empleados):
    """
    Esta función demuestra el polimorfismo.
    Itera sobre una lista de empleados y llama al mismo método 'calcular_salario_mensual'
    en cada uno. Python elige automáticamente la versión correcta del método
    según la clase del objeto.
    """
    costo_total_anual = 0
    print("--- PROCESANDO NÓMINA ANUAL ---")
    for emp in empleados:
        salario_mensual = emp.calcular_salario_mensual()
        salario_anual = salario_mensual * 12
        costo_total_anual += salario_anual
        print(f"Empleado: {emp.nombre}, Salario Anual: ${salario_anual:,.2f}")
    print("-" * 30)
    print(f"COSTO TOTAL ANUAL DE LA NÓMINA: ${costo_total_anual:,.2f}")


# Llamamos a la función con nuestra lista heterogénea
procesar_nomina_anual(lista_empleados)