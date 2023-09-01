USE [usacdelivery]
GO

-- Consulta 4
-- Top 5 de ciudades con más entregas
SELECT TOP 5 ci.nombre AS ciudad, COUNT(*) AS entregas_totales FROM Ciudad ci
INNER JOIN Entregas en ON ci.id = en.idCiudad
GROUP BY ci.nombre
ORDER BY entregas_totales DESC
;