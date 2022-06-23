from tkinter import Label, ttk
import tkinter as tk
from GestorDeCURegReservaDeTurno import GestorDeCURegReservaDeTurno as gestor

class InterfazDeReservaTurno():
    def __init__(self) -> None:
        self.combo_tiposRT = None
        self.grillaRTs = None
        self.rTSeleccionado = None
    ventana = tk.Tk()
    ventana.geometry("900x900")
    ventana.title('Caso de Uso 23: Registrar Reserva de Turno de Recurso Tecnológico')
    btn_opcionReservarTurnoRT = tk.Button(ventana,text="Reservar Turno de RT", padx=50, pady= 40, command=self.opcionReservarTurnoRT)
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

        self.self.grillaRTs = ttk.Treeview(self.ventana,columns=(1,2,3,4),show='headings')
        self.self.grillaRTs.pack()
        style = ttk.Style()
        style.map("Treeview", 
          foreground=fixed_map("foreground"),
          background=fixed_map("background"))
        
        self.grillaRTs.heading(1,text='Centro Investigacion')
        self.grillaRTs.heading(2,text='Nro Inventario')
        self.grillaRTs.heading(3,text='Modelo y Marca')
        self.grillaRTs.heading(4,text='Estado')
        self.grillaRTs.tag_configure('Azul',background='blue')
        self.grillaRTs.tag_configure('Verde',background='green')
        self.grillaRTs.tag_configure('Gris',background='grey')
        self.grillaRTs.tag_configure('CI',background='black',foreground='white')



        CIs = list(cisRT.keys())
        print('cis', CIs)
        for i in range((len(CIs))):
            ci_nombre = CIs[i]  
            print(ci_nombre)
            self.grillaRTs.insert('',tk.END,values=[ci_nombre,'','',''],tags='CI')
            for rt in cisRT[ci_nombre]:
                print(rt)
                if rt['estadoActual']['color'] == 'Azul':
                    self.grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Azul'))
                elif rt['estadoActual']['color'] == 'Verde':
                    self.grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Verde'))
                else: # rt['estadoActual']['color'] == 'Gris':
                    self.grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Gris'))
        self.pedirSeleccionDeRT()
    def pedirSeleccionDeRT(self):
        button_seleccionarRT = tk.Button(self.ventana,text='Seleccionar Recurso',background='light grey',command=self.tomarSeleccionTipoRT)
        button_seleccionarRT.pack(side='bottom',pady=20) 

    def tomarSeleccionRT(self):
        item_selected = self.grillaRTs.focus()
        item_selected = self.grillaRTs.item(item_selected,'values') 
        self.rTSeleccionado = {
            'nroInv': item_selected[1],
            'modMarca' : item_selected[2],
            'estadoActual' : item_selected[3],
        }
        gestor.tomarSeleccionRT(self.rTSeleccionado)
    ventana.mainloop()
 