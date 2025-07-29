def frecuencia(parrafo):
    parrafos=parrafo.lower()
    caracteres_a_reemplazar = [",", ".", "!", "?", "¿", "¡", ":", ";", ")", "(", "[", "]", "{", "}"]
    for caracter in caracteres_a_reemplazar:
        parrafos = parrafos.replace(caracter,' ')
        palabras = parrafos.split()    
    frecuencia_de_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_de_palabras:
            frecuencia_de_palabras[palabra] +=1
        else:
            frecuencia_de_palabras[palabra] =1
    return frecuencia_de_palabras     
if __name__ == "__main__":
    print("Veamos cuantas palabras hay")
    texto_usuario = input ("Por favor, ingresa tu texto: ")
    resultado = frecuencia (texto_usuario)
    print("\nCantidad de veces que se repiten las palabras")
    if resultado:
        for palabra, frecuencia_palabras in resultado.items():
            print(f"'{palabra}':{frecuencia_palabras}")
    else:
        print("No se encontraron palabras")
     


    