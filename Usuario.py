
class Usuario:
    def __init__(self,nombre_user,passw, habilitado) -> None:
        self._usuario = nombre_user
        self._clave = passw
        self._habilitado = habilitado

    @property
    def usuario(self):
        return self._usuario
    
    @property
    def clave(self):
        return self._clave

    @property
    def habilitado(self):
        return self._habilitado

    # posiblemente se necesite
    def getDataUsuario(self):
        data = {
            'nombre_user' : self.usuario,
            'clave' : self.clave,
            'habilitado' : self.habilitado
        }
        return data
