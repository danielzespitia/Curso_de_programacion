def calcular_area_rectangulo(largo, ancho):
  return largo * ancho

longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

area = calcular_area_rectangulo(longitud, ancho)

print(f"El área del rectángulo es: {area}")