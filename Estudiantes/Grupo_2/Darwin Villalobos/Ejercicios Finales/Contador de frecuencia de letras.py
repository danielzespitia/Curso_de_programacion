palabra = "banana"

frecuencia = {}
for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra] += 1
    else:
        frecuencia[letra] = 1

print(frecuencia)
