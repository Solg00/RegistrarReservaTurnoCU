from datetime import datetime
from time import strptime

from CambioDeEstadoTurno import CambioDeEstadoTurno


class Turno:
    def __init__(self, fechaGeneracion, diaSemana, fechaHoraInicio, fechaHoraFin,cambiosDeEstadoTurno = []) -> None:
        self._fechaGeneracion = fechaGeneracion
        self._diaSemana = diaSemana
        self._fechaHoraInicio = fechaHoraInicio
        self._fechaHoraFin = fechaHoraFin
        self._cambiosDeEstadoTurno = cambiosDeEstadoTurno

    @property
    def fechaGeneracion(self):
        return self._fechaGeneracion
    
    @property
    def diaSemana(self):
        return self._diaSemana
    
    @property
    def fechaHoraInicio(self):
        return self._fechaHoraInicio

    @property
    def fechaHoraFin(self):
        return self._fechaHoraFin

    @property
    def cambiosDeEstadoTurno(self):
        return self._cambiosDeEstadoTurno

    def crearCambioEstado(self, estado,date):
        # Se crea un nuevo cambio de estado, con un estado que se pasa por parametro
        cambioEstado = CambioDeEstadoTurno(estado)

        # Se busca el estado actual (que ahora seria el anterior) y se
        # setea su fechaHoraHasta con la fecha y hora actual
        for cambioEstado in self.cambiosDeEstadoTurno:
            if cambioEstado.sosEstadoActual():
                cambioEstado.fechaHoraFin = date

        # Finalmentese agrega el nuevo cambio de estado, ya con la fechaHoraHasta del estado anterior actualizada
        self.cambiosDeEstadoTurno.append(cambioEstado)

        print('**********TURNO RESERVADO****************')

    def sosPosteriorAFechaActual(self, date):
        if self.fechaHoraInicio > date:
            return True
        return False

    def getDatosTurno(self):
        return self

    def buscarEstadoActual(self):
        for cambioEstado in self.cambiosDeEstadoTurno:
            if cambioEstado.sosEstadoActual():
                return cambioEstado

    # El estadoReservado se lo pasaria el gestor despues de buscar entre los estados
    def reservar(self, estadoReservado,date):
        print('TURNO: reservando')

        self.crearCambioEstado(estadoReservado,date)

    def getDatosTurno(self):
        '''Devuelve la fecha de inicio, de fin y el estado del Turno'''
        turno_fechaHoraInicio = self.getFechaInicio()
        turno_fechaHoraFin = self.getFechaFin()
        turno_estado_actual = self.buscarEstadoActual().getNombreEstado()
        turnoData = {
                'FechaHoraInicio' : turno_fechaHoraInicio,
                'FechaHoraFin' : turno_fechaHoraFin,
                'EstadoActual' : turno_estado_actual,
            }
        return turnoData

    def getFechaInicio(self):
        return self._fechaHoraInicio

    def getFechaFin(self):
        return self._fechaHoraFin
