from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar

import datetime


cisRT = {'UTN FRC': [{'nroInv': 12123, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'Disponible','color':'Azul'}},
{'nroInv': 21312, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'otro','color':'Gris'}}],'UTN FRBA': [{'nroInv': 12123, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'Disponible','color':'Azul'}},
{'nroInv': 21312, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'otro','color':'Gris'}}]}


tiposrt = ['micro','macro']

def clear_window():
    '''Destroy elements of a frame'''
    for widget in frame.winfo_children():
            widget.destroy()
            
def opcionReservarTurnoRT():
    print("*****Interfaz: opción opcionReservarTurnoRT seleccionada  ******")
    btn_opcionReservarTurnoRT = tk.Button(frame,text="Reservar Turno de RT", padx=50, pady= 40, command=habilitarInterfaz)
    btn_opcionReservarTurnoRT.pack()



def habilitarInterfaz():
    mostrarTiposRT(tiposrt)

def mostrarTiposRT(tiposRT:list):
        clear_window()
        tiposRT = tiposRT
        tittle = tk.Label(frame,text="Seleccione el tipo de Recurso Tecnológico que desee:")
        tittle.pack(side='top')
        combo_tiposRT = ttk.Combobox(frame,state='readonly',values=tiposRT)
        combo_tiposRT.pack()
        combo_tiposRT.bind("<<ComboboxSelected>>", tomarSeleccionTipoRT)

        def tomarSeleccionTipoRT():
            tipoRTSeleccionado= combo_tiposRT.get()
            print(tipoRTSeleccionado)


ventana = tk.Tk()
ventana.geometry("900x900")
ventana.title('Registrar Reserva de Turno de Recurso Tecnológico')


frame = tk.Frame(ventana)
frame.pack()
opcionReservarTurnoRT()

ventana.mainloop()
