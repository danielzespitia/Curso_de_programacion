#ejercicios de diccionarios
#1. crear un diccionario de estudiante
"""crea un diccionario con los siguientes datos: nombre: ana, edad: 20, carrera: ingenieria"""
"""imprime el valor de carrera"""

mi_diccionario = {
    "nombre": "victor",
    "edad": 23,
    "carrera": "panadero",
}
print("\ncarrera:", mi_diccionario["carrera"])


#2. contar frecuencia de letras
"""dada una palabra (palabra = banana) crea un diccionario que cuente cuantas veces aparece cada letra"""
"""resultado esperado: {b:1 a:3 n:2}"""

palabra = "paralelepipedo"
frecuencia = {}
for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra] += 1
    else:
        frecuencia[letra] = 1
print (frecuencia)


#3. actualizar valores
"""dado el diccionario precios = {"manzana": 0.5, "banana": 0.3} cambia el precio de la manzana a 0.4"""

precios = {"manzana": 0.5, "banana": 0.3}
precios["manzana"] = 0.4
print("\nprecios despues de modificar el precio", precios)


#4 iterar sobre claves y valores
"""dado el diccionario = {"francia": "paris", "italia": "roma", "españa": "madrid"}"""
"""imprime cada pais y su capital en formato: "la capital de [pais] es [capital]"""

capitales = {"francia": "paris", "italia": "roma", "españa": "madrid"}
for pais, capital in capitales.items():
    print(f"la capital de {pais} es {capital}")