from datetime import date
from datetime import datetime
import re

string = '19950204'
año = string[0:4]
mes = string[4:6]
dia = string[6:8]
Fecha = año + '-' + mes + '-' +dia

#Día actual
today = date.today()
datetime_object = datetime.strptime(Fecha, '%Y-%m-%d').date()
años = ((today - datetime_object) / 365.25)
años = re.sub('[^0-9]', '', str(años))
print(int(años[0:2]) )