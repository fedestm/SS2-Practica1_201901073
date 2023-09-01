USE usacdelivery
GO
SELECT TOP 5 pr.nombre AS producto, MAX(en.costo) AS costo_envio FROM Producto pr
INNER JOIN Entregas en ON pr.id = en.idProducto
GROUP BY pr.nombre
ORDER BY costo_envio DESC