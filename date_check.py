import sys
import datetime


def calcular_rango_de_fechas(fecha_inicio, fecha_fin):
  fechas = []
  fecha_inicio_objeto = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d")
  fecha_fin_objeto = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")
  while fecha_inicio_objeto <= fecha_fin_objeto:
    fechas.append(fecha_inicio_objeto.strftime("%Y-%m-%d"))
    fecha_inicio_objeto += datetime.timedelta(days=1)
  return fechas

def obtener_fechas():
  if len(sys.argv) == 3:
    return calcular_rango_de_fechas(sys.argv[1], sys.argv[2])
  else:
    return [get_today()]

def get_today():
  today = datetime.date.today()
  str_today = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
  date_parts = str_today.split("-")
  year = date_parts[0]
  month = date_parts[1]
  day = date_parts[2]
  if len(str(month)) == 1:
      month = "0"+str(month)
  if len(str(day)) == 1:
      day = "0"+str(day)
  return year+"-"+month+"-"+day