"""HELLO BUDDY! You might use this module to run some tests or leave comments for your fellow Programmers to see"""

from tkinter import *
from tkinter import ttk



root = Tk()
frame = Frame(root)
frame.pack()
def mostrarDatosRTSeleccionado(rTSeleccionado,cIDelRT):
    labelframe_rtselec= LabelFrame(frame,text='Recurso Tecnológico Seleccionado')
    #Headers
    labelframe_rtselec.grid(row=0,column=0)
    label_rtseleccionadoNroInv = Label(labelframe_rtselec, text='Nro Inventario')
    label_rtseleccionadoNroInv.grid(row=1,column=0)
    label_rtseleccionadoModMarca = Label(labelframe_rtselec, text='Modelo y Marca')
    label_rtseleccionadoModMarca.grid(row=1,column=1)
    label_rtseleccionadoCI = Label(labelframe_rtselec, text='Centro De Investigación')
    label_rtseleccionadoCI.grid(row=1,column=2)
    label_rtseleccionadoEstado = Label(labelframe_rtselec, text='Estado')
    label_rtseleccionadoEstado.grid(row=1,column=3)

    sp = ttk.Separator(labelframe_rtselec, orient='horizontal')
    sp.grid(row=1,columnspan=4,sticky='ew')
    
    cell_nroInvRTSeleccionado = rTSeleccionado['nroInv']
    cell_nroInvRTSeleccionado.grid(row=2,column=0)
    cell_ModMarcaRTSeleccionado = rTSeleccionado['modMarca']
    cell_ModMarcaRTSeleccionado.grid(row=2,column=1)
    cell_CIRTSeleccionado = cIDelRT.nombre
    cell_CIRTSeleccionado.grid(row=2,column=2)
    cell_EstadoRTSeleccionado = rTSeleccionado['estadoActual']
    cell_EstadoRTSeleccionado.grid(row=2,column=3)

root.mainloop()