from datetime import datetime
from datetime import date
from Turno import *
from Estado import *
from CambioDeEstadoTurno import *
import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk
from tkinter.messagebox import showinfo
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
turno22 = Turno(datetime.now(), 4, datetime(2022, 6, 23, 12, 15, 0), datetime(2022, 6, 23, 12, 45, 0), [cambioEstadoDisponible])

# Con estado pendiente...
turno33 = Turno(datetime.now(), 4, datetime(2022, 6, 24, 12, 30, 0), datetime(2022, 6, 23, 13, 30, 0), [cambioEstadoPendiente])

# Turnos del dia 24
# Con estado pendiente...
turno3 = Turno(datetime.now(), 4, datetime(2022, 6, 24, 12, 30, 0), datetime(2022, 6, 24, 13, 30, 0), [cambioEstadoPendiente])

# Turnos del dia 25
#Disponible
turno4 = Turno(datetime.now(), 4, datetime(2022, 6, 25, 12, 30, 0), datetime(2022, 6, 25, 13, 30, 0), [cambioEstadoDisponible])
# Reservado
turno5 = Turno(datetime.now(), 4, datetime(2022, 6, 25, 12, 30, 0), datetime(2022, 6, 25, 13, 30, 0), [cambioEstadoReservado])

turnos = []

# for i in range(30):
#     turno6 = Turno(datetime.now(), 4, datetime(2022, 6, i + 1, 12, 30, 0), datetime(2022, 6, 25, 13, 30, 0), [cambioEstadoDisponible])
#     turnos.append(turno6)

turnos.append(turno5)
turnos.append(turno4)
turnos.append(turno1)
turnos.append(turno2)
turnos.append(turno3)
turnos.append(turno33)
turnos.append(turno22)

turnosAgrupados = agruparTurnos(turnos)
turnosPorColor = asignarColorTurnoXDisp(turnos)


# >>>> mostrarTurnos()

ventana = tk.Tk()


def mostrarTurnos(turnos, turnosColor):

    cal = Calendar(ventana, selectbackground="green", normalbackground="red", weekendbackground="red")
    for fecha in turnos.keys():
        for turno in turnos[fecha]:
            if turno.buscarEstadoActual().estado.getNombre() == "Disponible":
                cal.calevent_create(fecha, "", tags="ConTurnos")

    cal.tag_config("ConTurnos", background="blue")
    cal.pack()

    def mostrarTurnosDeFecha():
        date1 = cal.get_date().split("/")
        date1 = [int(a) for a in date1]
        fechaSeleccionada = date(day=date1[1], month=date1[0], year=date1[2] + 2000)
        for turno in turnos[fechaSeleccionada]:
            if turno in turnosPorColor["Azul"]:
                lblAzul = tk.Label(ventana,
                                   text="Hora Inicio: " + turno.fechaHoraInicio.time().strftime("%H:%M") +
                                   "    Hora Fin: " + turno.fechaHoraFin.time().strftime("%H:%M"), background="blue")
                lblAzul.pack()
            if turno in turnosPorColor["Rojo"]:
                lblRojo = tk.Label(ventana,
                                   text="Hora Inicio: " + turno.fechaHoraInicio.time().strftime("%H:%M") +
                                   "    Hora Fin: " + turno.fechaHoraFin.time().strftime("%H:%M"), background="red")
                lblRojo.pack()
            if turno in turnosPorColor["Gris"]:
                lblGris = tk.Label(ventana,
                                   text="Hora Inicio: " + turno.fechaHoraInicio.time().strftime("%H:%M") +
                                   "    Hora Fin: " + turno.fechaHoraFin.time().strftime("%H:%M"), background="grey")
                lblGris.pack()


    # TODO: Permitir seleccion solo de los diponibles
    btnSeleccionarFecha = tk.Button(ventana, text="Seleccionar Fecha", command=mostrarTurnosDeFecha, background="orange")
    btnSeleccionarFecha.pack()





    ventana.mainloop()


mostrarTurnos(turnosAgrupados, turnosPorColor)
