# Explicación: print() muestra datos, input() pide datos al usuario. ¡Importante! input() siempre devuelve los datos como una cadena de texto (str).

# Entrada (input) y Salida (print) en Python        

# Entrada: input() permite al usuario ingresar datos.

nombre = input("¿Cuál es tu nombre? ")  # Pide al usuario que ingrese su nombre
edad = int(input("¿Cuántos años tienes? "))  # Pide al usuario que ingrese su edad  
     
print(f"Hola, {nombre}. Tienes {edad} años.")  # Muestra un mensaje con el nombre y la edad ingresados

altura = float(input("¿Cuál es tu altura en metros? "))  # Pide la altura del usuario
print(f"Tu altura es {altura} metros.")  # Muestra la altura ingresada
