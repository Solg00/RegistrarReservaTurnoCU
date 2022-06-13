
class CambioDeEstadoTurno():
    def __init__(self, fechaHoraDesde, fechaHoraHasta) -> None:
        self._fechaHoraDesde = fechaHoraDesde
        self._fechaHoraHasta = fechaHoraHasta
        # TODO: Atributo Estado

    @property
    def fechaHoraDesde(self):
        return self._fechaHoraDesde

    @property
    def fechaHoraHasta(self):
        return self._fechaHoraHasta

    def sosEstadoActual(self):
        if self._fechaHoraHasta is None:
            return True
        return False


