# Los parámetros son las variables que una función espera recibir (como nombre en el ejemplo anterior). Los argumentos son los valores que le 
# pasas cuando la llamas ("Pedro", "Maria"). La palabra clave return permite que una función "devuelva" un resultado.

def sumar(a, b):
    resultado = a + b
    return resultado

# La función devuelve un valor que podemos guardar en una variable
valor_suma = sumar(10, 5)
print(valor_suma) # Imprime: 15

def saludar(nombre):
    mensaje = f"¡Hola, {nombre}!"
    return mensaje

# La función devuelve un mensaje que podemos imprimir
mensaje_saludo = saludar("Ana") 
print(mensaje_saludo)  # Imprime: ¡Hola, Ana!

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area
# La función devuelve el área del rectángulo
area_rectangulo = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {area_rectangulo}")  # Imprime: El área del rectángulo es: 15

