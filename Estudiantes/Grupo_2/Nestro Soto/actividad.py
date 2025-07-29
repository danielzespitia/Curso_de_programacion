contador = 1
while contador <11:
    print (f"contador: {contador}")
    contador += 1
print ("\n\n--- Contador for")
for contadorfor in range (10):
    print (f"contador {contadorfor + 1 }")
print("\n\n Lista")
nombres= ("Ana", "Daniel" ,"Jose") 
for nombre in nombres: 
    print (f"Hola {nombre}")
print ("\n\n siguiente ejercicio")
edades_familiares= [51, 46, 70, 23, 17]
print ("edades de la familia:",edades_familiares)
print(f"El primer elemento de la lista es:{edades_familiares}")

# Consulta de una edad en especifico 
print (f"La edad de mi Padre es: {edades_familiares[0]}")
print (f"Mi edad es: {edades_familiares[-1]}")
edades_familiares[4] = 18
print (f"Mi edad despues de mi cumpleaños es: {edades_familiares[4]} años")
edades_familiares.append(25)
print(f"Las edades de mi familia despues de mi cuñado {edades_familiares}")
edades_familiares.insert(0,70)
print(f"La edad de mi familia añadiendo a i abuela paterna {edades_familiares}")
edades_familiares.remove(70)
print(f"La edad de mi familia sin mi abuela paterna {edades_familiares}")
del edades_familiares [3]
print (f"Edades de mi familia sin mi hermana {edades_familiares}")
edades_familiares.sort()
print(edades_familiares)
edades_familiares.reverse()
print(edades_familiares)
print(f"Miembros de mi familia {len(edades_familiares)}")

