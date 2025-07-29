# pregunta: escribe un programa que le pida al usuario ingresar una nota entre 0 y 20.
# Si la nota es mayor o igual a 10 el programa debe mostrar aprobado , de lo contrario, debe mostrar "desaprobado"
nota = int (input("Cual es tu nota?"))
if nota >= 10 and nota <= 20:
    print ("Aprobado")
elif nota <= 9: 
    print ("Desaprobado")
else:
    print ("Fuera de Rango")