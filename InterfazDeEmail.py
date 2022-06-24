from tkinter import messagebox
from Turno import Turno
from datetime import date
from datetime import datetime

class InterfazDeEmail:

    def enviarnotificacion(self, email, mensaje):
        messagebox.showinfo(title="Notificacion Enviada a " + email, message=mensaje)


if __name__ == '__main__':
    turno1 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 10, 0, 0), datetime(2022, 6, 30, 11, 0, 0), [])
    interfazMail = InterfazDeEmail()
    interfazMail.enviarnotificacion("nicouemacapdevila@gmail.com",turno1)
