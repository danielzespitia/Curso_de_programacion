// Guardar como: app_js.mjs (o configurar package.json con "type": "module")

// 1. Importar las librerías necesarias
import { MongoClient } from 'mongodb';

// --- Variables de Conexión ---
const MONGO_URI = "mongodb://localhost:27017/";
const DATABASE_NAME = "tienda_tech";
const COLLECTION_NAME = "productos";

// Creamos un cliente de MongoDB
const client = new MongoClient(MONGO_URI);

// La lógica principal debe estar en una función async
async function main() {
  try {
    // 2. Conectar al servidor de MongoDB
    await client.connect();
    console.log("✅ Conexión a MongoDB exitosa.");

    // 3. Seleccionar la Base de Datos y la Colección
    const db = client.db(DATABASE_NAME);
    const collection = db.collection(COLLECTION_NAME);

    // (Opcional) Limpiar la colección para empezar de cero en cada ejecución
    await collection.deleteMany({});
    console.log("\n🧹 Colección limpiada.");

    // 4. CREAR: Insertar un nuevo documento
    const productoNuevo = {
        nombre: "Smartwatch Pro",
        marca: "TechFlow",
        precio: 249.99,
        disponible: true, // En JS, el booleano es true
        caracteristicas: ["GPS", "Monitor Cardiaco", "Resistente al agua"],
        especificaciones: {
            pantalla: "AMOLED 1.4 pulgadas",
            bateria_dias: 7
        }
    };
    const result = await collection.insertOne(productoNuevo);
    console.log(`\n📄 CREAR: Producto insertado con ID: ${result.insertedId}`);

    // 5. LEER: Buscar documentos
    // a) Buscar un documento por su nombre
    console.log("\n🔍 LEER: Buscando el 'Smartwatch Pro'...");
    const productoEncontrado = await collection.findOne({ nombre: "Smartwatch Pro" });
    console.log(`   -> Encontrado: ${productoEncontrado.nombre} - Precio: $${productoEncontrado.precio}`);

    // b) Buscar todos los productos de una marca
    console.log("\n🔍 LEER: Buscando todos los productos de la marca 'TechFlow'...");
    const productosMarca = await collection.find({ marca: "TechFlow" }).toArray();
    productosMarca.forEach(prod => {
        console.log(`   -> Producto: ${prod.nombre}`);
    });

    // 6. ACTUALIZAR: Modificar un documento
    console.log("\n🔄 ACTUALIZAR: Bajando el precio y añadiendo una nueva característica...");
    // Los operadores $set y $push son idénticos a los de Python
    const updateQuery = { nombre: "Smartwatch Pro" };
    const newValues = {
        $set: { precio: 229.99 },
        $push: { caracteristicas: "NFC para pagos" }
    };
    await collection.updateOne(updateQuery, newValues);
    const productoActualizado = await collection.findOne(updateQuery);
    console.log(`   -> Nuevo precio: $${productoActualizado.precio}`);
    console.log(`   -> Características: ${productoActualizado.caracteristicas}`);

    // 7. BORRAR: Eliminar un documento
    console.log("\n❌ BORRAR: Eliminando el 'Smartwatch Pro'...");
    const deleteResult = await collection.deleteOne({ nombre: "Smartwatch Pro" });
    console.log(`   -> Documentos eliminados: ${deleteResult.deletedCount}`);
    // Comprobar que ya no existe
    const productoFinal = await collection.findOne({ nombre: "Smartwatch Pro" });
    console.log(`   -> ¿Producto existe después de borrar? ${productoFinal ? 'Sí' : 'No'}`);

  } catch (e) {
    console.error("❌ Error en la operación de MongoDB:", e);
  } finally {
    // 8. Cerrar la conexión siempre al final
    await client.close();
    console.log("\n🔌 Conexión cerrada.");
  }
}

// Ejecutar la función principal y capturar errores
main().catch(console.error);