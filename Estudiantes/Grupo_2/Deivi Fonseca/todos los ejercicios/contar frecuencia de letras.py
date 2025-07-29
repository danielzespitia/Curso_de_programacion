frase = input("pon una palabra:")
palabras = ("palabra").lower

frecuencias = {}
for palabras in frase:
        palabra_limpia = palabras.strip(".,;:")
        if palabra_limpia:
                frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0 + 1)
        print("Frecuencia de palabras:")
        print(frecuencias)
        print("Frecuencia de palabras")