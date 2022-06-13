
class Marca:
    def __init__(self,nombre,modelos=[]) -> None:
        self._nombre = nombre
        self._modelos = modelos

    # Encapsulamiento
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def modelos(self):
        return self._modelos

    def getNombre(self):
        return self.nombre