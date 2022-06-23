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

    def mostrarRTs(self, cisRT:dict):
        def fixed_map(option): #Función necesaria para tkinter 8.6>>> y python 3.8
            # Returns the style map for 'option' with any styles starting with
            # ("!disabled", "!selected", ...) filtered out

            # style.map() returns an empty list for missing options, so this should
            # be future-safe
                return [elm for elm in style.map("Treeview", query_opt=option)
                        if elm[:2] != ("!disabled", "!selected")]

        grillaRTs = ttk.Treeview(self.ventana,columns=(1,2,3,4),show='headings')
        grillaRTs.pack()
        style = ttk.Style()
        style.map("Treeview", 
          foreground=fixed_map("foreground"),
          background=fixed_map("background"))
        
        grillaRTs.heading(1,text='Centro Investigacion')
        grillaRTs.heading(2,text='Nro Inventario')
        grillaRTs.heading(3,text='Modelo y Marca')
        grillaRTs.heading(4,text='Estado')
        grillaRTs.tag_configure('Azul',background='blue')
        grillaRTs.tag_configure('Verde',background='green')
        grillaRTs.tag_configure('Gris',background='grey')
        grillaRTs.tag_configure('CI',background='black',foreground='white')



        CIs = list(cisRT.keys())
        print('cis', CIs)
        for i in range((len(CIs))):
            ci_nombre = CIs[i]  
            print(ci_nombre)
            grillaRTs.insert('',tk.END,values=[ci_nombre,'','',''],tags='CI')
            for rt in cisRT[ci_nombre]:
                print(rt)
                if rt['estadoActual']['color'] == 'Azul':
                    grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Azul'))
                elif rt['estadoActual']['color'] == 'Verde':
                    grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Verde'))
                else: # rt['estadoActual']['color'] == 'Gris':
                    grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Gris'))


    ventana.mainloop()
 