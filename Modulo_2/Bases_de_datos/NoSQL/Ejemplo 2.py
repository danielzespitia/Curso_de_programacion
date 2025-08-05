# Guardar como: app_python.py

# 1. Importar las librerías necesarias
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# --- Variables de Conexión ---
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "tienda_tech"
COLLECTION_NAME = "productos"

try:
    # 2. Conectar al servidor de MongoDB
    client = MongoClient(MONGO_URI)
    # Comprobar si la conexión fue exitosa
    client.admin.command('ping')
    print("✅ Conexión a MongoDB exitosa.")

    # 3. Seleccionar la Base de Datos y la Colección
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # (Opcional) Limpiar la colección para empezar de cero en cada ejecución
    collection.delete_many({})
    print("\n🧹 Colección limpiada.")

    # 4. CREAR: Insertar un nuevo documento
    producto_nuevo = {
        "nombre": "Smartwatch Pro",
        "marca": "TechFlow",
        "precio": 249.99,
        "disponible": True, # En Python, el booleano es True
        "caracteristicas": ["GPS", "Monitor Cardiaco", "Resistente al agua"],
        "especificaciones": {
            "pantalla": "AMOLED 1.4 pulgadas",
            "bateria_dias": 7
        }
    }
    result = collection.insert_one(producto_nuevo)
    print(f"\n📄 CREAR: Producto insertado con ID: {result.inserted_id}")

    # 5. LEER: Buscar documentos
    # a) Buscar un documento por su nombre
    print("\n🔍 LEER: Buscando el 'Smartwatch Pro'...")
    producto_encontrado = collection.find_one({"nombre": "Smartwatch Pro"})
    print(f"   -> Encontrado: {producto_encontrado['nombre']} - Precio: ${producto_encontrado['precio']}")

    # b) Buscar todos los productos de una marca
    print("\n🔍 LEER: Buscando todos los productos de la marca 'TechFlow'...")
    productos_marca = collection.find({"marca": "TechFlow"})
    for prod in productos_marca:
        print(f"   -> Producto: {prod['nombre']}")

    # 6. ACTUALIZAR: Modificar un documento
    print("\n🔄 ACTUALIZAR: Bajando el precio y añadiendo una nueva característica...")
    # $set modifica el valor de un campo.
    # $push añade un elemento a un array.
    update_query = {"nombre": "Smartwatch Pro"}
    new_values = {
        "$set": {"precio": 229.99},
        "$push": {"caracteristicas": "NFC para pagos"}
    }
    collection.update_one(update_query, new_values)
    producto_actualizado = collection.find_one(update_query)
    print(f"   -> Nuevo precio: ${producto_actualizado['precio']}")
    print(f"   -> Características: {producto_actualizado['caracteristicas']}")

    # 7. BORRAR: Eliminar un documento
    print("\n❌ BORRAR: Eliminando el 'Smartwatch Pro'...")
    delete_result = collection.delete_one({"nombre": "Smartwatch Pro"})
    print(f"   -> Documentos eliminados: {delete_result.deleted_count}")
    # Comprobar que ya no existe
    producto_final = collection.find_one({"nombre": "Smartwatch Pro"})
    print(f"   -> ¿Producto existe después de borrar? {'Sí' if producto_final else 'No'}")


except ConnectionFailure as e:
    print(f"❌ Error de conexión a MongoDB: {e}")
finally:
    # 8. Cerrar la conexión siempre al final
    if 'client' in locals() and client:
        client.close()
        print("\n🔌 Conexión cerrada.")