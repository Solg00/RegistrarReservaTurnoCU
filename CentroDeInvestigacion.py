class CentroDeInvestigacion:
    def __init__(self, nombre, sigla, direccion, edificio, piso, coordenadas, correoElectronico,
                 numeroResolucionCreacion, fechaResolucionCreacion, reglamento, caracteristicasGenerales,
                 fechaAlta, tiempoAntelacionReserva, fechaBaja, motivoBaja) -> None:
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
        self._fechaAlta = fechaAlta
        self._tiempoAntelacionReserva = tiempoAntelacionReserva
        self._fechaBaja = fechaBaja
        self._motivoBaja = motivoBaja
        self._cientificos = []

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
    def fechaAlta(self):
        return self._fechaAlta

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

    def agregarTelefonoContacto(self, telefono):
        self.telefonosContacto.append(telefono)

    def agregarCientifico(self, cientifico):
        self.cientificos.append(cientifico)

    def misCientificosActivos(self):
        cientificosActivos = []
        for cientifico in self.cientificos:
            if cientifico.esCientificoActivo():
                cientificosActivos.append(cientifico)
        return cientificosActivos
