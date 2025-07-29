contador = 1
while contador < 11:
    print (f"contador:{contador}")
    contador +=1
            
            # Bucle for con range: Se usa para repetir un bloque de código un número específico de veces
for i in range(5):  # Repite 5 veces
    print(f"Iteración {i + 1}")  # Imprime el número de iteració

for i in range (10):
    print(f"Iteración {i + 1}")

#
edades_familiares = [46,23,40,9]
print (f"edades de mi familia:{edades_familiares}")

# consulta de una edad en especifico
print (f"la edad de mi hermano es:{edades_familiares[1]} años")

# modificar edad
edades_familiares[1]= 25
print (f"la edad de mi hermano ahora es:{edades_familiares [1]}")
    
edades_familiares.append(70) # añade una nueva edad al final
edades_familiares.insert(0, 17) # insertar a una nueva edad al inicio de la lista
print (edades_familiares)

edades_familiares.remove(9) #eliminar una edad especifica
print (edades_familiares) 

edades_familiares.sort() # ordena de menor a mayor
print(edades_familiares)

edades_familiares.reverse() #ordena de mayor a menor
print(edades_familiares)

