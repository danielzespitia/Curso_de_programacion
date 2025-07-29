edades_familiares = [44, 43, 24, 19, 15]
print("las edades de mi familia son:",edades_familiares)

# Consulta de una edad en espcifico
print(f"La edad de mi hermana es: {edades_familiares[2]} años")

# Modificar edad
edades_familiares[2] = 25
print(f"La edad de mi hermana ahora es: {edades_familiares[2]} años")

edades_familiares.append(30) # Añadir una ueva edad al final de la lista
edades_familiares.insert(0, 20) # Insertar una nueva edad al inicio de la lista
print(edades_familiares)

edades_familiares.remove(44) # Eliminar una edad especifica
print(edades_familiares)

edades_familiares.sort() # Ordenar las edades de menor a mayor
print(edades_familiares)
edades_familiares.reverse() # Invertir el orden de las edades
print(edades_familiares)

print(f"La lista tiene {len(edades_familiares)} edades registradas.")