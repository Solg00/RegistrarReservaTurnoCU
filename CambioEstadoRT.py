from datetime import datetime

class CambioEstadoRT:
    def __init__(self,estado) -> None:
        self._fechaHoraDesde = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._fechaHoraHasta = None
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
        if self.fechaHoraHasta is None:
            return True
        
        return False

    def getNombreEstado(self):
        return self.estado.getNombre()
    
    def esReservable(self):
        if self.estado.esReservable():
            return True
        return False

