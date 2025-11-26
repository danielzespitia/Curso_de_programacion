edades_familiares = [25, 28, 22, 55, 53] 

print("Las edades de mi familia son:", edades_familiares) 
print(f"Las edades de mi familia son: {edades_familiares}") 

# Consulta de una edad en especifico
print(f"La edad de mi hermana es: {edades_familiares[2]} años")

# Modificar edad 
edades_familiares[2] = 23  
print(f"La edad de mi hermana ahora es: {edades_familiares[2]} años")

edades_familiares.append(30)  # Añadir una nueva edad al final de la lista
edades_familiares.insert(0, 20)  # Insertar una nueva edad al inicio de la lista
print(edades_familiares)

edades_familiares.remove(55)  # Eliminar una edad específica
print(edades_familiares)

edades_familiares.sort()  # Ordenar las edades de menor a mayor
print(edades_familiares)

edades_familiares.reverse()  # Invertir el orden de las edades
print(edades_familiares)

print(f"\nLa lista tiene {len(edades_familiares)} edades registradas.")

