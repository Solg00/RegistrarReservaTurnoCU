from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar

import datetime


cisRT = {'UTN FRC': [{'nroInv': 12123, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'Disponible','color':'Azul'}},
{'nroInv': 21312, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'otro','color':'Gris'}}],'UTN FRBA': [{'nroInv': 12123, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'Disponible','color':'Azul'}},
{'nroInv': 21312, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'otro','color':'Gris'}}]}



def mostrar(cisRT):
   pass

ws = tk.Tk()
cal = Calendar(ws)
cal.pack()
day = datetime.date(2022, 6, 30)
cal.calevent_create(day, "", tags="hi")
cal.tag_config("hi", background="red")
ws.mainloop()