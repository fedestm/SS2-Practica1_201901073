USE [usacdelivery]
GO

BULK INSERT Temporal FROM 'C:/Users/gnitr/Documents/Github/SS2-Practica1_201901073/EntregasUSAC-Delivery.csv'
WITH (
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '\n',
    CODEPAGE = 'ACP',
    DATAFILETYPE = 'Char',
    FIRSTROW = 2,
    TABLOCK 
    )
GO
SELECT * FROM Temporal