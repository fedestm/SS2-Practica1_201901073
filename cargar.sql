USE [usacdelivery]
GO

WITH CTE AS (
    SELECT EntregaId, ROW_NUMBER() OVER (PARTITION BY EntregaId ORDER BY EntregaId) AS RowNumber
    FROM Temporal
)
DELETE FROM CTE WHERE RowNumber > 1;


-- Años, NombreProducto, EstadoEntregas, PrecioProducto vacíos
DELETE FROM Temporal WHERE Anios = '' OR NombreProducto = '' OR EstadoEntrega = '' OR PrecioProducto = '';

INSERT INTO Ciudad (nombre)
(
    SELECT DISTINCT CiudadEntrega FROM Temporal
)

INSERT INTO Cliente (nombre, direccion)
(
    SELECT DISTINCT NombreCliente, Direccion FROM Temporal
)

INSERT INTO Empleado (nombre, puesto)
(
    SELECT DISTINCT NombreEmpleadoEntrega, PuestoEmpleadoEntrega FROM Temporal
)

INSERT INTO EstadoEntregas (nombre)
(
    SELECT DISTINCT EstadoEntrega FROM Temporal
)

INSERT INTO Producto (nombre, descripcion, peso, precio)
(
    SELECT DISTINCT NombreProducto, Descripcion, Peso, PrecioProducto FROM Temporal
)
select * from Tiempo;
INSERT INTO Tiempo (dia, mes, anio)
(
    SELECT DISTINCT Dias, Meses, Anios FROM Temporal
)
GO
INSERT INTO Entregas (entregaid, tiempo_entrega, costo, idTiempo, idEmpleado, idCliente, idCiudad, idProducto, idEstado_entregas)
SELECT
    EntregaId,
    TiempoEntrega,
    CostoEnvio,
    Tiempo.id AS idTiempo,
    Empleado.id AS idEmpleado,
    Cliente.id AS idCliente,
    Ciudad.id AS idCiudad,
    Producto.id AS idProducto,
    EstadoEntregas.id AS idEstado_entregas
FROM Temporal
INNER JOIN Tiempo ON Temporal.Dias = Tiempo.dia AND Temporal.Meses = Tiempo.mes AND Temporal.Anios = Tiempo.anio
INNER JOIN Empleado ON Temporal.NombreEmpleadoEntrega = Empleado.nombre AND Temporal.PuestoEmpleadoEntrega = Empleado.puesto
INNER JOIN Cliente ON Temporal.NombreCliente = Cliente.nombre AND Temporal.Direccion = Cliente.direccion
INNER JOIN Ciudad ON Temporal.CiudadEntrega = Ciudad.nombre
INNER JOIN Producto ON Temporal.NombreProducto = Producto.nombre AND Temporal.Descripcion = Producto.descripcion AND Temporal.Peso = Producto.peso AND Temporal.PrecioProducto = Producto.precio
INNER JOIN EstadoEntregas ON Temporal.EstadoEntrega = EstadoEntregas.nombre;

GO