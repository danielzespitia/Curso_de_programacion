-- ###################################################################################
-- #                                                                                 #
-- #                     CURSO DETALLADO DE SQL CON MYSQL                              #
-- #                                                                                 #
-- #   Bienvenido a este curso práctico de SQL. Este script está diseñado para       #
-- #   ser tanto una guía de referencia como un tutorial interactivo. Cada           #
-- #   sección explica un concepto clave de SQL y proporciona ejemplos de código     #
-- #   que puedes ejecutar directamente en tu gestor de base de datos MySQL.         #
-- #                                                                                 #                                                            #
-- #                                                                                 #
-- ###################################################################################


-- ###################################################################################
-- # MÓDULO 1: INTRODUCCIÓN Y CONCEPTOS FUNDAMENTALES                                #
-- ###################################################################################

/*
CONCEPTOS CLAVE:

1.  BASE DE DATOS (Database):
    Una base de datos es una colección organizada de datos estructurados, almacenados electrónicamente en un sistema informático.
    Piensa en ella como un archivador digital muy eficiente, donde cada cajón, carpeta y documento está perfectamente ordenado para un acceso rápido.

2.  SGBD (Sistema de Gestión de Bases de Datos):
    Es el software que permite a los usuarios crear, leer, actualizar y administrar una base de datos. MySQL es un SGBD. Otros ejemplos son PostgreSQL, SQL Server, Oracle, etc.
    El SGBD es el "bibliotecario" que gestiona el archivador, sabe dónde está todo y cómo recuperarlo o guardarlo de forma segura.

3.  SQL (Structured Query Language - Lenguaje de Consulta Estructurado):
    Es el lenguaje estándar utilizado para comunicarse con un SGBD y realizar operaciones sobre los datos.
    SQL son las "instrucciones" que le das al bibliotecario (SGBD) para que trabaje con los documentos (datos).

4.  SUBCONJUNTOS DE SQL:
    - DDL (Data Definition Language - Lenguaje de Definición de Datos): Define la estructura. Comandos: CREATE, ALTER, DROP.
    - DML (Data Manipulation Language - Lenguaje de Manipulación de Datos): Trabaja con los datos en sí. Comandos: INSERT, UPDATE, DELETE.
    - DQL (Data Query Language - Lenguaje de Consulta de Datos): Se usa para consultar y recuperar datos. Comando principal: SELECT.
*/

-- Primero, creamos nuestra base de datos para el curso.
-- CREATE DATABASE crea un nuevo contenedor lógico para nuestras tablas y datos.
-- Es la primera instrucción que se suele ejecutar en un proyecto nuevo.
CREATE DATABASE IF NOT EXISTS ECommerceDB;

-- Usamos el comando USE para seleccionar la base de datos sobre la que queremos trabajar.
-- Todas las consultas siguientes se ejecutarán dentro de 'ECommerceDB'.
USE ECommerceDB;


-- ###################################################################################
-- # MÓDULO 2: DDL - LENGUAJE DE DEFINICIÓN DE DATOS                                 #
-- ###################################################################################

/*
El DDL se utiliza para construir y gestionar la arquitectura de la base de datos.
Con estos comandos, creamos las "cajas" (tablas) y definimos qué tipo de información irá en cada "compartimento" (columna).
*/

-- =================================================================================
-- CREACIÓN DE TABLAS (CREATE TABLE)
-- =================================================================================
/*
`CREATE TABLE` define una nueva tabla. Dentro de los paréntesis, especificamos las columnas.
Cada columna tiene:
1.  Un nombre (ej. `customer_id`).
2.  Un tipo de dato (ej. `INT`, `VARCHAR`).
    - `INT`: Para números enteros.
    - `VARCHAR(n)`: Para cadenas de texto de longitud variable, con un máximo de 'n' caracteres.
    - `PRIMARY KEY`: Es una restricción que identifica de forma única cada registro en una tabla. No puede contener valores NULL y cada valor debe ser único. Es el "DNI" de cada fila.
*/

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    country VARCHAR(100)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    item VARCHAR(100),
    amount INT,
    customer_id INT -- Esta columna relacionará el pedido con un cliente.
);

CREATE TABLE Shippings (
    shipping_id INT PRIMARY KEY,
    status VARCHAR(100),
    customer_id INT -- Esta columna relacionará el envío con un cliente.
);


