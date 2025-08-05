# Importar la librería estándar de Python para trabajar con JSON
import json

# 1. Crear la estructura de datos usando un diccionario de Python.
#    Esta es la forma en que trabajas con los datos dentro de tu programa.
#    Nota que es casi idéntico al ejemplo de MongoDB, porque pymongo usa
#    esta misma estructura.
producto_dict = {
    "id_producto": "SKU-TV-001",
    "nombre": "Televisor Smart 4K",
    "categoria": "Electrónica",
    "precio": 499.99,
    "disponible": True,  # En Python es True, en JSON se convierte a true
    "especificaciones": {
        "resolucion": "3840x2160",
        "tamano_pantalla": "55 pulgadas",
        "puertos_hdmi": 4
    },
    "opiniones": [
        {
            "usuario": "juan_perez",
            "calificacion": 5,
            "comentario": "Excelente calidad de imagen."
        },
        {
            "usuario": "ana_gomez",
            "calificacion": 4,
            "comentario": "El sonido podría ser mejor, pero la imagen es increíble."
        }
    ]
}

# 2. Convertir el diccionario de Python a una cadena de texto con formato JSON.
#    Esto es lo que se enviaría a una API o se guardaría en un archivo.
#    - json.dumps() significa "dump string" (volcar a cadena).
#    - indent=4 le dice a la librería que formatee el texto de manera legible.
json_string = json.dumps(producto_dict, indent=4)


# 3. Imprimir el resultado.
#    Esta variable 'json_string' contiene el código JSON puro.
print("--- CÓDIGO JSON GENERADO ---")
print(json_string)


# 4. El proceso inverso: convertir una cadena JSON de vuelta a un diccionario de Python.
#    Esto es lo que haría tu programa al recibir datos de una API.
#    - json.loads() significa "load string" (cargar desde cadena).
print("\n--- DICCIONARIO PYTHON RECONSTRUIDO DESDE JSON ---")
diccionario_reconstruido = json.loads(json_string)
# Ahora puedes acceder a los datos como lo harías con cualquier diccionario.
print(f"Nombre del producto: {diccionario_reconstruido['nombre']}")
print(f"Resolución: {diccionario_reconstruido['especificaciones']['resolucion']}")

