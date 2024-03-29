/*****************************************/
/***PROCEDIMIENTO ALMACENADO ***/
/**ELIMINAR EN EL SIGUENTE ORDER ***/
GO
CREATE PROCEDURE sp_EliminarTablas 
 AS
	BEGIN
	  DELETE  FROM CLIENTES;
	  DELETE FROM SUCURSAL;
	  DELETE FROM GENERO;
	  DELETE FROM ZONA;
	  DELETE FROM CIUDAD;
	  DELETE FROM TIPO_DOC;
END

EXEC sp_EliminarTablas;

/*****************************************/

/**INSERTAR EN EL SIGUENTE ORDEN ***/
		SELECT * FROM CIUDAD;
		SELECT * FROM ZONA;
		SELECT * FROM GENERO;
		SELECT * FROM TIPO_DOC;
		SELECT * FROM SUCURSAL;
		SELECT * FROM CLIENTES;

/***CONSULTAS PARA LOS REPORTES ***/
/***A***/
SELECT Edad AS EDAD, COUNT(*) as CANTIDAD, GENERO.Desc_Genero AS GENERO
FROM CLIENTES INNER JOIN GENERO ON  GENERO.Cod_Genero = CLIENTES.Cod_Genero
WHERE Edad >= 18 AND Edad <= 40
GROUP BY Edad, GENERO.Desc_Genero
HAVING COUNT(*) > 500	
ORDER BY Edad DESC;

/***B***/
SELECT COUNT(*) AS TOTAL_PERSONAS,
   	   CLIENTES.Edad AS EDAD, 
	   SUM(CLIENTES.Ingresos) AS TOTAL_INGRESOS, 
	   (SUM(CLIENTES.Ingresos)/COUNT(*)) AS PROMEDIO
FROM CLIENTES 
INNER JOIN GENERO ON CLIENTES.Cod_Genero = GENERO.Cod_Genero
GROUP BY CLIENTES.Edad
ORDER BY CLIENTES.Edad ASC;

/***C***/
SELECT COUNT(*),CIUDAD.Desc_Ciudad, GENERO.Desc_Genero FROM CIUDAD INNER JOIN SUCURSAL ON CIUDAD.Cod_Ciudad = CIUDAD.Cod_Ciudad 
INNER JOIN CLIENTES ON CLIENTES.Cod_Sucursal = SUCURSAL.Cod_Sucursal INNER JOIN GENERO ON GENERO.Cod_Genero = CLIENTES.Cod_Genero
GROUP BY CIUDAD.Desc_Ciudad, GENERO.Desc_Genero
ORDER BY COUNT(*) DESC;


/***D***/
SELECT CLIENTES.Nombre,CLIENTES.Edad,CLIENTES.Id,CIUDAD.Desc_Ciudad,ZONA.Desc_Zona 
FROM CIUDAD 
INNER JOIN SUCURSAL ON CIUDAD.Cod_Ciudad = SUCURSAL.Cod_Ciudad 
INNER JOIN ZONA ON ZONA.Cod_Pais_Region_Zona = SUCURSAL.Cod_Pais_Region_Zona 
INNER JOIN CLIENTES ON CLIENTES.Cod_Sucursal = SUCURSAL.Cod_Sucursal
WHERE ZONA.Cod_Pais_Region_Zona = 1690469
AND CIUDAD.Cod_Ciudad IN (169008001000,169085225009);

/*** Adicional ***/
SELECT CIUDAD.Desc_Ciudad,ZONA.Desc_Region,SUCURSAL.Desc_Sucursal,ZONA.Desc_Pais,CLIENTES.Id,CLIENTES.Nombre_Completo,CLIENTES.Fecha_Nacimiento,
CLIENTES.Edad FROM CIUDAD left JOIN SUCURSAL ON CIUDAD.Cod_Ciudad = CIUDAD.Cod_Ciudad left JOIN ZONA ON ZONA.Cod_Pais_Region_Zona = SUCURSAL.Cod_Pais_Region_Zona
right JOIN CLIENTES ON CLIENTES.Cod_Sucursal = SUCURSAL.Cod_Sucursal left JOIN GENERO ON GENERO.Cod_Genero = CLIENTES.Cod_Genero left JOIN TIPO_DOC ON
TIPO_DOC.Cod_Tip_Doc = CLIENTES.Cod_Genero WHERE CLIENTES.Id in (select id from CLIENTES where Nombre_Completo LIKE '%Juan%Gomez%');


SELECT CLIENTES.Nombre_Completo,CLIENTES.Id,CLIENTES.Fecha_Nacimiento,CLIENTES.Edad FROM CIUDAD left JOIN SUCURSAL ON CIUDAD.Cod_Ciudad = CIUDAD.Cod_Ciudad left JOIN ZONA ON ZONA.Cod_Pais_Region_Zona = SUCURSAL.Cod_Pais_Region_Zona
right JOIN CLIENTES ON CLIENTES.Cod_Sucursal = SUCURSAL.Cod_Sucursal left JOIN GENERO ON GENERO.Cod_Genero = CLIENTES.Cod_Genero left JOIN TIPO_DOC ON
TIPO_DOC.Cod_Tip_Doc = CLIENTES.Cod_Genero WHERE CLIENTES.Id in (select id from CLIENTES where Nombre_Completo LIKE '%Juan%Gomez%')
group by CLIENTES.Nombre_Completo,CLIENTES.Id,CLIENTES.Fecha_Nacimiento,CLIENTES.Edad;
/***(ciudad, región, sucursal, zona, país, nit, nombre completo, fecha_nacimiento,

ingresos)***/