-- =================================================================================
-- MODIFICACIÓN DE TABLAS (ALTER TABLE)
-- =================================================================================
/*
`ALTER TABLE` nos permite modificar una tabla existente. Es muy útil cuando los requisitos de un proyecto cambian y necesitamos
ajustar la estructura de datos sin tener que borrar y recrear la tabla.
*/

-- Ejemplo 1: Añadir una nueva columna.
-- Vamos a añadir una columna para el correo electrónico del cliente en la tabla `Customers`.
ALTER TABLE Customers
ADD COLUMN email VARCHAR(150);

-- Ejemplo 2: Modificar el tipo de dato de una columna.
-- Supongamos que 100 caracteres para el 'status' en Shippings es poco. Lo cambiamos a 120.
ALTER TABLE Shippings
MODIFY COLUMN status VARCHAR(120);

-- Ejemplo 3: Eliminar una columna.
-- Si decidimos que la edad no es relevante, podemos eliminar esa columna.
ALTER TABLE Customers
DROP COLUMN age;


-- =================================================================================
-- ELIMINACIÓN DE TABLAS (DROP TABLE)
-- =================================================================================
/*
`DROP TABLE` elimina una tabla por completo, incluyendo su estructura, todos sus datos y los índices asociados.
¡CUIDADO! Esta acción es irreversible. Una vez que una tabla es eliminada, la única forma de recuperarla es a través de una copia de seguridad.
*/

-- Para el propósito del curso, no la ejecutaremos, pero así es como se haría:
-- DROP TABLE Shippings;


-- ###################################################################################
-- # MÓDULO 3: DML - LENGUAJE DE MANIPULACIÓN DE DATOS                               #
-- ###################################################################################
/*
Ahora que tenemos la estructura, el DML nos permite "llenar los archivadores".
Con estos comandos, añadimos, modificamos y borramos los registros (las filas) dentro de nuestras tablas.
*/

-- =================================================================================
-- INSERCIÓN DE DATOS (INSERT INTO)
-- =================================================================================
/*
`INSERT INTO` añade nuevas filas a una tabla.
La sintaxis `INSERT INTO nombre_tabla (columna1, columna2, ...) VALUES (valor1, valor2, ...)` es la más clara,
ya que especifica explícitamente dónde va cada valor.
*/
-- (Primero, volvemos a añadir la columna 'age' que borramos antes para que los inserts funcionen)
ALTER TABLE Customers ADD COLUMN age INT;

INSERT INTO Customers (customer_id, first_name, last_name, age, country, email) VALUES
(1, 'Juan', 'Perez', 28, 'Mexico', 'juan.perez@email.com'),
(2, 'Ana', 'García', 34, 'España', 'ana.garcia@email.com'),
(3, 'Carlos', 'Rodriguez', 45, 'Argentina', 'carlos.r@email.com'),
(4, 'Maria', 'Lopez', 22, 'Colombia', 'maria.lopez@email.com'),
(5, 'Luis', 'Martinez', 52, 'Mexico', 'luis.martinez@email.com');

INSERT INTO Orders (order_id, item, amount, customer_id) VALUES
(101, 'Laptop', 1, 1),
(102, 'Mouse', 2, 1),
(103, 'Teclado', 1, 2),
(104, 'Monitor', 1, 3),
(105, 'Webcam', 1, 4),
(106, 'Mouse', 1, 4),
(107, 'Laptop', 1, 5);

INSERT INTO Shippings (shipping_id, status, customer_id) VALUES
(201, 'Shipped', 1),
(202, 'Pending', 2),
(203, 'Delivered', 3),
(204, 'Shipped', 4);


-- =================================================================================
-- ACTUALIZACIÓN DE DATOS (UPDATE)
-- =================================================================================
/*
`UPDATE` modifica los registros existentes en una tabla.
La cláusula `WHERE` es CRUCIAL. Si olvidas el `WHERE`, ¡actualizarás TODAS las filas de la tabla!
La sintaxis es `UPDATE nombre_tabla SET columna1 = valor1, columna2 = valor2, ... WHERE condicion;`
*/

-- Ejemplo: El cliente Carlos Rodriguez se ha mudado a Chile.
UPDATE Customers
SET country = 'Chile'
WHERE customer_id = 3;


-- =================================================================================
-- ELIMINACIÓN DE DATOS (DELETE)
-- =================================================================================
/*
`DELETE FROM` elimina filas de una tabla.
Al igual que con `UPDATE`, la cláusula `WHERE` es FUNDAMENTAL. Si la omites, ¡borrarás TODOS los datos de la tabla!
*/

-- Ejemplo: El cliente ha cancelado el pedido 106.
DELETE FROM Orders
WHERE order_id = 106;


