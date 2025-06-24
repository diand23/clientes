-- Crear base de datos (opcional, si tu gestor lo permite)
--CREATE DATABASE clientes;
--USE datos_clientes;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(20) NOT NULL,
    apellidos VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Tabla de facturas
CREATE TABLE IF NOT EXISTS facturas (
    numero_factura INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INT NOT NULL,
    fecha_emision DATETIME DEFAULT CURRENT_TIMESTAMP,
    descripcion VARCHAR(100) NOT NULL,
    monto DECIMAL(10, 2) NOT NULL CHECK (monto > 0),
    estado TEXT NOT NULL CHECK (estado IN ('Pendiente', 'Pagada', 'Cancelada')),
    FOREIGN KEY (id_cliente) REFERENCES usuarios(id_cliente) ON DELETE CASCADE
);

-- Insertar usuarios
INSERT INTO usuarios (id_cliente, nombre, apellidos, email, telefono, direccion)
VALUES
(3, 'María', 'López', 'maria.lopez@email.com', '555-2345', 'Plaza Mayor 10'),
(4, 'Carlos', 'Fernández', 'carlos.fernandez@email.com', '555-3456', 'Calle Real 45'),
(5, 'Sofía', 'Gómez', 'sofia.gomez@email.com', '555-4567', 'Avenida Central 100'),
(6, 'Jorge', 'Ramírez', 'jorge.ramirez@email.com', '555-5678', 'Calle Luna 21'),
(7, 'Elena', 'Díaz', 'elena.diaz@email.com', '555-6789', 'Boulevard Sol 5'),
(8, 'Miguel', 'Torres', 'miguel.torres@email.com', '555-7890', 'Calle Nubes 33'),
(9, 'Laura', 'Vargas', 'laura.vargas@email.com', '555-8901', 'Paseo del Río 12'),
(10, 'Andrés', 'Castillo', 'andres.castillo@email.com', '555-9012', 'Camino Real 9');

-- Insertar facturas
INSERT INTO facturas (id_cliente, descripcion, monto, estado)
VALUES
(3, 'Compra de muebles', 1200.00, 'Pagada'),
(4, 'Servicio de instalación', 300.00, 'Pendiente'),
(5, 'Venta de software', 2500.00, 'Pagada'),
(6, 'Mantenimiento anual', 450.00, 'Cancelada'),
(7, 'Consultoría en marketing', 1000.00, 'Pendiente'),
(8, 'Diseño gráfico', 700.00, 'Pagada'),
(9, 'Venta de hardware', 1800.00, 'Pagada'),
(10, 'Capacitación técnica', 850.00, 'Pendiente');


