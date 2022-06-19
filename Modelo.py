class Modelo:

    #Constructores
    def __init__(self,nombre) -> None:
        self._nombre = nombre

    #Propiedades
    @property
    def nombre(self):
        return self._nombre
    
    #Metodos
    def getNombre(self):
        '''Obtiene el nombre del modelo'''
        return self.nombre
    
    def getMarca(self,marcas:list):
        '''Obtiene la marca del modelo'''
        for marca in marcas:
            for i in marca.modelos:
                if self.nombre==i.nombre:
                    return marca.getNombre()