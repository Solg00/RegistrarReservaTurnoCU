from datetime import datetime

class CambioEstadoRT:
    def __init__(self,fechaDesde,fechaHasta=None) -> None:
        self._fechaHoraDesde = datetime.strptime(fechaDesde,"%d/%m/%Y %H:%M").strftime('%d/%m/%Y %H:%M')
        if fechaHasta:
            self._fechaHoraHasta = datetime.strptime(fechaHasta,"%d/%m/%Y %H:%M").strftime("%d/%m/%Y %H:%M")
        else:
            self._fechaHoraHasta = fechaHasta
    
    @property
    def fechaHoraDesde(self):
        return self._fechaHoraDesde
    
    @property
    def fechaHoraHasta(self):
        return self._fechaHoraHasta

    def sosEstadoActual(self):
        if self.fechaHoraHasta is None:
            return True
        
        return False

    def __str__(self) -> str:
        return f'CAMBIO: {self.fechaHoraDesde} - {self.fechaHoraHasta}'