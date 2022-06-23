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

    def mostrarRTs(self, cisRT):
        grillaRTs = ttk.Treeview(self.ventana,columns=(1,2,3,4),show='headings')
        grillaRTs.pack()
        grillaRTs.heading(1,text='Centro Investigacion')
        grillaRTs.heading(2,text='Nro Inventario')
        grillaRTs.heading(3,text='Modelo y Marca')
        grillaRTs.heading(4,text='Estado')
        values = []
        CIs = list(cisRT.keys())
        for i in (len(CIs)-1):
            ci_nombre = CIs[i]            
            for rt in cisRT[ci_nombre]:
                tupla_tittle = (ci_nombre,'','','')
                tupla_rt = ('',cisRT['nroInv'],cisRT['modMarca'],cisRT['estadoActual'])
                values.append(tupla_tittle)
                values.append(tupla_rt)
        #Treeview



    ventana.mainloop()
 