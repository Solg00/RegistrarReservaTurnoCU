
class Usuario:
    def __init__(self,nombre_user,passw, habilitado) -> None:
        self._nomUsuario = nombre_user
        self._clave = passw
        self._habilitado = habilitado
    
    #Encapsulamiento
    @property
    def nomUsuario(self):
        return self._nomUsuario
    
    @property
    def clave(self):
        return self._clave

    @property
    def habilitado(self):
        return self._habilitado

    # posiblemente se necesite
    def getDataUsuario(self):
        data = {
            'nombre_user' : self.nomUsuario,
            'clave' : self.clave,
            'habilitado' : self.habilitado
        }
        return data
