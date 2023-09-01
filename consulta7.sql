USE [usacdelivery]
GO

-- Consulta 7
-- Total de entregas realizadas por ciudad.
SELECT cd.nombre AS ciudad, COUNT(*) AS total_entregas FROM Ciudad cd
INNER JOIN Entregas en ON en.idCiudad = cd.id
GROUP BY cd.nombre
;
