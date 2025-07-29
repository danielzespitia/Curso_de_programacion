alumnos = {
    "Luis": {"Matematicas", "Historia", "Biologia"},
    "Ana": {"Matematicas", "Fisica", "Quimica"},
    "Carlos": {"Historia", "Arte", "Biologia"},
}

materias_unicas = alumnos["Luis"].union(alumnos["Ana"]).union(alumnos["Carlos"])
print("Materias unicas:", materias_unicas)

areas_comunes = alumnos["Luis"].intersection(alumnos["Ana"])
print("Areas comunes entre Luis y Ana:", areas_comunes)

alumnos["Carlos"].add("Fisica")
print("Materias de Carlos despues de agregar 'Fisica':", alumnos["Carlos"])

alumnos["Carlos"].discard("Arte")
print("Materias de Carlos despues de eliminar 'Arte':", alumnos["Carlos"])

for alumno, materias in alumnos.items():
    print(f"{alumno} cursa {len(materias)} materias.")
