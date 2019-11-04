###############################################################################################
#       FUNCIÓN QUE INSERTA DATOS DESDE .XLSX FILE EN LA TABLA DE CIUDADES EN SQL SERVER
###############################################################################################
import xlrd
import pyodbc

def InsertarCiudades(parameter_path):

    Path = str(parameter_path)
    book = xlrd.open_workbook(Path)
    sheet = book.sheet_by_name('cat_ciudad')

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-8LT275E\SQLEXPRESS;'
                          'Database=DB_PYTHON;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    for i in range(1, sheet.nrows):

        Cod_Ciudad = sheet.cell(i, 0).value
        Desc_Ciudad = sheet.cell(i, 1).value
        Desc_Departamento = sheet.cell(i, 2).value
        Desc_Pais = sheet.cell(i, 3).value

        query = '''INSERT INTO CIUDAD (Cod_Ciudad, Desc_Ciudad, Desc_Departamento, Desc_Pais) VALUES (?,?,?,?)'''
        values = (Cod_Ciudad, Desc_Ciudad, Desc_Departamento, Desc_Pais)
        cursor.execute(query, values)
        conn.commit()

    cursor.close()
    conn.close()
    print("Se insertaron : " + str(sheet.nrows - 1) +
          " registros en la tabla CIUDAD")
