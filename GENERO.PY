import xlrd
import pyodbc

book = xlrd.open_workbook(r'C:\\Users\\Julian\\Downloads\\TABLAS_PRUEBA_ING_DATOS.xlsx')
sheet = book.sheet_by_name('clientes')

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

print("Se insertaron registros en la tabla GENERO")
cursor.close()
conn.close()
