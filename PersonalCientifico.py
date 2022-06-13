from Usuario import Usuario


class PersonalCientifico():
    def __init__(self,leg,nom,ape,dni,emailIns,email,cel,usuario) -> None:
        self._legajo = leg
        self._nombre = nom
        self._apellido = ape
        self._numeroDocumento = dni
        self._correoInstitucional = emailIns
        self._correo = email
        self._telefonoCelular = cel
        self._usuario = usuario

    #Encapsulamiento de atributos
    @property
    def legajo(self):
        return self._legajo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def numeroDocumento(self):
        return self._numeroDocumento

    @property
    def correoInstitucional(self):
        return self._correoInstitucional
    
    @property
    def correo(self):
        return self._correo
    
    @property
    def telefonoCel(self):
        return self._telefonoCelular

    @property
    def usuario(self):
        return self._usuario

    #Metodos de clase
    def sosUsuarioActual(self,usuarioActual:Usuario) -> bool:
        '''Compara el usuario del cientifico con el usuario en sesion y retorna un booleano'''
        if self.usuario.nomUsuario == usuarioActual.nomUsuario:
            return True
        else:
            return False

    def getEmail(self) -> str:
        return self.correo

    