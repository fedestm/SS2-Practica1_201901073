USE [usacdelivery]
GO

SELECT TOP 5 cl.nombre, COUNT(en.id) AS entregas_realizadas FROM Entregas en
INNER JOIN Cliente cl ON cl.id = en.idCliente
GROUP BY cl.nombre
ORDER BY entregas_realizadas DESC