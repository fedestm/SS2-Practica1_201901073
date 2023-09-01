USE [usacdelivery]
GO

-- Consulta 9
-- Total de Entregas por mes
SELECT tm.mes AS mes, COUNT(*) AS total_entregas FROM Tiempo tm
INNER JOIN Entregas en ON en.idTiempo = tm.id
GROUP BY tm.mes
;