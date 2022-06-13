
class TipoRecursoTecnologico():
    def __init__(self, nombre, descripcion) -> None:
        self._nombre = nombre
        self._descripcion = descripcion

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    def getNombre(self):
        return self._nombre
