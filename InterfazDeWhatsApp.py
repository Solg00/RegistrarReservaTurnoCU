from tkinter import messagebox
from Turno import Turno
from datetime import date
from datetime import datetime


class InterfazDeWhatsApp:

    def enviarnotificacion(self, numTelefono, mensaje):
        messagebox.showinfo(title="Notificacion Enviada a " + numTelefono, message='Telefono:' + numTelefono+ '\n'+mensaje)

if __name__ == '__main__':
    turno1 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 10, 0, 0), datetime(2022, 6, 30, 11, 0, 0), [])
    interfazWp = InterfazDeWhatsApp()

    interfazWp.enviarnotificacion("3543635023",turno1)
