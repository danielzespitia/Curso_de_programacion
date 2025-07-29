print("Calculadora de promedio")

numeros = []

while True:
        entrada = input("Ingresa un número o 'fin': ").strip() # Usar .strip() es buena práctica
        
        if entrada.lower() == 'fin':
            break
        
        # Validación de números usando replace y isdigit (según tu preferencia)
        try_float = entrada.replace('.', '', 1).replace('-', '', 1)
        if try_float.isdigit():
            numeros.append(float(entrada))
        else:
            print("Entrada no válida. Por favor, ingresa un número o 'fin'.")
            
if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"Los números ingresados son: {numeros}")
        print(f"El promedio es: {promedio:.2f}")
else:
        print("No se ingresaron números para calcular el promedio.")