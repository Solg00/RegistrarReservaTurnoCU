from datetime import datetime


class CentroDeInvestigacion:
    def __init__(self, nombre, sigla, direccion, edificio, piso, coordenadas, correoElectronico,
                 numeroResolucionCreacion, fechaResolucionCreacion, reglamento, caracteristicasGenerales,
                 tiempoAntelacionReserva, fechaBaja, motivoBaja,cientificos=[], recursosTecnologicos=[]) -> None:
        self._nombre = nombre
        self._sigla = sigla
        self._direccion = direccion
        self._edificio = edificio
        self._piso = piso
        self._coordenadas = coordenadas
        self._telefonosContacto = []
        self._correoElectronico = correoElectronico
        self._numeroResolucionCreacion = numeroResolucionCreacion
        self._fechaResolucionCreacion = fechaResolucionCreacion
        self._reglamento = reglamento
        self._caracteristicasGenerales = caracteristicasGenerales
        self._fechaAlta = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._tiempoAntelacionReserva = tiempoAntelacionReserva
        self._fechaBaja = fechaBaja
        self._motivoBaja = motivoBaja
        self._cientificos = cientificos
        self._recursosTecnologicos = recursosTecnologicos
    @property
    def nombre(self):
        return self._nombre

    @property
    def sigla(self):
        return self._sigla

    @property
    def direccion(self):
        return self._direccion

    @property
    def edificio(self):
        return self._edificio

    @property
    def piso(self):
        return self._piso

    @property
    def coordenadas(self):
        return self._coordenadas

    @property
    def correoElectronico(self):
        return self._correoElectronico

    @property
    def numeroResolucionCreacion(self):
        return self._numeroResolucionCreacion

    @property
    def fechaResolucionCreacion(self):
        return self._fechaResolucionCreacion

    @property
    def reglamento(self):
        return self._reglamento

    @property
    def caracteristicasGenerales(self):
        return self._caracteristicasGenerales

    @property
    def tiempoAntelacionReserva(self):
        return self._tiempoAntelacionReserva

    @property
    def fechaBaja(self):
        return self._fechaBaja

    @property
    def motivoBaja(self):
        return self._motivoBaja

    @property
    def telefonosContacto(self):
        return self._telefonosContacto

    @property
    def cientificos(self):
        return self._cientificos

    @property
    def recursosTecnologicos(self):
        return self._recursosTecnologicos

    @property
    def getNombre(self):
        return self.nombre

    def esTuRT(self,rt):
        for recurso in self.recursosTecnologicos:
            if recurso.nroRT == rt.nroRT:
                return True
        return False

    def misCientificosActivos(self):
        cientificosActivos = []
        for cientifico in self.cientificos:
            if cientifico.esCientificoActivo():
                cientificosActivos.append(cientifico)
        return cientificosActivos
