
while True:
    try:
        n = int(input("Ingrese un número entero positivo N: "))
        if n > 0:
            break
        else:
            print("El número debe ser positivo. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")

suma_pares = 0

# Usando for con range y condicional if
for i in range(n + 1): # Incluye N si es par
    if i % 2 == 0:
        suma_pares += i

print(f"La suma de los números pares entre 0 y {n} es: {suma_pares}")
