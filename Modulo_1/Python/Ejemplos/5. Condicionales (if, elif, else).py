edad = int(input("\n¿Cuántos años tienes? "))

# Las condiciones necesitan un dato booleano (True o False) para decidir 
# qué bloque de código ejecutar. En este caso, se evalúa la edad ingresada 
# por el usuario para determinar si es menor de edad, adulto o adulto mayor.

if edad < 18:
    print("Eres menor de edad.")
elif edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")
    
    
    
    
    
# Ejemplo 2

entrada = True

# Se utiliza una variable booleana para controlar el acceso a un evento. 
# Si la variable 'entrada' es True, se permite la entrada; de lo contrario, se deniega el acceso.

if entrada:
    print("¡Bienvenido al evento!") 
else:
    print("Lo siento, no puedes entrar al evento.")
   
   
   
   
    
# Ejemplo 3

if True:
    print("Esta condición siempre es verdadera.")
else:   
    print("Esta condición nunca se ejecutará.")
  
  
  
    
# Ejemplo 4

dia = "lunes"

# Podemos verificar un string para saber si se ejecutara

if dia == "lunes":
    print("Hoy es lunes, comienza la semana.")
elif dia == "viernes":
    print("Hoy es viernes, el fin de semana está cerca.")
else:
    print("Hoy es un día entre semana.")
    
    
    
    
# Ejemplo 5

edad_persona = int(input("\nIngresa tu edad: "))

# Utilizamos los operadores logicos para añadir mas condiciones a cumplir

if edad_persona <= 18 and edad_persona <= 65:
    print("Acabas de cumplir 18 años, eres mayor de edad.")
elif edad_persona > 65 and edad_persona <= 100:
    print("Eres adulto mayor.")
elif edad_persona > 100 and edad_persona <= 120:
    print("¡Wow! Eres una persona centenaria.")
elif edad_persona < 0:
    print("La edad no puede ser negativa.")
elif edad_persona == 0:
    print("¡Felicidades por tu nacimiento!")
else:
    print("Edad no válida.")
    
    
    
# Ejemplo 6

animal_favorito = input("\n¿Cuál es tu animal favorito? ")

# En este ejemplo, se utiliza una estructura condicional para verificar el animal favorito del usuario.
# Se consideran diferentes formas de escribir el nombre del animal (mayúsculas y sinónimos) para mostrar
# un mensaje personalizado. Si el usuario ingresa un animal diferente, se muestra un mensaje de interés 
# por su elección.

if (animal_favorito == "perro" or animal_favorito == "PERRO") or (animal_favorito == "canino" or animal_favorito == "CANINO"):
    print("¡Los perros son geniales!")
elif (animal_favorito == "gato" or animal_favorito == "GATO") or animal_favorito == "felino":
    print("¡Los gatos son adorables!")

# En este ejemplo, se utilizan operadores lógicos para verificar si el animal favorito del usuario es 
# un perro, gato o pájaro, considerando diferentes formas de escribirlo (mayúsculas y sinónimos). Si 
# el usuario ingresa un animal diferente, se muestra un mensaje de interés por su elección.

elif (animal_favorito == "pájaro" or animal_favorito == "PÁJARO") or animal_favorito == "ave":
    print("¡Los pájaros son fascinantes!")
else:
    print("¡Interesante elección de animal favorito!")
    
    
    
    
# Ejemplo 7

herramienta = input("\n¿cuál es tu herramienta de programación favorita? ").lower()

# En este ejemplo, se utiliza el método .lower() para convertir la entrada del usuario a minúsculas,
# lo que permite comparar la respuesta sin importar si el usuario ingresa mayúsculas o minúsculas. 

if herramienta == "python":
    print("¡Python es una excelente herramienta de programación!")
elif herramienta == "java":
    print("¡Java es una herramienta de programación muy popular!")
elif herramienta == "javascript":
    print("¡JavaScript es esencial para el desarrollo web!")
else:
    print("¡Interesante elección de herramienta de programación!")
    
   
   
    
# Ejemplo 8

lenguaje = input("\n¿cuál es tu lenguaje de programación favorito? ")

# En este ejemplo, se utiliza el método .lower() para convertir la entrada del usuario a minúsculas,
# lo que permite comparar la respuesta sin importar si el usuario ingresa mayúsculas o minúsculas. 
# Se verifica si el lenguaje de programación favorito del usuario es Python o Java, y se muestra un 
# mensaje personalizado para cada caso. Si el usuario ingresa un lenguaje diferente, se muestra un 
# mensaje de interés por su elección.

if lenguaje == "python".lower:
    print("¡Python es un lenguaje de programación versátil y fácil de aprender!")
elif lenguaje == "java".lower:
    print("¡Java es un lenguaje de programación robusto y ampliamente utilizado!")
else:
    print("¡Interesante elección de lenguaje de programación!")