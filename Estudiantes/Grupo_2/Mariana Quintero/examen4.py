print("\n---ejercicio 4 frecuencia de palabras en un texto---")
parrafo = ("la casa es grande y puerta roja")
palabras = parrafo.lower().split()
frecuencias = {"la":2,"casa":1,"es":2,"grande":1,"y":1,"puerta":1,"roja":1}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias [palabra] = 1

print ("la casa es grande y puerta roja:")
print(frecuencias)