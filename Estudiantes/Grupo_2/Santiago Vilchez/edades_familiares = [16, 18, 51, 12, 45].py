edades_familiares = [16, 18, 51, 12, 45]

print(f"las edades de las familias son: {edades_familiares}")

# consulta de una edad en especifico
print(f"la edad de mi hermano es:{edades_familiares[0]} años")


# modificar edad
edades_familiares[0]=18
print(f"la edad de mi hermano ahora es: {edades_familiares[0]} años")

edades_familiares.append(16) # añadir una nueva edad al final de la lista
edades_familiares.insert(0,20) # insentar una nueva edad al inicio de la lista
print(edades_familiares)

edades_familiares.remove(45) # eliminar una edad especifica
print(edades_familiares)

edades_familiares.sort() # ordenar de las edades de menor a mayor
print(edades_familiares)

edades_familiares.reverse() # invertir el orden de las edades
print(edades_familiares)

print(f"la lista tiene{len (edades_familiares)} edades registradas")