-- ###################################################################################
-- # MÓDULO 4: DQL - LENGUAJE DE CONSULTA DE DATOS (FUNDAMENTOS)                     #
-- ###################################################################################
/*
El DQL es posiblemente la parte más utilizada de SQL en el día a día.
Nos permite hacer "preguntas" a nuestra base de datos para extraer la información que necesitamos.
*/

-- =================================================================================
-- SELECCIÓN BÁSICA (SELECT, FROM)
-- =================================================================================
/*
`SELECT` especifica las columnas que quieres ver.
`FROM` especifica la tabla de la que quieres obtener los datos.
El asterisco `*` es un comodín que significa "todas las columnas".
*/

-- Seleccionar toda la información de todos los clientes.
SELECT * FROM Customers;

-- Seleccionar solo el nombre, apellido y país de los clientes.
SELECT first_name, last_name, country FROM Customers;


-- =================================================================================
-- FILTRADO DE DATOS (WHERE)
-- =================================================================================
/*
`WHERE` se usa para filtrar registros y obtener solo aquellos que cumplen una condición específica.
Permite hacer preguntas mucho más precisas.
*/

-- Clientes que son de Mexico.
SELECT * FROM Customers WHERE country = 'Mexico';

-- Clientes que tienen más de 30 años.
SELECT * FROM Customers WHERE age > 30;

-- Pedidos con una cantidad de items mayor o igual a 2.
SELECT * FROM Orders WHERE amount >= 2;

-- Clientes que NO son de España.
SELECT * FROM Customers WHERE country != 'España';

-- Uso de `AND` (ambas condiciones deben ser verdaderas)
-- Clientes de Mexico que tienen más de 30 años.
SELECT * FROM Customers WHERE country = 'Mexico' AND age > 30;

-- Uso de `OR` (al menos una de las condiciones debe ser verdadera)
-- Clientes que son de Colombia O de Argentina.
SELECT * FROM Customers WHERE country = 'Colombia' OR country = 'Argentina';


-- =================================================================================
-- ORDENAMIENTO DE RESULTADOS (ORDER BY)
-- =================================================================================
/*
`ORDER BY` se utiliza para ordenar el conjunto de resultados por una o más columnas.
`ASC` (Ascendente) es el orden por defecto.
`DESC` (Descendente) ordena de mayor a menor.
*/

-- Ordenar a los clientes por su nombre de la A a la Z.
SELECT * FROM Customers ORDER BY first_name ASC;

-- Ordenar a los clientes por edad, del más viejo al más joven.
SELECT * FROM Customers ORDER BY age DESC;

-- Ordenar por múltiples columnas: por país, y dentro de cada país, por nombre.
SELECT * FROM Customers ORDER BY country, first_name;


-- ###################################################################################
-- # MÓDULO 5: DQL - CONSULTAS INTERMEDIAS (AGREGACIÓN Y AGRUPAMIENTO)               #
-- ###################################################################################
/*
Aquí es donde SQL empieza a mostrar su verdadero poder analítico.
Podemos realizar cálculos sobre conjuntos de datos para obtener resúmenes y métricas.
*/

-- =================================================================================
-- FUNCIONES DE AGREGADO
-- =================================================================================
/*
Estas funciones toman un conjunto de valores (una columna) y devuelven un único valor.
*/

-- `COUNT()`: Cuenta el número de filas.
-- ¿Cuántos clientes tenemos en total?
SELECT COUNT(*) FROM Customers;

-- `SUM()`: Suma los valores de una columna numérica.
-- ¿Cuál es la cantidad total de items vendidos en todos los pedidos?
SELECT SUM(amount) FROM Orders;

-- `AVG()`: Calcula el promedio.
-- ¿Cuál es la edad promedio de nuestros clientes?
SELECT AVG(age) FROM Customers;

-- `MAX()` y `MIN()`: Obtienen el valor máximo y mínimo.
-- ¿Cuál es la edad del cliente más viejo y del más joven?
SELECT MAX(age), MIN(age) FROM Customers;


-- =================================================================================
-- AGRUPAMIENTO DE DATOS (GROUP BY)
-- =================================================================================
/*
`GROUP BY` agrupa filas que tienen los mismos valores en columnas específicas en filas de resumen.
Se usa casi siempre con funciones de agregado para realizar cálculos por grupo.
*/

