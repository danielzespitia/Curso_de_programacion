-- Borrar Datos (Delete)

-- Comando: DELETE FROM

-- ¡MÁXIMO CUIDADO! Siempre usa WHERE o borrarás toda la tabla.

-- Ejemplo: Borrar al usuario Carlos Ruiz.

DELETE FROM usuarios WHERE id = 3;
-- O podrías usar WHERE nombre = 'Carlos Ruiz';
-- O si quieres borrar a todos los usuarios que no estén activos:
DELETE FROM usuarios WHERE activo = FALSE;  
-- O si quieres borrar todos los usuarios (¡CUIDADO! Esto eliminará toda la tabla):
-- DELETE FROM usuarios;
-- Nota: En MySQL, si quieres eliminar la tabla completa y no solo los datos, usarías:
DROP TABLE usuarios;