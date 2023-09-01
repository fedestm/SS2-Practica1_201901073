USE [usacdelivery]
GO

-- Consulta 10
-- Total de Entregas por año
SELECT tm.anio AS anio, COUNT(*) AS total_entregas FROM Tiempo tm
INNER JOIN Entregas en ON en.idTiempo = tm.id
GROUP BY tm.anio
;
