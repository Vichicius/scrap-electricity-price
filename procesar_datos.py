import date_check


def processData():
  processed_data = []
  # Abrir el archivo y leer su contenido línea por línea
  fechas = date_check.obtener_fechas()
  for i in range(len(fechas)):
    with open("datos/"+fechas[i]+".txt", "r") as f:
        datos = f.readlines()

    # Inicializar el array de precios
    preciosESP = []
    preciosPT = []
    energiaMercadoDiario = []
    energiaMercadoIbericoBilaterales = []

    # Iterar sobre cada línea
    for linea in datos:
      # Dividir la línea en una lista de palabras
      palabras = linea.split(";")
      
      # Si la primera palabra es "Precio marginal en el sistema español (EUR/MWh)",
      # significa que la siguiente línea contiene los precios que estamos buscando
      if palabras[0] == "Precio marginal en el sistema español (EUR/MWh)" or palabras[0] == "Precio marginal en el sistema espaÃ±ol (EUR/MWh)":
        # Iterar sobre cada palabra de la línea y convertirla a un número
        for p in palabras[1:]:
          try:
            precio = float(p.replace(',', '.'))
            preciosESP.append(precio)
          except ValueError:
            # Saltear palabras que no sean números
            pass
      
      #Portugal
      if palabras[0] == "Precio marginal en el sistema portugués (EUR/MWh)" or palabras[0] == 'Precio marginal en el sistema portuguÃ©s (EUR/MWh)':
        # Iterar sobre cada palabra de la línea y convertirla a un número
        for p in palabras[1:]:
          try:
            precio = float(p.replace(',', '.'))
            preciosPT.append(precio)
          except ValueError:
            # Saltear palabras que no sean números
            pass

      #energiaMercadoDiario
      if palabras[0] == "Energía total del mercado Ibérico (MWh)" or palabras[0] == 'Energía total del mercado Ibérico (MWh)':
        # Iterar sobre cada palabra de la línea y convertirla a un número
        for p in palabras[1:]:
          try:
            precio = float(p.replace(',', '.'))
            energiaMercadoDiario.append(precio)
          except ValueError:
            # Saltear palabras que no sean números
            pass
      
      #energiaMercadoIbericoBilaterales
      if palabras[0] == "Energía total con bilaterales del mercado Ibérico (MWh)" or palabras[0] == 'Energía total con bilaterales del mercado Ibérico (MWh)':
        # Iterar sobre cada palabra de la línea y convertirla a un número
        for p in palabras[1:]:
          try:
            precio = float(p.replace(',', '.'))
            energiaMercadoIbericoBilaterales.append(precio)
          except ValueError:
            # Saltear palabras que no sean números
            pass

    precios = {}
    precios["España"] = preciosESP
    precios["Portugal"] = preciosPT
    precios["EnergiaMercadoDiario"] = energiaMercadoDiario
    precios["EnergiaMercadoIbericoBilaterales"] = energiaMercadoIbericoBilaterales
    # Mostrar el array de precios
    print(precios)
    
    processed_data.append(precios)
  return processed_data
