from tkinter import ttk
import tkinter as tk
from turtle import title
from GestorDeCURegReservaDeTurno import GestorDeCURegReservaDeTurno as gestor

class InterfazDeReservaTurno():
    def __init__(self) -> None:
        self.combo_tiposRT = None

    ventana = tk.Tk()
    ventana.geometry("900x900")
    ventana.title('Caso de Uso 23: Registrar Reserva de Turno de Recurso Tecnológico')
    btn_opcionReservarTurnoRT = tk.Button(ventana,text="Reservar Turno de RT", padx=50, pady= 40, command=opcionReservarTurnoRT)
    btn_opcionReservarTurnoRT.pack()

    def opcionReservarTurnoRT(self):
        print("*****Interfaz: opción opcionReservarTurnoRT seleccionada  ******")
        self.habilitarInterfaz()

    
    def habilitarInterfaz():
        gestor.registrarReservaTurno()
    
    def mostrarTiposRT(self,tiposRT:list):
        tittle = tk.Label(self.ventana,text="Seleccione el tipo de Recurso Tecnológico que desee:")
        tittle.pack(side='top')
        self.combo_tiposRT = ttk.Combobox(self.ventana,state='readonly',values=tiposRT)
        self.combo_tiposRT.place(x=50, y=50)
        self.combo_tiposRT.bind("<<ComboboxSelected>>", self.tomarSeleccionTipoRT)
        
    def tomarSeleccionTipoRT(self):
        tipoRTSeleccionado= self.combo_tiposRT.get()
        gestor.tomarSeleccionTipoRT(tipoRTSeleccionado)

    ventana.mainloop()
 