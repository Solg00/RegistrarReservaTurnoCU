from datetime import datetime

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

    def crearCambioEstado(self, estado):
        # Se crea un nuevo cambio de estado, con un estado que se pasa por parametro
        cambioEstado = CambioDeEstadoTurno(estado)

        # Se busca el estado actual (que ahora seria el anterior) y se
        # setea su fechaHoraHasta con la fecha y hora actual
        for cambioEstado in self.cambiosDeEstadoTurno:
            if cambioEstado.sosEstadoActual():
                cambioEstado.fechaHoraHasta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Finalmentese agrega el nuevo cambio de estado, ya con la fechaHoraHasta del estado anterior actualizada
        self.cambiosDeEstadoTurno.append(cambioEstado)

    def sosPosteriorAFechaActual(self):
        if self.fechaHoraInicio > datetime.now():
            return True
        return False

    def getDatosTurno(self):
        return self

    def buscarEstadoActual(self):
        for cambioEstado in self.cambiosDeEstadoTurno:
            if cambioEstado.sosEstadoActual():
                return cambioEstado

    # El estadoReservado se lo pasaria el gestor despues de buscar entre los estados
    def reservar(self, estadoReservado):
        self.crearCambioEstado(estadoReservado)
