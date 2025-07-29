print("\n--- ejercicio 2: calculadora promedio")
ingresar_numeros = [10,15,30,20]
print(f"contar los numeros hasta: {ingresar_numeros[0]}")
contador = input("cual es el numero 10?")
print()
contador = input ("cual es el numero 15?")
print()
contador = input("cual es el numero 30?")
print()
contador = input("cual es el numero 20?")
print()
contador = 1
while contador < 5:
    print(f"contador: {contador}")
    contador += 1
numeros = [10,15,30,20]
suma = sum(numeros)
print("suma:", suma)
promedio = sum(numeros) / len(numeros)
print ("promedio",promedio)
contador = input("fin del conteo")




