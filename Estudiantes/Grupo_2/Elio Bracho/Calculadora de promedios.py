numeros = []
dato_del_usuario = ""
print("Esta es una calculadora de promedios")
print("Escribe os numeros uno por uno, a finaizar, escribe fin")
while dato_del_usuario.lower() != "fin":
    dato_del_usuario = input("Escribe un numero (o 'fin' al terminar)> ")
    if dato_del_usuario.lower() == "fin":
        break
    try:
        numero = float(dato_del_usuario)
        numeros.append(numero)
    except ValueError:
        print("Error, no es un numero vaido, vuelve a intentarlo")
if numeros:
    suma = sum(numeros)
    cantidad_de_numeros = len(numeros)
    promedio = suma / cantidad_de_numeros
    print("Resultado")
    print(f"numeros que ingresaste: {numeros}")
    print(f"Suma tota: {suma:.2f}")
    print(f"Cantidad de numeros: {cantidad_de_numeros}")
    print(f"El promedio es: {promedio}")
else:
    ("\nNo ingresaste ningun numero")    
