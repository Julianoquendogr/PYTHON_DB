###############################################################################################
#       FUNCIÓN QUE INSERTA DATOS DESDE .XLSX FILE EN LA TABLA DE TIPO_DOC EN SQL SERVER
###############################################################################################

import xlrd
import pyodbc

def InsertarTipo_Doc(parameter_path):

    Path = str(parameter_path)
    book = xlrd.open_workbook(Path)
    sheet = book.sheet_by_name('cat_tip_doc')

    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                        'Database=DB_PYTHON;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()

    for i in range(1, sheet.nrows):

        Cod_Tip_Doc = sheet.cell(i, 0).value
        Desc_Tip_Doc = sheet.cell(i, 1).value

        query = '''INSERT INTO TIPO_DOC (Cod_Tip_Doc, Desc_Tip_Doc) VALUES (?,?)'''
        values = (Cod_Tip_Doc, Desc_Tip_Doc)
        cursor.execute(query, values)
        conn.commit()

    print("Se insertaron : " + str(sheet.nrows - 1) +
        " registros en la tabla TIPO_DOC")
    cursor.close()
    conn.close()
