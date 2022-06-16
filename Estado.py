class Estado:

    #Constructores
    def __init__(self,nombre,description,ambito,esReservable,esCancelable) -> None:
        self._nombre = nombre
        self._description = description
        self._ambito = ambito
        self._esReservable = esReservable
        self._esCancelable = esCancelable


    #Propiedades
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def description(self):
        return self._description

    @property
    def ambito(self):
        return self._ambito

    @property
    def esReservable(self):
        return self._esReservable

    @property
    def esCancelable(self):
        return self._esCancelable

    #Metodos
    def esReservado(self):
        '''Devuelve si el estado es el Estado Reservado'''
        if self._nombre == "Reservado":
            return True
        else:
            return False

    def esAmbito(self,ambi):
        if self._ambito == ambi:
            return True
        else:
            return False

