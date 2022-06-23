from datetime import datetime
from datetime import date
from Turno import *
from Estado import *
from CambioDeEstadoTurno import *
# listaNotas = [10]
# dic = {"Nico" : listaNotas,
#        "Caro" : [9],
#        "Diego": [8]}
#
# dic["Nico"].append(9)
# print(dic)
# >>> Metodos del gestor


def agruparTurnos(turnos):
        turnosAgrupados = {}
        for turno in turnos:
            turnosDia = []
            fechaTurno = turno.fechaHoraInicio.date()
            fechas = turnosAgrupados.keys()
            if fechaTurno not in fechas:
                turnosAgrupados[fechaTurno] = turnosDia
                turnosAgrupados[fechaTurno].append(turno)
            else:
                turnosAgrupados[fechaTurno].append(turno)
        return turnosAgrupados


def asignarColorTurnoXDisp(turnos):
        turnosPorColor = {"Azul": [],
                          "Gris": [],
                          "Rojo": []}

        for turno in turnos:
            print(turno.cambiosDeEstadoTurno[-1].estado.getNombre())
            estadoTurno = turno.cambiosDeEstadoTurno[-1].estado.getNombre()
            if estadoTurno == "Disponible":
                turnosPorColor["Azul"].append(turno)
            if estadoTurno == "Con reserva pendiente de confirmacion":
                turnosPorColor["Gris"].append(turno)
            if estadoTurno == "Reservado":
                turnosPorColor["Rojo"].append(turno)

        return turnosPorColor


# >>> ESTADOS
estadoDisponible = Estado("Disponible", "Esta disponible", "Turno", True, False)
estadoReservado = Estado("Reservado", "Esta reservado", "Turno", False, True)
estadoPendiente = Estado("Con reserva pendiente de confirmacion", "Pendiente", "Turno", False, True)

# >>> Cambios de estado
cambioEstadoDisponible = CambioDeEstadoTurno(estadoDisponible)
cambioEstadoReservado = CambioDeEstadoTurno(estadoReservado)
cambioEstadoPendiente = CambioDeEstadoTurno(estadoPendiente)


# Turnos del dia 23
# Reservado
turno1 = Turno(datetime.now(), 4, datetime(2022, 6, 23, 10, 30, 0), datetime(2022, 6, 23, 10, 30, 0), [cambioEstadoReservado])
# Disponible
turno2 = Turno(datetime.now(), 4, datetime(2022, 6, 23, 11, 15, 0), datetime(2022, 6, 23, 12, 0, 0), [cambioEstadoDisponible])

# Turnos del dia 24
# Con estado pendiente...
turno3 = Turno(datetime.now(), 4, datetime(2022, 6, 24, 12, 30, 0), datetime(2022, 6, 24, 13, 30, 0), [cambioEstadoPendiente])

# Turnos del dia 25
#Disponible
turno4 = Turno(datetime.now(), 4, datetime(2022, 6, 25, 12, 30, 0), datetime(2022, 6, 25, 13, 30, 0), [cambioEstadoDisponible])
# Reservado
turno5 = Turno(datetime.now(), 4, datetime(2022, 6, 25, 12, 30, 0), datetime(2022, 6, 25, 13, 30, 0), [cambioEstadoReservado])

turnos = []
turnos.append(turno5)
turnos.append(turno4)
turnos.append(turno1)
turnos.append(turno2)
turnos.append(turno3)

turnosAgrupados = agruparTurnos(turnos)
turnosPorColor = asignarColorTurnoXDisp(turnos)

for key in 

