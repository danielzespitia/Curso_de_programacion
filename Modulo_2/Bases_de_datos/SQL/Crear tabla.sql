-- Creando tu Primera Base de Datos y Tabla (Lenguaje DDL)

-- DDL (Data Definition Language): Son los comandos que definen la estructura (el "esqueleto") de nuestra base de datos.

-- Ejemplo Práctico:

-- Crear la Base de Datos

CREATE DATABASE mi_tienda;

-- Seleccionar la Base de Datos para usarla:

USE mi_tienda;

-- Crear una Tabla: Vamos a crear una tabla para guardar usuarios.

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    fecha_registro DATE,
    activo BOOLEAN DEFAULT TRUE
);
-- INT: Número entero.

-- AUTO_INCREMENT: El id se numerará solo (1, 2, 3...).

-- PRIMARY KEY: Es el identificador único de cada fila. No puede haber dos iguales.

-- VARCHAR(100): Texto de hasta 100 caracteres.

-- NOT NULL: Este campo es obligatorio.

-- UNIQUE: No puede haber dos usuarios con el mismo email.

-- DATE: Para guardar fechas.

-- DEFAULT TRUE: Si no especificamos nada, el usuario estará activo por defecto.