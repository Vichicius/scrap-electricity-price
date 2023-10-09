import tkinter as tk
from tkcalendar import *
from tkinter import *
import ciclo_de_ejecucion

def reformat_date(date_str):
  # Separar día, mes y año
  month, day, year = date_str.split("/")
  # Añadir un cero a la izquierda al mes y al día si son de un solo dígito
  month = month.zfill(2)
  day = day.zfill(2)
  # Si el año es de dos dígitos, añadir los dos primeros dígitos del siglo actual al principio
  if len(year) == 2:
      year = "20" + year
  # Devolver la fecha en el nuevo formato
  return f"{year}-{month}-{day}"

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Generar gráfica del precio horario del mercado diario")
        self.geometry('300x600')
        self.my_label = Label(self, text= "Selecciona el primer día")
        self.my_label.pack(pady=20)
        self.first_calendar = Calendar(self)
        self.first_calendar.pack(pady=0, fill = 'both', expand = True)
        self.my_label = Label(self, text= "Selecciona el último día")
        self.my_label.pack(pady=20)
        self.second_calendar = Calendar(self)
        self.second_calendar.pack(pady=0, fill = 'both', expand = True)
        self.button = tk.Button(self, text="Ejecutar programa", command=self.on_button)
        self.button.pack(pady=20)

    def on_button(self):
        primer_dia = reformat_date(self.first_calendar.get_date())
        segundo_dia = reformat_date(self.second_calendar.get_date())
        rango_de_fechas = ["",primer_dia, segundo_dia]
        # Aquí puedes poner el código para ejecutar tu programa Python
        print(rango_de_fechas)
        ciclo_de_ejecucion.execute(rango_de_fechas)
        pass

if __name__ == "__main__":
  app = App()
  app.mainloop()


# from tkinter import *
# from tkcalendar import *

# root = Tk()
# root.title("Prueba")
# root.geometry('500x500')


# cal = Calendar(root, selectmode="day", year=2023, month=1, day=8)
# cal.pack(pady=20)

# def grab_date():
#   my_label.config(text=cal.get_date())

# my_button = Button(root, text= "Get date", command=grab_date)
# my_button.pack(pady=20)


# my_label = Label(root, text= "")
# my_label.pack(pady=20)




# root.mainloop()


