"""HELLO BUDDY! You might use this module to run some tests or leave comments for your fellow Programmers to see"""

from tkinter import *
from tkinter import ttk,messagebox
from CentroDeInvestigacion import CentroDeInvestigacion


rt ={'nroInv':1231312,'modMarca':'Modelo12321-12312', 'estadoActual':'Disponible'}
ci1= CentroDeInvestigacion("Mecanica","MEC","Av. avenida 500","Edificio1",1,"22.55.60","ej@gm.com",50058,'',"reglamento","cracteristicas generales",22,None,None,[],[])
tiposenv = ['WSP','EMAIL']
turnoSeleccionado = {'fechaInicio': '1/2/2022','fechaFin': '5/2/2022'}
root = Tk()
frame = Frame(root)
frame.pack()
def cerrar():
    root.destroy()
def mostrarDatosRTSeleccionado(rTSeleccionado,cIDelRT):
    labelframe_rtselec= LabelFrame(frame,text='Recurso Tecnológico Seleccionado')
    #Headers
    labelframe_rtselec.grid(column=0,row=0)
    sp = ttk.Separator(frame, orient='horizontal')
    label_rtseleccionadoNroInv = Label(labelframe_rtselec, text='Nro Inventario')
    label_rtseleccionadoNroInv.grid(row=0,column=0)
    label_rtseleccionadoModMarca = Label(labelframe_rtselec, text='Modelo y Marca')
    label_rtseleccionadoModMarca.grid(row=0,column=1)
    label_rtseleccionadoCI = Label(labelframe_rtselec, text='Centro De Investigación')
    label_rtseleccionadoCI.grid(row=0,column=2)
    label_rtseleccionadoEstado = Label(labelframe_rtselec, text='Estado')
    label_rtseleccionadoEstado.grid(row=0,column=3)

    sp = ttk.Separator(labelframe_rtselec, orient='horizontal')
    sp.grid(row=1,columnspan=4,sticky='ew')
    
    cell_nroInvRTSeleccionado =Label(labelframe_rtselec,textvariable=StringVar(value=cIDelRT.nombre))
    cell_nroInvRTSeleccionado.grid(row=3,column=0)

def cancelar():
    cancelar = messagebox.askyesno(title='Cancelación de Reserva', message='Desea cancelar su reserva?')
    print(cancelar)
    if cancelar:
        cerrar()
        
def pedirConfirmacion():
    skip = Label(frame,text=' ')
    skip.grid(row=6,column=1)
    btn_confirmacion = Button(frame,text='Confirmar',background='green')
    btn_confirmacion.grid(row=7,column=3)
    btn_cancelar = Button(frame,text='Cancelar',background='red',command=cancelar)
    btn_cancelar.grid(row=7,column=4)

def pedirSeleccionEnvioNotificacion(tipoEnvio):
    tipoEnvioNotif = tipoEnvio
    label_seleccionEnvioNotif = Label(frame,text="Seleccione cómo desea que se le envíe la notificación:")
    label_seleccionEnvioNotif.grid(row=5,column=0)
    combo_envioNotif = ttk.Combobox(frame,state='readonly',values=tipoEnvioNotif)
    combo_envioNotif.grid(row=5,column=1)
    #combo_envioNotif.bind("<<ComboboxSelected>>", tomarSeleccionTipoRT)


def mostrarDatosTurnoSeleccionado(turnoSeleccionado):
    labelframe_turno= LabelFrame(frame,text='Turno Seleccionado')
    labelframe_turno.grid(column=0,row=2)

    #Headers
    label_fechaInicioTurnoSelec = Label(labelframe_turno, text='Fecha Inicio')
    label_fechaInicioTurnoSelec.grid(row=0,column=0)
    label_fechaFinTurnoSelec = Label(labelframe_turno, text='Fecha Fin')
    label_fechaFinTurnoSelec.grid(row=0,column=1)
    
    sp = ttk.Separator(labelframe_turno, orient='horizontal')
    sp.grid(row=1,columnspan=2,sticky='ew')

    cell_fechaInicioTurnoSelec =  Label(labelframe_turno, textvariable= StringVar(value=turnoSeleccionado['fechaInicio']))
    cell_fechaInicioTurnoSelec.grid(row=2,column=0)
    cell_fechaInicioTurnoSelec =  Label(labelframe_turno, textvariable= StringVar(value=turnoSeleccionado['fechaFin']))
    cell_fechaInicioTurnoSelec.grid(row=2,column=1)

mostrarDatosRTSeleccionado(rt,ci1)
mostrarDatosTurnoSeleccionado(turnoSeleccionado)
pedirSeleccionEnvioNotificacion(tiposenv)
pedirConfirmacion()
root.mainloop()