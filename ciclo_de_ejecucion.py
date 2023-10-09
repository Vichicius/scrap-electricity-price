import obtener_datos
import procesar_datos
import generar_grafica_en_excel
import date_check
import sys

def execute(rango_de_fechas):
  sys.argv = rango_de_fechas
  #Obtener array de fechas para conseguir los datos
  dates = date_check.obtener_fechas()
          
  #Obtener la URL de los datos de los dias indicados
  URLs = obtener_datos.getURLs(dates)

  #Guardar los datos de la URL anterior en un fichero
  rawdata = obtener_datos.getHTML(URLs)
  obtener_datos.updateData(rawdata)

  #Extraer los datos de las 4 graficas a construir
  data_list = procesar_datos.processData()

  #Generar grafica de lineas con los datos
  generar_grafica_en_excel.generateExcel(data_list)