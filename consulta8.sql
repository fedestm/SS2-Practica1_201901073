USE [usacdelivery]
GO

-- Consulta 8
-- Total de Entregas por días de la semana
SELECT tm.dia AS dia, COUNT(*) AS total_entregas FROM Tiempo tm
INNER JOIN Entregas en ON en.idTiempo = tm.id
GROUP BY tm.dia
;