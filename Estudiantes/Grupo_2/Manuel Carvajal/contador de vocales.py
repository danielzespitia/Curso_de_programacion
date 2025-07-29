print("\n\n contador de vocales y consonantes")
frase=input("\n ingresa una frase:\n   ")
vocales=0
consonantes=0
consonantes_lista="bcdfghjklmnñpqrstvwxyz"
vocales_lista= "a,e,i,o,u,á,é,í,ó,ú"
for letra in frase.lower():

     if letra in vocales_lista:
        vocales += 1

     elif letra.isalpha():
        consonantes += 1
        print("la frase ",frase,"posee", vocales ,"vocales y ", consonantes ," consonantes")