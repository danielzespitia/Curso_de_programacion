edades_familia = [23, 51, 50, 75]
print ("las edades de mi familia son:", edades_familia)

print("edad de mi mama:", edades_familia[1] )
print("edad de mi abuela:", edades_familia[-1])
print(f"mi edad es : {edades_familia[0]}")
print(f"edad de mario es: {edades_familia [2]}")

edades_familia[2] = 49
print(f"la edad de mario ahora es: {edades_familia[2]} años")

edades_familia.append(12)
print(edades_familia)

edades_familia.remove(51)
print(edades_familia)

edades_familia.sort()
print(edades_familia)

edades_familia.reverse()
print(edades_familia)

print(f"la lista tiene {len(edades_familia)} edades registradas")