from PersonalCientifico import PersonalCientifico
from Usuario import Usuario

class AsignacionCientificoDelCI:

    #Constructores
    def __init__(self,fechaDesde,fechaHasta,personalCientifico:PersonalCientifico) -> None:
        self._fechaDesde = fechaDesde
        self._fechaHasta = fechaHasta
        self._personalCientifico = personalCientifico

    #Propiedades
    @property
    def fechaDesde(self):
        return self._fechaDesde
    
    @property
    def fechaHasta(self):
        return self._fechaHasta

    @property
    def personalCientifico(self):
        return self._personalCientifico

    #Metodos
    def esCientificoActivo(self):
        '''Comprueba si el cientifico esta actualmente asignado al CI'''
        if self._fechaHasta == None:
            return True
        else:
            return False

    def compararUsuario(self, usuario:Usuario):
        '''Comprueba si el Usuario logueado es el mismo que el del cientifico asignado'''
        return self._personalCientifico.sosUsuarioActual(usuario)
