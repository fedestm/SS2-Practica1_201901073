USE [usacdelivery]
GO

-- Consulta 5
-- Top 5 de envíos con estado Pendiente
SELECT TOP 5 pr.nombre AS producto_pendiente, COUNT(*) AS cantidad FROM Entregas en
INNER JOIN EstadoEntregas es ON en.idEstado_entregas = es.id
INNER JOIN Producto pr ON pr.id = en.idProducto
WHERE es.nombre = 'Pendiente'
GROUP BY pr.nombre
ORDER BY cantidad DESC
;