-- Insertar Datos (Create)

-- Comando: INSERT INTO

-- Ejemplo: Añadir usuarios a nuestra tabla.

-- Insertar un solo usuario
INSERT INTO usuarios (nombre, email, fecha_registro)
VALUES ('Juan Pérez', 'juan.perez@email.com', '2025-07-01');

-- Insertar múltiples usuarios a la vez
INSERT INTO usuarios (nombre, email, fecha_registro) VALUES
('Ana Gómez', 'ana.gomez@email.com', '2025-07-02'),
('Carlos Ruiz', 'carlos.ruiz@email.com', '2025-07-03');