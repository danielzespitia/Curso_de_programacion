# --- Frecuencia de Palabras ---
    
print("Frecuencia de Palabras")
parrafo = input("Ingresa un párrafo de texto: ")
palabras = parrafo.lower().split()
frecuencias = {}
for palabra in palabras:
        palabra_limpia = palabra.strip(".,;:")
        if palabra_limpia:
                frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0 + 1)
        print("Frecuencia de palabras:")
        print(frecuencias)
        print("Frecuencia de palabras")


