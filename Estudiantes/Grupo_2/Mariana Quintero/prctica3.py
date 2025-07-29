edades_familiares = [15,21, 18, 17, 45]

print(f"las edades de mi familia son: {edades_familiares}")

# consulta de una edad en especifico
print(f"la edad de mi prima es : {edades_familiares[0]} años")


# modificar la edad 
edades_familiares[0]= 16
print(f"la edad de mi prima ahora es: {edades_familiares[0]}años")
edades_familiares.append(43) # añadir una nueva edad al final de la lista
edades_familiares.insert(0, 25) # insertar una nueva edad al inicio de la lista
print(edades_familiares)

edades_familiares.remove(18) # eliminar una edad especifica
print(edades_familiares)

edades_familiares.sort() # ordenar de las edades de menor a mayor
print(edades_familiares)

edades_familiares.reverse() # invertir el orden de ls edades 
print(edades_familiares)

print(f"la lista tiene{len (edades_familiares)} edades registradas")