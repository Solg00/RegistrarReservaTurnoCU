
class Marca:
    def __init__(self,nombre) -> None:
        self._nombre = nombre
    

    @property
    def nombre(self):
        return self._nombre

    def getNombre(self):
        return self.nombre