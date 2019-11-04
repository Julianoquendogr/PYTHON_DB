###############################################################################################
#       FUNCIÓN QUE INSERTA DATOS DESDE .XLSX FILE EN LA TABLA DE SUCURSAL EN SQL SERVER
###############################################################################################

import xlrd
import pyodbc

def InsertarSucursal(parameter_path):

    Path = str(parameter_path)
    book = xlrd.open_workbook(Path)
    sheet = book.sheet_by_name('cat_sucursal')

    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                        'Database=DB_PYTHON;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()

    for i in range(1, sheet.nrows):

        Cod_Sucursal        = sheet.cell(i, 0).value
        Desc_Sucursal       = sheet.cell(i, 1).value
        Cod_Pais_Region_Zona= sheet.cell(i, 2).value
        Cod_Ciudad          = sheet.cell(i, 3).value

        query = '''INSERT INTO SUCURSAL (Cod_Sucursal, Desc_Sucursal, Cod_Pais_Region_Zona, Cod_Ciudad) VALUES (?,?,?,?)'''

        values = (Cod_Sucursal, Desc_Sucursal, Cod_Pais_Region_Zona, Cod_Ciudad)
        cursor.execute(query, values)
        conn.commit()

    print("Se insertaron : " + str(sheet.nrows - 1) + " registros en la tabla SUCURSAL")
    cursor.close()
    conn.close()
