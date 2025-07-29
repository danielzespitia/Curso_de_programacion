import json

def convertir_lista_a_diccionario(lista_de_tuplas):
    return dict(lista_de_tuplas)

if __name__ == "__main__":
    lista_entrada = [('nombre', 'Victor'), ('edad', 13), ('ciudad', 'Maracaibo')]
    resultado_diccionario = convertir_lista_a_diccionario(lista_entrada)
    print(json.dumps(resultado_diccionario, indent=2, ensure_ascii=False))