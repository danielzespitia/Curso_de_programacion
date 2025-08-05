-- Actualizar Datos (Update)

-- Comando: UPDATE

-- ¡CUIDADO! Siempre usa WHERE en un UPDATE o modificarás toda la tabla.

-- Ejemplo: Cambiar el email de Ana Gómez.

UPDATE usuarios
SET email = 'ana.gomez.nuevo@email.com'
WHERE id = 2; -- O podrías usar WHERE nombre = 'Ana Gómez'