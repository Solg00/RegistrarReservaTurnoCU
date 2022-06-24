from select import select
from tkinter import Label, StringVar, ttk,messagebox
import tkinter as tk
from GestorDeCURegReservaDeTurno import GestorDeCURegReservaDeTurno as gestor

class InterfazDeReservaTurno():
    def __init__(self) -> None:
        self.combo_tiposRT = None
        self.grillaRTs = None
        self.button_seleccionarRT = None
        self.labelframe_rtselec = None
        self.label_rtseleccionadoNroInv = None
        self.label_rtseleccionadoModMarca = None
        self.label_rtseleccionadoCI = None
        self.label_rtseleccionadoEstado = None
        self.cell_nroInvRTSeleccionado = None
        self.cell_ModMarcaRTSeleccionado = None
        self.cell_CIRTSeleccionado = None
        self.cell_EstadoRTSeleccionado = None
        self.combo_envioNotif = None

        self.tiposRT = None
        self.tipoRTSeleccionado = None
        self.rTSeleccionado = None
        self.cIDelRT = None
        self.tiposEnvioNotif = None
        self.envioNotifSeleccionado = None
        #Empieza funcionalidad
        self.opcionReservarTurnoRT()

        self.ventana = tk.Tk()
        self.ventana.geometry("900x900")
        self.ventana.title('Registrar Reserva de Turno de Recurso Tecnológico')
        self.ventana.mainloop()

        self.frame = tk.Frame(ventana)
        self.frame.pack()

    #Utils
    def clear_window(self):
        '''Destroy elements of a frame'''
        for widget in self.frame.winfo_children():
            widget.destroy()

    def close_window(self):
        self.ventana.destroy()

    #Métodos de clase
    def opcionReservarTurnoRT(self):
        print("*****Interfaz: opción opcionReservarTurnoRT seleccionada  ******")
        btn_opcionReservarTurnoRT = tk.Button(self.frame,text="Reservar Turno de RT", padx=50, pady= 40, command=self.habilitarInterfaz)
        btn_opcionReservarTurnoRT.pack()


    
    def habilitarInterfaz(self):
        gestor.registrarReservaTurno()
    
    def mostrarTiposRT(self,tiposRT:list):
        self.clear_window()

        self.tiposRT = tiposRT
        tittle = tk.Label(self.frame,text="Seleccione el tipo de Recurso Tecnológico que desee:")
        tittle.pack(side='top')
        self.combo_tiposRT = ttk.Combobox(self.frame,state='readonly',values=self.tiposRT)
        self.combo_tiposRT.pack()
        self.combo_tiposRT.bind("<<ComboboxSelected>>", self.tomarSeleccionTipoRT)
        
    def tomarSeleccionTipoRT(self):
        self.tipoRTSeleccionado= self.combo_tiposRT.get()
        gestor.tomarSeleccionTipoRT(self.tipoRTSeleccionado)

    def mostrarRTs(self, cisRT:dict):
        self.clear_window()

        def fixed_map(option): #Función necesaria para tkinter 8.6>>> y python 3.8
            # Returns the style map for 'option' with any styles starting with
            # ("!disabled", "!selected", ...) filtered out

            # style.map() returns an empty list for missing options, so this should
            # be future-safe
                return [elm for elm in style.map("Treeview", query_opt=option)
                        if elm[:2] != ("!disabled", "!selected")]

        self.grillaRTs = ttk.Treeview(self.frame,columns=(1,2,3,4),show='headings')
        self.grillaRTs.pack()
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
        self.button_seleccionarRT = tk.Button(self.frame,text='Seleccionar Recurso',background='light grey',command=self.tomarSeleccionTipoRT)
        self.button_seleccionarRT.pack(side='bottom',pady=20) 

    def tomarSeleccionRT(self):
        item_selected = self.grillaRTs.focus()
        item_selected = self.grillaRTs.item(item_selected,'values') 
        self.rTSeleccionado = {
            'nroInv': item_selected[1],
            'modMarca' : item_selected[2],
            'estadoActual' : item_selected[3],
        }
        gestor.tomarSeleccionRT(self.rTSeleccionado)


    def mostrarDatosRTSeleccionado(self):
        self.labelframe_rtselec= tk.LabelFrame(self.frame,text='Recurso Tecnológico Seleccionado')
        self.labelframe_rtselec.grid(column=0,row=0)

        #Headers
        self.labelframe_rtselec.pack()
        self.label_rtseleccionadoNroInv = tk.Label(self.labelframe_rtselec, text='Nro Inventario')
        self.label_rtseleccionadoNroInv.grid(row=0,column=0)
        self.label_rtseleccionadoModMarca = tk.Label(self.labelframe_rtselec, text='Modelo y Marca')
        self.label_rtseleccionadoModMarca.grid(row=0,column=1)
        self.label_rtseleccionadoCI = tk.Label(self.labelframe_rtselec, text='Centro De Investigación')
        self.label_rtseleccionadoCI.grid(row=0,column=2)    
        self.label_rtseleccionadoEstado = tk.Label(self.labelframe_rtselec, text='Estado')
        self.label_rtseleccionadoEstado.grid(row=0,column=3)

        sp = ttk.Separator(self.labelframe_rtselec, orient='horizontal')
        sp.grid(row=1,columnspan=4,sticky='ew')
        
        #RT
        self.cell_nroInvRTSeleccionado = tk.Label(self.labelframe_rtselec, textvariable= StringVar(value=self.rTSeleccionado['nroInv']))
        self.cell_nroInvRTSeleccionado.grid(row=2,column=0)
        self.cell_ModMarcaRTSeleccionado = tk.Label(self.labelframe_rtselec, textvariable= StringVar(value=self.rTSeleccionado['modMarca']))
        self.cell_ModMarcaRTSeleccionado.grid(row=2,column=1)
        self.cell_CIRTSeleccionado = tk.Label(self.labelframe_rtselec, textvariable= StringVar(value=self.cIDelRT.nombre))
        self.cell_CIRTSeleccionado.grid(row=2,column=2)
        self.cell_EstadoRTSeleccionado = tk.Label(self.labelframe_rtselec, textvariable= StringVar(value=self.rTSeleccionado['estadoActual']))
        self.cell_EstadoRTSeleccionado.grid(row=2,column=3)
    
        self.mostrarDatosTurnoSeleccionado()


    def mostrarDatosTurnoSeleccionado(self):
        self.labelframe_turno= tk.LabelFrame(self.frame,text='Turno Seleccionado')
        self.labelframe_turno.grid(column=0,row=1)
        #Headers
        self.label_fechaInicioTurnoSelec = tk.Label(self.labelframe_turno, text='Fecha Inicio')
        self.label_fechaInicioTurnoSelec.grid(row=0,column=0)
        self.label_fechaFinTurnoSelec = tk.Label(self.labelframe_turno, text='Fecha Fin')
        self.label_fechaFinTurnoSelec.grid(row=0,column=1)
        
        sp = ttk.Separator(self.labelframe_turno, orient='horizontal')
        sp.grid(row=1,columnspan=2,sticky='ew')

        self.cell_fechaInicioTurnoSelec =  tk.Label(self.labelframe_turno, textvariable= StringVar(value=self.turnoSeleccionado['fechaInicio']))
        self.cell_fechaInicioTurnoSelec.grid(row=2,column=0)
        self.cell_fechaInicioTurnoSelec =  tk.Label(self.labelframe_turno, textvariable= StringVar(value=self.turnoSeleccionado['fechaFin']))
        self.cell_fechaInicioTurnoSelec.grid(row=2,column=1)


    def pedirSeleccionEnvioNotificacion(self,tipoEnvio):
        self.tiposEnvioNotif = tipoEnvio
        self.label_seleccionEnvioNotif = tk.Label(self.frame,text="Seleccione cómo desea que se le envíe la notificación:")
        self.label_seleccionEnvioNotif.grid(row=5,column=0)
        self.combo_envioNotif = ttk.Combobox(self.frame,state='readonly',values=self.tipoEnvioNotif)
        self.combo_envioNotif.grid(row=5,column=1)
        self.combo_envioNotif.bind("<<ComboboxSelected>>", self.tomarSeleccionEnvioNotificacion)


    def tomarSeleccionEnvioNotificacion(self):
        self.envioNotifSeleccionado = self.combo_envioNotif.get()
        gestor.tomarSeleccionEnvioNotificacion(self.envioNotifSeleccionado)

    def pedirConfirmacion(self):
        skip = Label(self.frame,text=' ')
        skip.grid(row=6,column=1)

        self.btn_confirmacion = tk.Button(self.frame,text='Confirmar',background='green',command=self.tomarSeleccionTipoRT)
        self.btn_confirmacion.grid(row=7,column=3)
        self.btn_cancelar = tk.Button(self.frame,text='Cancelar',background='red',command=self.cancelar)
        self.btn_confirmacion.grid(row=7,column=4)

    def tomarConfirmacion(self):
        self.confirmacion = True
        gestor.tomarConfirmacion(self.confirmacion)

    def cancelar(self):
        cancelar = messagebox.askyesno(title='Cancelación de Reserva', message='Desea cancelar su reserva?')
        if cancelar:
            self.confirmacion = False
            gestor.tomarConfirmacion(self.confirmacion)
            print('****CANCELAR****')
            gestor.finCU()
            self.close_window()
 