from datetime import datetime


class RecursoTecnologico:
    def __init__(self,nroRT,img,perMP,durMP,frHorTur,modelo,tipoRT,cambioEstado,turnos=[]) -> None:
        self._nroRT = nroRT
        self._fechaAlta = datetime.now().strftime('%d/%m/%Y %H:%M')
        self._imagenes = img
        self._periodicidaMP = perMP
        self._duracionMP = durMP
        self._fraccionHorarioTurnos = frHorTur
        self._modelo = modelo
        self._tipoRT = tipoRT
        self._turnos = turnos
        self._cambioEstadoRT = cambioEstado
    @property
    def nroRT(self):
        return self._nroRT
    
    @property
    def fechaAlta(self):
        return self._fechaAlta
    
    @property
    def imagenes(self):
        return self._imagenes

    @property
    def periodicidaMP(self):
        return self._periodicidaMP
    
    @property
    def duracionMP(self):
        return self._duracionMP
    
    @property
    def fraccionHorarioTurnos(self):
        return self._fraccionHorarioTurnos
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def tipoRT(self):
        return self._tipoRT
    
    @property
    def cambioEstadoRT(self):
        return self._cambioEstadoRT

    @property
    def turnos(self):
        return self._turnos

    # Metodos de clase
    def sosRTDelTipoSeleccionado(self,tipoSeleccionado)-> bool:
        '''Compara si el tipo del RT es igual al enviado por parametro y retorna un booleano'''
        if self.tipoRT.nombre == tipoSeleccionado:
            return True
        else:
            return False
    
    def getNumeroInventario(self) -> int:
        return self.nroRT
    
    def miModeloYMarca(self,marcas:list)-> str :
        return self.modelo.getNombre() + '-' + self.modelo.getMarca(marcas)

    def getMiCI(self,centrosInvestigacion:list):
        '''Obtiene el centro de investigación al que pertenece el RT'''
        for centro in centrosInvestigacion:
            if centro.esTuRT(self):
                return centro
    
    def buscarTurnosDelRT(self) -> list:
        '''Obtiene los turnos del RT posteriores a la fecha actual'''
        listaTurnos = []
        for turno in self.turnos:
            posterior = turno.sosPosteriorAFechaActual()
            if posterior:
                turno = turno.getDatosTurno()
                listaTurnos.append(turno)
        return listaTurnos

    def buscarEstadoActual(self):
        '''Obtiene el estado actual del RT'''
        estadoActual = None
        for cambioEstado in self.cambioEstadoRT:
            if cambioEstado.sosEstadoActual():
                estadoActual = cambioEstado
        return estadoActual

    def esReservable(self):
        return self.buscarEstadoActual().esReservable()

    def getCIDeRT(self,CIs):
        for centroInvestigacion in CIs:
            if centroInvestigacion.esTuRT(self):
                return centroInvestigacion.getNombre()

    def getDatosRT(self,CIs,marcas):
        '''Devuelve el Nro de Inventario, la Marca y modelo, el nombre del CI, y el estado del RT'''
        rt_estado_actual = self.buscarEstadoActual().getNombreEstado()
        rt_nroInv = self.getNumeroInventario()
        rt_modMarc = self.miModeloYMarca(marcas)
        rt_CI = self.getCIDeRT(CIs)
        rt_data = {
                'nroInv' : rt_nroInv,
                'modMarca' : rt_modMarc,
                'estadoActual' : rt_estado_actual,
                'CI_nombre' : rt_CI,
            }
        return rt_data