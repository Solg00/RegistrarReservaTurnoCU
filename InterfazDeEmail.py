from tkinter import messagebox
from Turno import Turno
from datetime import date
from datetime import datetime

class InterfazDeEmail:
    def __init__(self, email, turnoSelect):
        self._email = email
        self._turnoSelect = turnoSelect

    @property
    def email(self):
        return self._email

    @property
    def turnoSeleccionado(self):
        return self._turnoSelect

    def enviarnotificacion(self):
        messagebox.showinfo(title="Notificacion Enviada", message="Notificacion enviada a: " + self.email +
                                                                  "\nDatos del turno: "
                                                                  "\nFecha: " + self.turnoSeleccionado.fechaHoraInicio.date().strftime("%d/%m/%y") +
                                                                  "\nHora de Inicio: " + self.turnoSeleccionado.fechaHoraInicio.time().strftime("%H:%M") +
                                                                  "\nHora de Fin: " + self.turnoSeleccionado.fechaHoraFin.time().strftime("%H:%M"))


if __name__ == '__main__':
    turno1 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 10, 0, 0), datetime(2022, 6, 30, 11, 0, 0), [])
    interfazMail = InterfazDeEmail("nicouemacapdevila@gmail.com",turno1)
    interfazMail.enviarnotificacion()
