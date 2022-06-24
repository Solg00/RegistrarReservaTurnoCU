from datetime import datetime
from datetime import date
from Turno import *
from Estado import *
from CambioDeEstadoTurno import *
import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk
from tkinter.messagebox import showinfo
from functools import partial
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


class Main():
    def __init__(self) -> None:
        self.ventana = tk.Tk()

        self.cal = None
        self.btnPedirSeleccionTurno = None
        self.turnoSeleccionado = None

    def tomarSeleccionTurno(self, turnoSelect):
                self.turnoSeleccionado = turnoSelect
                lblTurno = tk.Label(self.ventana, text= turnoSelect.fechaHoraInicio)
                lblTurno.grid(row=6, column=0)

    def pedirSeleccionDeTurno(self, turnos, turnosColor):
        for widget in self.ventana.winfo_children():
            if widget == self.cal or widget == self.btnPedirSeleccionTurno:
                continue
            widget.destroy()

        date1 = self.cal.get_date().split("/")
        date1 = [int(a) for a in date1]
        fechaSeleccionada = date(day=date1[1], month=date1[0], year=date1[2] + 2000)
        column = 2
        for turno in turnos[fechaSeleccionada]:
            column += 1
            if turno in turnosColor["Azul"]:
                lblAzul = tk.Label(self.ventana,
                                   text="Hora Inicio: " + turno.fechaHoraInicio.time().strftime("%H:%M") +
                                   "    Hora Fin: " + turno.fechaHoraFin.time().strftime("%H:%M"), background="blue")
                lblAzul.grid(row=column, column=0)
                btnReservar = tk.Button(self.ventana, text="Reservar", command=partial(self.tomarSeleccionTurno, turno))
                btnReservar.grid(row=column, column=1)
            if turno in turnosColor["Rojo"]:
                lblRojo = tk.Label(self.ventana,
                                   text="Hora Inicio: " + turno.fechaHoraInicio.time().strftime("%H:%M") +
                                   "    Hora Fin: " + turno.fechaHoraFin.time().strftime("%H:%M"), background="red")
                lblRojo.grid(row=column, column=0)
            if turno in turnosColor["Gris"]:
                lblGris = tk.Label(self.ventana,
                                   text="Hora Inicio: " + turno.fechaHoraInicio.time().strftime("%H:%M") +
                                   "    Hora Fin: " + turno.fechaHoraFin.time().strftime("%H:%M"), background="grey")
                lblGris.grid(row=column, column=0)


    def mostrarTurnos(self, turnos, turnosColor):

        self.cal = Calendar(self.ventana, selectbackground="green", normalbackground="red", weekendbackground="red")
        self.cal.grid(row=0, column=0, columnspan=2)

        for fecha in turnos.keys():
            for turno in turnos[fecha]:
                if turno.buscarEstadoActual().estado.getNombre() == "Disponible":
                    self.cal.calevent_create(fecha, "", tags="ConTurnos")

        self.cal.tag_config("ConTurnos", background="blue")

        # TODO: Permitir seleccion solo de los diponibles
        self.btnPedirSeleccionTurno = tk.Button(self.ventana, text="Seleccionar Fecha", command=partial(self.pedirSeleccionDeTurno, turnos, turnosColor), background="orange")
        self.btnPedirSeleccionTurno.grid(row=2, column=0, columnspan=2)


if __name__ == '__main__':
    main = Main()
    main.mostrarTurnos(turnosAgrupados, turnosPorColor)
    main.ventana.mainloop()
