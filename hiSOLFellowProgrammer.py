from tkinter import ttk
import tkinter as tk




cisRT = {'UTN FRC': [{'nroInv': 12123, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'Disponible','color':'Azul'}},
{'nroInv': 21312, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'otro','color':'Gris'}}],'UTN FRBA': [{'nroInv': 12123, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'Disponible','color':'Azul'}},
{'nroInv': 21312, 'modMarca': '1-Philco', 'estadoActual':{'nombre':'otro','color':'Gris'}}]}



def mostrar(cisRT):
    def fixed_map(option):
    # Returns the style map for 'option' with any styles starting with
    # ("!disabled", "!selected", ...) filtered out

    # style.map() returns an empty list for missing options, so this should
    # be future-safe
        return [elm for elm in style.map("Treeview", query_opt=option)
                if elm[:2] != ("!disabled", "!selected")]
    def pedirSeleccionDeRT():
        button_seleccionarRT = tk.Button(ventana,text='Seleccionar Recurso',background='light grey', command=tomarSeleccionTipoRT)
        button_seleccionarRT.pack(side='bottom',pady=20) 

    def tomarSeleccionTipoRT():
     a = grillaRTs.focus()
     b = grillaRTs.item(a,'values')
     print(b[1])
    ventana = tk.Tk()
    grillaRTs = ttk.Treeview(ventana,columns=(1,2,3,4),show='headings')
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

    #grillaRTs.insert('',tk.END,values=['UTN FRC','','',''])
    #grillaRTs.insert('',tk.END, values=('',cisRT['UTN FRC'][0]["nroInv"],cisRT['UTN FRC'][0]["modMarca"],cisRT['UTN FRC'][0]["estadoActual"]['nombre']),tags='Azul')
    #grillaRTs.insert('',tk.END, values=('',cisRT['UTN FRC'][1]["nroInv"],cisRT['UTN FRC'][1]["modMarca"],cisRT['UTN FRC'][1]["estadoActual"]['nombre']),tags='Gris')

    CIs = list(cisRT.keys())
    print('cis', CIs)
    for i in range((len(CIs))):
        ci_nombre = CIs[i]  
        print(ci_nombre)
        grillaRTs.insert('',tk.END,values=[ci_nombre,'','',''],tags=('CI'))
        for rt in cisRT[ci_nombre]:
            print(rt)
            if rt['estadoActual']['color'] == 'Azul':
                grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Azul'))
            elif rt['estadoActual']['color'] == 'Verde':
                grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Verde'))
            else: # rt['estadoActual']['color'] == 'Gris':
                grillaRTs.insert('', tk.END, values=['',rt['nroInv'],rt['modMarca'],rt['estadoActual']['nombre']],tags=('Gris'))
    pedirSeleccionDeRT()

    ventana.mainloop()

mostrar(cisRT)