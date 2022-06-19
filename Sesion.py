from Usuario import Usuario

class Sesion:

    #Constructores
    def __init__(self,usuario:Usuario) -> None:
        self._usuario = usuario
    
    #Propiedades
    @property
    def usuario(self):
        return self._usuario

    #Metodos
    def getUsuarioSesion(self):
        '''Obtiene el usuario en Sesion'''
        return self.usuario

