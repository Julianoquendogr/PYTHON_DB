import ciudad
import zona
import genero
import tipo_doc
import sucursal
import clientes
from datetime import datetime 

print("Starts at : " + str(datetime.now()))
Path = 'C:\\Users\\Julian\\Downloads\\TABLAS_PRUEBA_ING_DATOS.xlsx'

ciudad.InsertarCiudades(Path)
zona.InsertarZona(Path)
genero.InsertarGenero()
tipo_doc.InsertarTipo_Doc(Path)
sucursal.InsertarSucursal(Path)
clientes.InsertarClientes(Path)

print("Ends at : " + str(datetime.now()))
