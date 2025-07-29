import json

def contar_frecuencia_palabras(parrafo):
    parrafo = parrafo.lower()
    palabras = parrafo.replace(",", "").replace(".", "").split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

if _name_ == "_main_":
    parrafo_entrada = "La casa es grande y la puerta es roja"
    resultado = contar_frecuencia_palabras(parrafo_entrada)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

    parrafo_entrada_2 = "Este es un ejemplo, este ejemplo es simple."
    resultado_2 = contar_frecuencia_palabras(parrafo_entrada_2)
    print(json.dumps(resultado_2, indent=2, ensure_ascii=False))