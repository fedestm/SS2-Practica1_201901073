USE [usacdelivery]
GO

-- Consulta 6
-- Top 5 de envíos con estado Entregado
SELECT TOP 5 pr.nombre AS producto_entregado, COUNT(*) AS cantidad FROM Entregas en
INNER JOIN EstadoEntregas es ON en.idEstado_entregas = es.id
INNER JOIN Producto pr ON pr.id = en.idProducto
WHERE es.nombre = 'Entregado'
GROUP BY pr.nombre
ORDER BY cantidad DESC
;