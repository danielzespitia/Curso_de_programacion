# Aritméticos: Para hacer matemáticas.

suma = 10 + 5       # 15
resta = 10 - 5      # 5
multiplicacion = 10 * 5  # 50
division = 10 / 3   # 3.333...
division_entera = 10 // 3 # 3 (descarta el residuo)
modulo = 10 % 3     # 1 (el residuo de la división)
potencia = 2 ** 3   # 8 (2 elevado a la 3)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}, División entera: {division_entera}, Módulo: {modulo}, Potencia: {potencia}")

# Comparación = Relacionales: Para comparar valores.

igual = (10 == 10)        # True (son iguales)
diferente = (10 != 5)     # True (son diferentes)   
mayor_que = (10 > 5)       # True (10 es mayor que 5)
menor_que = (10 < 5)       # False (10 no es menor que 5)
mayor_igual = (10 >= 10)   # True (10 es mayor o igual a 10)
menor_igual = (10 <= 5)    # False (10 no es menor   o igual a 5)
print(f"Igual: {igual}, Diferente: {diferente}, Mayor que: {mayor_que}, Menor que: {menor_que}, Mayor o igual: {mayor_igual}, Menor o igual: {menor_igual}")    

# Lógicos: Para combinar condiciones.

and_condition = (10 > 5 and 5 < 10)  # True (ambas son verdaderas)                  
or_condition = (10 > 5 or 5 > 10)   # True (al menos una es verdadera)
not_condition = not (10 > 5)         # False (niega la condición)   
print(f"And: {and_condition}, Or: {or_condition}, Not: {not_condition}")    

# Asignación: Para asignar valores a variables.

x = 10      
y = 5
x += 5  # x = x + 5, ahora x es 15
y -= 2  # y = y - 2, ahora y es 3
print(f"x: {x}, y: {y}")

# Identidad: Para comparar si dos variables son el mismo objeto en memoria.

a = [1, 2, 3]       
b = a  # b es una referencia al mismo objeto que a
c = a.copy()  # c es una copia de a, no el mismo objeto
print(f"a is b: {a is b}, a is c: {a is c}, a == c: {a == c}")  # True, False, True
