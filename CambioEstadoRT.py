from datetime import datetime

class CambioEstadoRT:
    def __init__(self,estado,fechaDesde,fechaHasta=None) -> None:
        self._fechaHoraDesde = datetime.strptime(fechaDesde,"%d/%m/%Y %H:%M").strftime('%d/%m/%Y %H:%M')
        if fechaHasta:
            self._fechaHoraHasta = datetime.strptime(fechaHasta,"%d/%m/%Y %H:%M").strftime("%d/%m/%Y %H:%M")
        else:
            self._fechaHoraHasta = fechaHasta
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
    
    def __str__(self) -> str:
        return f'CAMBIO: {self.fechaHoraDesde} - {self.fechaHoraHasta}'