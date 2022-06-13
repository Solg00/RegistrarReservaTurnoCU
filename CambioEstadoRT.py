from datetime import datetime

class CambioEstadoRT:
    def __init__(self,fechaDesde,fechaHasta) -> None:
        self._fechaHoraDesde = datetime.strptime(fechaDesde,"%d/%m/%Y %H:%M").strftime('%d/%m/%Y %H:%M')
        self._fechaHoraHasta = datetime.strptime(fechaHasta,"%d/%m/%Y %H:%M").strftime("%d/%m/%Y %H:%M")
    
    @property
    def fechaHoraDesde(self):
        return self._fechaHoraDesde
    
    @property
    def fechaHoraHasta(self):
        return self._fechaHoraHasta

    def sosEstadoActual(self,estadoActual):
        if estadoActual is None:
            return True
        else:
            if self.fechaHoraDesde > estadoActual.fechaHoraDesde:
                return True
            else:
                return False
    
    def __str__(self) -> str:
        return f'CAMBIO: {self.fechaHoraDesde} - {self.fechaHoraHasta}'