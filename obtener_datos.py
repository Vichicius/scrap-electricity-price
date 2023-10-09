import requests
import date_check
from datetime import date


def getHTML(URLs):
    html_list = []
    for website in URLs:
        consultaServidor = requests.get(website)
        html = consultaServidor.text
        html_list.append(html)
    return html_list

def getURLs(dates):
    websites = []
    for date in dates:
        date_parts = date.split("-")
        year = date_parts[0]
        month = date_parts[1]
        day = date_parts[2]
        if len(str(month)) == 1:
            month = "0"+str(month)
        if len(str(day)) == 1:
            day = "0"+str(day)

        website = "https://www.omie.es/sites/default/files/dados/AGNO_"+year+"/MES_"+month+"/TXT/INT_PBC_EV_H_1_"+day+"_"+month+"_"+year+"_"+day+"_"+month+"_"+year+".TXT"
        websites.append(website)
    return websites

def updateData(data_list):
    fechas = date_check.obtener_fechas()
    for i in range(len(data_list)):
        with open("datos/"+fechas[i]+".txt", "w") as archivo:
            archivo.write(data_list[i])