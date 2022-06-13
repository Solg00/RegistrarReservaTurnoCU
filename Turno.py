from datetime import datetime


class Turno:
    def __init__(self, fechaGeneracion, diaSemana, fechaHoraInicio, fechaHoraFin) -> None:
        self._fechaGeneracion = fechaGeneracion
        self._diaSemana = diaSemana
        self._fechaHoraInicio = fechaHoraInicio
        self._fechaHoraFin = fechaHoraFin
        self._cambiosDeEstadoTurno = []

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

    def sosPosteriorAFechaActual(self):
        if self.fechaHoraInicio > datetime.now():
            return True
        return False

    def getDatosTurno(self):
        return

    def estoyDisponible(self):
        for cambioEstado in self.cambiosDeEstadoTurno:
            if cambioEstado.sosEstadoActual() and cambioEstado.nombre == "Disponible":
                return True
        return False

    def reservar(self):

