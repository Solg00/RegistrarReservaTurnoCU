from TipoRecursoTecnologico import TipoRecursoTecnologico
from CambioEstadoRT import CambioEstadoRT
from Estado import Estado
from RecursoTecnologico import RecursoTecnologico

estadoDisponibleRt = Estado("Disponible", "Esta disponible", "RT", True, False)
estadoMantenimientoRt = Estado("Mantenimiento", "Esta en Mantenimiento", "RT", False, False)
tipo1= TipoRecursoTecnologico("Varios","Dispositivos varios...")


rt1= RecursoTecnologico(1, "imagen.png", 0,  20, 22, 'mod1', tipo1, [CambioEstadoRT(estadoDisponibleRt),CambioEstadoRT(estadoMantenimientoRt)],[])

def buscarRT(recursosTecnologicos,tipoRTSeleccionado):
    for rt in recursosTecnologicos:
        rtest = rt.buscarEstadoActual()
        if rt.sosRTDelTipoSeleccionado(tipoRTSeleccionado) and rtest.esReservable():
            print( rtest.esReservable())
            print(True)



buscarRT([rt1],tipo1)