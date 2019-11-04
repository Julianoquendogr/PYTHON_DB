import xlrd
import pyodbc

book = xlrd.open_workbook(r'C:\\Users\\Julian\\Downloads\\TABLAS_PRUEBA_ING_DATOS.xlsx')
sheet = book.sheet_by_name('cat_ciudad')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                      'Database=DB_PYTHON;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

for i in range(1, sheet.nrows):

    Cod_Ciudad        = sheet.cell(i, 0).value
    Desc_Ciudad       = sheet.cell(i, 1).value
    Desc_Departamento = sheet.cell(i, 2).value
    Desc_Pais         = sheet.cell(i, 3).value

    query = '''INSERT INTO CIUDAD (Cod_Ciudad, Desc_Ciudad, Desc_Departamento, Desc_Pais) VALUES (?,?,?,?)'''
   
    values = (Cod_Ciudad, Desc_Ciudad, Desc_Departamento, Desc_Pais)
    cursor.execute(query, values)
    conn.commit()

print("Se insertaron : " + str(sheet.nrows - 1) + " registros en la tabla CIUDAD")
cursor.close()
conn.close()
