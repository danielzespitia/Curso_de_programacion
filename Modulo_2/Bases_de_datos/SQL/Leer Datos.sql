-- Leer Datos (Read)

-- Comando: SELECT

-- Ejemplo: Consultar los usuarios que hemos insertado.

-- Seleccionar todas las columnas de todos los usuarios
SELECT * FROM usuarios;

-- Seleccionar solo el nombre y el email
SELECT nombre, email FROM usuarios;

-- Usar WHERE para filtrar: solo el usuario con id = 1
SELECT * FROM usuarios WHERE id = 1;

-- Filtrar por nombre y que estén activos
SELECT * FROM usuarios WHERE nombre = 'Ana Gómez' AND activo = TRUE;

-- Usar LIKE para buscar patrones (todos los emails que terminen en @email.com)
SELECT * FROM usuarios WHERE email LIKE '%@email.com';