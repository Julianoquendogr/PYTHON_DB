###############################################################################################
#       FUNCIÓN QUE INSERTA DATOS DESDE .XLSX FILE EN LA TABLA DE ZONA EN SQL SERVER
###############################################################################################

import xlrd
import pyodbc

def InsertarZona(parameter_path):

    Path = str(parameter_path)
    book = xlrd.open_workbook(Path)
    sheet = book.sheet_by_name('cat_zona')

    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                        'Database=DB_PYTHON;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()

    for i in range(1, sheet.nrows):

        Cod_Pais_Region_Zona = sheet.cell(i, 0).value
        Desc_Zona = sheet.cell(i, 1).value
        Desc_Region = sheet.cell(i, 2).value
        Desc_Pais = sheet.cell(i, 3).value

        query = '''INSERT INTO ZONA (Cod_Pais_Region_Zona, Desc_Zona,Desc_Region, Desc_Pais) VALUES (?,?,?,?)'''
        values = (Cod_Pais_Region_Zona, Desc_Zona, Desc_Region, Desc_Pais)
        cursor.execute(query, values)
        conn.commit()

    print("Se insertaron : " + str(sheet.nrows - 1) + " registros en la tabla ZONA")
    cursor.close()
    conn.close()


