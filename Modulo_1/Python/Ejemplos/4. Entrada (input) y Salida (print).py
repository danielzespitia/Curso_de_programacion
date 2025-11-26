# Explicación: print() muestra datos, input() pide datos al usuario. ¡Importante! input() siempre devuelve los datos como una cadena de texto (str).

# Entrada (input) y Salida (print) en Python        

# Entrada: input() permite al usuario ingresar datos.

nombre = input("¿Cuál es tu nombre? ")  # Pide al usuario que ingrese su nombre
edad = input("¿Cuántos años tienes? ")  # Pide al usuario que ingrese su edad       

# Salida: print() muestra datos en la consola.

print(f"Hola, {nombre}! Tienes {edad} años.")  # Muestra un saludo personalizado
print("¡Bienvenido al mundo de Python!")  # Mensaje de bienvenida

# Nota: input() siempre devuelve los datos como una cadena de texto (str).

# Si necesitas un número, debes convertirlo usando int() o float().

# Ejemplo de conversión de tipo:

edad_num = int(edad)
print(f"Hola {nombre}, el año que viene tendrás {edad_num + 1} años.")

# Aquí convertimos la edad a un número entero para hacer cálculos.
# Si el usuario ingresa un número decimal, usa float() en su lugar:
# edad_num = float(edad)

altura = float(input("¿Cuál es tu altura en metros? "))  # Pide la altura del usuario
print(f"Tu altura es {altura} metros.")  # Muestra la altura ingresada
