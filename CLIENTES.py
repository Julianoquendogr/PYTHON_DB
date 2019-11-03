import xlrd
import pyodbc

book = xlrd.open_workbook(r'C:\\Users\\Julian\\Downloads\\TABLAS_PRUEBA_ING_DATOS.xlsx')
sheet = book.sheet_by_name('clientes')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                      'Database=DB_PYTHON;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

for i in range(1, sheet.nrows):

    Id                    = sheet.cell(i, 0).value
    Cod_Tip_Doc           = sheet.cell(i, 1).value
    Cod_Genero            = sheet.cell(i, 2).value
    Nombre_Completo       = sheet.cell(i, 4).value

    query = '''INSERT INTO CLIENTES (Id, Cod_Tip_Doc, Cod_Genero, Nombre_Completo) VALUES (?,?,?,?)'''
    #Cod_Cuidad = int(Cod_Cuidad)
    values = (Id, Cod_Tip_Doc, Cod_Genero, Nombre_Completo)
    cursor.execute(query, values)
    conn.commit()

print("Se insertaron : " + str(sheet.nrows - 1) + " registros en la tabla SUCURSAL")
cursor.close()
conn.close()
