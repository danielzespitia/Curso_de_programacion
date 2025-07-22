# ====================================================================
# 🐍 Guía Interactiva de Condicionales en Python para Principiantes 🧠
# ====================================================================

# ¡Hola! En programación, no siempre queremos que nuestro código haga lo mismo.
# A veces, necesitamos que tome decisiones y actúe de manera diferente 
# según la situación. Para eso, usamos las **condicionales**.

# Imagina que eres un portero de una discoteca. Tu regla es: 
# "Si la persona tiene 18 años o más, puede entrar. Si no, no puede". 
# ¡Eso es una condicional!

# En Python, las condicionales principales son `if`, `elif` y `else`.
# Ejecuta este archivo para ver los ejemplos en acción.

print("--- Inicio de la Guía Interactiva de Condicionales ---")

# ====================================================================
# 1. La Condicional `if` (Si...)
# ====================================================================
# La usamos para ejecutar un bloque de código **solo si** una condición es verdadera.
#
# Sintaxis:
# if condicion:
#     # Este código se ejecuta si la condición es Verdadera

# --- Ejemplo de `if` ---
# Vamos a comprobar si un alumno ha aprobado. La nota para aprobar es 5.
print("\n\n--- Ejemplo 1: La condicional 'if' ---")

nota_alumno = 7

print(f"La nota del alumno es: {nota_alumno}")
print("Revisando la nota...")

if nota_alumno >= 5:
    # Esta línea solo se ejecutará si la nota es 5 o más
    print("¡Felicidades! Has aprobado.")

print("Fin de la revisión.")


# ====================================================================
# 2. La Condicional `if-else` (Si... Si no...)
# ====================================================================
# La usamos cuando queremos hacer una cosa si la condición es verdadera, 
# y **otra cosa diferente** si es falsa.
#
# Sintaxis:
# if condicion:
#     # Se ejecuta si la condición es Verdadera
# else:
#     # Se ejecuta si la condición es Falsa

# --- Ejemplo de `if-else` ---
# Comprobar si un número es positivo o no.
print("\n\n--- Ejemplo 2: La condicional 'if-else' ---")

numero = -10
print(f"El número a comprobar es: {numero}")

if numero > 0:
    print("El número es positivo.")
else:
    print("El número NO es positivo (es cero o negativo).")


# ====================================================================
# 3. La Condicional `if-elif-else` (Si... Si no, si... Si no...)
# ====================================================================
# ¿Y si tenemos más de dos posibilidades? Usamos `elif` 
# (una contracción de "else if") para añadir más condiciones.
#
# Sintaxis:
# if condicion1:
#     # Se ejecuta si la condicion1 es Verdadera
# elif condicion2:
#     # Se ejecuta si la condicion1 es Falsa, PERO la condicion2 es Verdadera
# else:
#     # Se ejecuta si NINGUNA de las anteriores es Verdadera

# --- Ejemplo de `if-elif-else` ---
# Dar una calificación basada en la nota.
print("\n\n--- Ejemplo 3: La condicional 'if-elif-else' ---")

nota_final = 8
print(f"La nota final del alumno es: {nota_final}")

if nota_final == 10:
    print("¡Matrícula de Honor! ¡Excelente trabajo!")
elif nota_final >= 7:
    print("¡Notable! Muy bien hecho.")
elif nota_final >= 5:
    print("Aprobado. ¡Buen esfuerzo!")
else:
    print("Reprobado. Necesitas estudiar un poco más.")


# ====================================================================
# 4. Combinando Condiciones con `and` y `or`
# ====================================================================
# A veces, una decisión depende de varias cosas a la vez.
#
# `and` (y): Ambas condiciones deben ser verdaderas.
# `or` (o): Al menos una de las condiciones debe ser verdadera.

# --- Ejemplo con `and` ---
# Para entrar a una atracción, debes ser mayor de 12 años Y medir más de 1.50 metros.
print("\n\n--- Ejemplo 4: Combinando condiciones con 'and' ---")

edad_and = 15
altura_and = 1.60
print(f"Requisitos: Edad > 12 y Altura > 1.50. Tu edad: {edad_and}, tu altura: {altura_and}")

if edad_and > 12 and altura_and > 1.50:
    print("¡Puedes pasar a la atracción!")
else:
    print("Lo siento, no cumples con los requisitos.")


# --- Ejemplo con `or` ---
# Tienes descuento si eres estudiante O si eres mayor de 65 años.
print("\n\n--- Ejemplo 5: Combinando condiciones con 'or' ---")

es_estudiante_or = False
edad_or = 70
print(f"Requisitos: Ser estudiante o Edad > 65. Eres estudiante: {es_estudiante_or}, tu edad: {edad_or}")

if es_estudiante_or or edad_or > 65:
    print("¡Tienes un descuento especial!")
else:
    print("Precio regular.")


# ====================================================================
# 💡 Tabla de Operadores de Comparación
# ====================================================================
# Para crear nuestras condiciones, usamos estos operadores:
#
# | Operador | Significado                  | Ejemplo      | Resultado |
# | :------: | ---------------------------- | ------------ | --------- |
# |   ==     | Igual a                      | 5 == 5       | True      |
# |   !=     | No igual a (diferente de)    | 5 != 6       | True      |
# |    <     | Menor que                    | 5 < 10       | True      |
# |    >     | Mayor que                    | 10 > 5       | True      |
# |   <=     | Menor o igual que            | 5 <= 5       | True      |
# |   >=     | Mayor o igual que            | 10 >= 10     | True      |
#
# ====================================================================
print("\n\n--- Fin de la Guía ---")
print("¡La práctica es la clave! Modifica las variables y vuelve a ejecutar el código.")