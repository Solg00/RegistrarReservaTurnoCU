
class CambioDeEstadoTurno():
    def __init__(self, fechaHoraDesde, fechaHoraHasta, estado) -> None:
        self._fechaHoraDesde = fechaHoraDesde
        self._fechaHoraHasta = fechaHoraHasta
        self._estado = estado
    @property
    def fechaHoraDesde(self):
        return self._fechaHoraDesde

    @property
    def fechaHoraHasta(self):
        return self._fechaHoraHasta

    @property
    def estado(self):
        return self._estado

    def sosEstadoActual(self):
        if self._fechaHoraHasta is None:
            return True
        return False


