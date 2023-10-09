from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference, Series, LineChart
import date_check


def generateExcel(data_list):
    fechas = date_check.obtener_fechas()
    dias = len(data_list)

    wb = Workbook()
    sheet = wb.active

    titulos = ["Hora", "Precio marginal español", "Precio marginal portugués", "Energía negociada Mercado Diario", "Energía Mercado Ibérico incluyendo bilaterales"]
    hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]*dias

    precioEspaña = []
    precioPortugal = []
    energiaDiario = []
    energiaBilateral = []

    for x in data_list:
        precioEspaña = precioEspaña + x["España"]
        precioPortugal = precioPortugal + x["Portugal"]
        energiaDiario = energiaDiario + x["EnergiaMercadoDiario"]
        energiaBilateral = energiaBilateral + x["EnergiaMercadoIbericoBilaterales"]

    sheet.append(titulos)
    for i in range(len(hours)):
        sheet.append([hours[i], precioEspaña[i], precioPortugal[i], energiaDiario[i], energiaBilateral[i]])


    maximum_row = 1 + (24*dias)
    # # Crear la primera gráfica (precio barras)
    # Crea la gráfica de barra con los 2 datos de precios 
    chartBar = BarChart()
    chartBar.title = "Precio horario del mercado diario"
    chartBar.y_axis.title = "EUR/MWh"
    chartBar.y_axis.axId = 200

    #Recoger datos del eje Y
    datosPrecios = Reference(sheet, min_col=2, min_row=1, max_col=3, max_row=maximum_row)
    #Añadir eje Y
    chartBar.add_data(datosPrecios, titles_from_data=True)



    # # Crear la segunda gráfica (energía lineas)
    # Crea la gráfica de línea con los 2 datos de energías 
    chartLine = LineChart()
    chartLine.y_axis.title = "MWh"
    chartLine.y_axis.crosses = "max" #mover el eje y a la derecha del todo

    #Recoger datos del eje Y
    datosPrecios = Reference(sheet, min_col=4, min_row=1, max_col=5, max_row=maximum_row)
    #Añadir eje Y
    chartLine.add_data(datosPrecios, titles_from_data=True)



    # #Recoger datos del eje X
    horas = Reference(sheet, min_col=1, min_row=2, max_row=maximum_row)
    #Añadir eje X
    chartBar.x_axis.title = "Hora"
    chartBar.set_categories(horas)


    chartBar += chartLine



    # #Añadir la grafica a la hoja y generarla
    sheet.add_chart(chartBar, "G3")
    
    wb.save("Precio-horario-del-mercado-diario.xlsx")


    