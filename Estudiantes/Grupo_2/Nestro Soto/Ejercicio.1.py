"""Objetivo: Practicar bucles for y condicionales if-elif else con cadenas de texto"""
"""Enunciado:"""
"""Escribe un programa que pida al usuario que ingrese una frase. El programa debe iterar a traves de la fase y contar el número de vocales (a,e,i,o,u) y consonantes. Al final, debe imprimir ambos conteos."""

#Ejercicio
def Contador_de_vocales_y_consonantes():
    print ("contador de vocales y consonantes")
    frase = input("Inserta tu palabra").lower()
    vocales = 0 
    consonantes = 0
    vocales_lista = "aeiouáéíóú"
    for letra in frase.lower():
        if letra in vocales_lista:
            vocales += 1 
        elif letra.isalpha (): 
            consonantes += 1 
            print (f"La frase {frase} tiene ")

    print (f"El número de vocales es: {vocales} y el numero de consonantes es : {consonantes}")
Contador_de_vocales_y_consonantes()
#fin del ejercicio 

     
           

               

 