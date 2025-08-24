CREATE DATABASE ETL_DB;
GO

USE ETL_DB;
GO

CREATE TABLE Ventas (
	id_venta INT PRIMARY KEY,
	producto NVARCHAR(100),
	cantidad INT,
	precio_unitario DECIMAL(10,2),
	total DECIMAL(10,2),
	fecha DATE);

SELECT * FROM ventas;
