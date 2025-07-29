# Permiten ejecutar un bloque de código solo si se cumple una condición. if es el primero, elif (else if) 
# permite añadir más condiciones, y else se ejecuta si ninguna de las anteriores es verdadera.

edad = 18
if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("¡Justo tienes 18 años!")
else:
    print("Eres mayor de edad.")
    
# Explicación:
# - if evalúa si la condición es verdadera. Si lo es, ejecuta el bloque de código indentado debajo.
# - elif permite añadir más condiciones. Si la primera condición no se cumple, evalúa la     siguiente.
# - else se ejecuta si ninguna de las condiciones anteriores es verdadera.  
# - Las condiciones pueden ser comparaciones (edad < 18) o cualquier expresión que devuelva True o False.
# - Puedes tener múltiples elif y un solo else al final.
# - Es importante mantener la indentación correcta para que Python entienda qué código pertenece a cada bloque.
# - Puedes usar operadores lógicos (and, or, not) para combinar condiciones más complejas.
# - También puedes usar operadores de comparación (==, !=, >, <, >=, <=) para comparar valores.
# - Recuerda que las condiciones se evalúan en orden, y solo se ejecuta el bloque del primer if o elif que sea verdadero.
# - Si necesitas ejecutar un bloque de código sin condiciones, puedes usar un bloque if sin elif o else.

# Condificonales Combnados

# Operador and (y)
# Permite combinar condiciones, y solo se cumple si ambas son verdaderas.
# Ejemplo: Acceso a un área restringida solo si el usuario es mayor de edad
# y es un administrador.
# Si ambas condiciones son verdaderas, se concede el acceso.

edad = 25
es_administrador = True

if edad >= 18 and es_administrador:
    print("Acceso concedido. Bienvenido, administrador.")
else:
    print("Acceso denegado.")
    
# Operador or (o)
# Permite combinar condiciones, y se cumple si al menos una es verdadera.   
# Ejemplo: Acceso a un área restringida si el usuario es mayor de edad
# o es un administrador.

edad = 16
es_administrador = False    
if edad >= 18 or es_administrador:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
    
# Operador not (no)
# Invierte el resultado de una condición.   
# Ejemplo: Acceso a un área restringida si el usuario no es un administrador.

es_administrador = False
if not es_administrador:
    print("Acceso denegado. Solo administradores pueden acceder.")
else:
    print("Acceso concedido. Bienvenido, administrador.")
    
# Operadores de comparación
# Permiten comparar valores y devolver True o False.
# Ejemplo: Comprobar si un número es mayor que otro.
numero1 = 10
numero2 = 5
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}.")
else:
    print(f"{numero1} no es mayor que {numero2}.")
    
# Operadores de comparación comunes:
# == (igual a), != (diferente de), > (mayor que), < (menor que),
# >= (mayor o igual que), <= (menor o igual que).  
 
# Ejemplo de operadores de comparación

numero1 = 10
numero2 = 5
if numero1 == numero2:
    print(f"{numero1} es igual a {numero2}.")
elif numero1 != numero2:
    print(f"{numero1} es diferente de {numero2}.")  
elif numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}.")
elif numero1 < numero2: 
    print(f"{numero1} es menor que {numero2}.") 
# elif numero1 >= numero2:
#     print(f"{numero1} es mayor o igual que {numero2}.")
# elif numero1 <= numero2:
#     print(f"{numero1} es menor o igual que {numero2}.")
# Nota: Puedes usar elif para añadir más condiciones, pero recuerda que solo se ejecutará el bloque del primer if o elif que sea verdadero.
else:
    print("Ninguna de las condiciones anteriores se cumplió.")
    
# Ejemplo de uso de operadores lógicos
numero1 = 10    
numero2 = 5
numero3 = 15
if (numero1 > numero2 and numero1 < numero3) or (numero2 < numero3):
    print(f"{numero1} es mayor que {numero2} y menor que {numero3}, o {numero2} es menor que {numero3}.")
    # Nota: Los operadores lógicos permiten combinar condiciones de manera flexible.
else:
    print("Ninguna de las condiciones se cumplió.")

nota = int(input("cual es la nota?"))
if nota >=10:
    print ("aprobado")
else: 
    print ("desaprovado")


temperatura = int(input("que temperatura hace hoy?"))
if temperatura <10:
    print ("ponte abrigo, hace frio")

elif temperatura >=10 and temperatura <=20:
    print (" una chaqueta ligera esta bien")

else:
    print ("hace calor, usa ropa fresca")


