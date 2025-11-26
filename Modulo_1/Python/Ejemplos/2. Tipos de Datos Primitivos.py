# int (Entero): Números enteros sin decimales. Ej: 10, -3, 0.

edad = 25
print(edad) # Imprime: 25

# float (Flotante): Números con decimales. Ej: 9.81, -3.14.

altura = 1.75
print(altura) # Imprime: 1.75

# bool (Booleano): Verdadero o falso. Ej: True, False.
es_estudiante = True
print(es_estudiante) # Imprime: True

# str (Cadena de texto): Texto encerrado en comillas simples ' ' o dobles " ".

nombre = "Ana"
print(nombre) # Imprime: Ana

# Ejemplo de métodos y f-strings:
# Métodos de cadenas de texto (strings) y f-strings

saludo = "hola mundo"
print(saludo.upper()) # Imprime: HOLA MUNDO
print(saludo.capitalize()) # Imprime: Hola mundo
print(saludo.replace("mundo", "Python")) # Imprime: hola Python
print(saludo.lower())  # Imprime: hola mundo

nombre = "Carlos"
edad = 30
# f-string: una forma moderna y fácil de incluir variables en un texto
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
print(mensaje) # Imprime: Hola, me llamo Carlos y tengo 30 años.