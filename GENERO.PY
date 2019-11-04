###############################################################################################
#       FUNCIÓN QUE INSERTA DATOS TABLA DE GENERO EN SQL SERVER
###############################################################################################

import xlrd
import pyodbc


def InsertarGenero():

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                          'Database=DB_PYTHON;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO GENERO (Cod_Genero, Desc_Genero) VALUES 
                    (1,'Masculino'),
                    (2,'Fenemino'),
                    (3,'No informa')
                    ''')
    conn.commit()

    print("Se insertaron : 3 registros en la tabla GENERO")
    cursor.close()
    conn.close()