-- ¿Cuántos clientes tenemos por cada país?
-- La consulta agrupa todas las filas por el valor de 'country', y luego `COUNT` cuenta las filas de cada grupo.
SELECT country, COUNT(*) AS total_clientes
FROM Customers
GROUP BY country;


-- =================================================================================
-- FILTRADO DE GRUPOS (HAVING)
-- =================================================================================
/*
`HAVING` es como un `WHERE`, pero para los grupos creados por `GROUP BY`.
`WHERE` filtra filas antes de agrupar.
`HAVING` filtra grupos después de agrupar.
*/

-- Mostrar solo los países que tienen más de 1 cliente.
SELECT country, COUNT(*) AS total_clientes
FROM Customers
GROUP BY country
HAVING COUNT(*) > 1;


-- ###################################################################################
-- # MÓDULO 6: DQL - CONSULTAS AVANZADAS (UNIONES Y SUBCONSULTAS)                    #
-- ###################################################################################
/*
La capacidad de combinar datos de múltiples tablas es fundamental en bases de datos relacionales.
*/

-- =================================================================================
-- UNIONES DE TABLAS (JOINs)
-- =================================================================================
/*
Un `JOIN` combina filas de dos o más tablas basándose en una columna relacionada entre ellas.
La columna `customer_id` es nuestra "llave" para conectar las tablas.
*/

-- `INNER JOIN`: Devuelve solo las filas que tienen una coincidencia en AMBAS tablas.
-- Queremos ver cada pedido con el nombre y apellido del cliente que lo realizó.
SELECT
    Orders.order_id,
    Orders.item,
    Customers.first_name,
    Customers.last_name
FROM Orders
INNER JOIN Customers ON Orders.customer_id = Customers.customer_id;

-- `LEFT JOIN`: Devuelve TODAS las filas de la tabla de la izquierda (`Customers`) y las filas coincidentes de la tabla de la derecha (`Orders`).
-- Si un cliente no tiene pedidos, las columnas de `Orders` aparecerán como `NULL`.
-- Esto es útil para encontrar, por ejemplo, clientes que nunca han comprado.
SELECT
    Customers.first_name,
    Customers.last_name,
    Orders.order_id,
    Orders.item
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id;


-- =================================================================================
-- SUBCONSULTAS (SUBQUERIES)
-- =================================================================================
/*
Una subconsulta es una consulta `SELECT` anidada dentro de otra consulta.
La consulta interna se ejecuta primero, y su resultado es utilizado por la consulta externa.
*/

-- Queremos encontrar los nombres de los clientes que han comprado una 'Laptop'.
-- 1. La subconsulta `(SELECT customer_id FROM Orders WHERE item = 'Laptop')` se ejecuta primero. Devuelve una lista de IDs de clientes (1, 5).
-- 2. La consulta externa usa esa lista: `SELECT * FROM Customers WHERE customer_id IN (1, 5);`
SELECT first_name, last_name
FROM Customers
WHERE customer_id IN (SELECT customer_id FROM Orders WHERE item = 'Laptop');


-- ###################################################################################
-- # MÓDULO 7: SQL INTERMEDIO - ÍNDICES Y CLAVES FORÁNEAS                            #
-- ###################################################################################

-- =================================================================================
-- ÍNDICES (INDEXES)
-- =================================================================================
/*
Un índice es una estructura de datos que mejora la velocidad de las operaciones de recuperación de datos en una tabla.
Piensa en el índice de un libro: en lugar de leer todo el libro para encontrar un tema, vas al índice, que te dice la página exacta.
Los índices en SQL funcionan de manera similar. Se crean en una o más columnas.
Son especialmente útiles en columnas que se usan frecuentemente en cláusulas `WHERE` y en `JOINs`.
*/

-- Crear un índice en la columna `customer_id` de la tabla `Orders` acelerará las uniones con la tabla `Customers`.
CREATE INDEX idx_orders_customer_id ON Orders (customer_id);


-- =================================================================================
-- CLAVES FORÁNEAS (FOREIGN KEYS)
-- =================================================================================
/*
Una clave foránea es una clave utilizada para vincular dos tablas. Es un campo (o colección de campos) en una tabla
que se refiere a la `PRIMARY KEY` en otra tabla.
Su principal propósito es garantizar la **integridad referencial** de los datos. Esto significa que:
- No puedes crear un pedido para un `customer_id` que no existe en la tabla `Customers`.
- No puedes eliminar un cliente si este tiene pedidos asociados (a menos que se configure de otra manera).
*/

-- Añadimos una restricción de clave foránea a la tabla `Orders`.
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id);

-- FIN DEL CURSO --
