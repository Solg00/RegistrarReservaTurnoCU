
from datetime import datetime
from datetime import date
from InterfazDeTurno import InterfazDeReservaTurno as interfaz

class GestorDeCURegReservaDeTurno:
    def __init__(self,RTs,tiposRT,CIs,sesion,estados) -> None:
        self._recursosTecnologicos = RTs
        self._tiposRT = tiposRT
        self._centrosInvestigacion = CIs
        self._sesion = sesion 
        self._estados = estados

        self._datosRts = []
        self._tipoRTSeleccionado = None
        self._RtXCI = {}
        self._RTSeleccionado = None
        self._usuarioLogueado = None
        self._ciDelRT = None
        self._turnosRT = None
        self._turnoSeleccionado = None
        self._envioNotifSeleccionado = None
        self._confirmacion = ''
        
    def registrarReservaTurno(self):
        print('***GESTOR INICIO CU ***')
        self.buscarTiposRT()

    def buscarTiposRT(self):
        nombresRts = []
        for tipo in self._tiposRT:
            nombresRts.append(tipo.getNombre())
        
        interfaz.mostrarTiposRT(nombresRts)

    
    def tomarSeleccionTipoRT(self, selected):
        self._tipoRTSeleccionado = selected
        self.buscarRT()

    def tomarSeleccionRT(self, selected):
        self._RTSeleccionado = selected


    def tomarSeleccionDeTurno(self, selected):
        self._turnoSeleccionado  = selected

    def tomarSeleccionEnvioNotificacion(self, selected):
        self._envioNotifSeleccionado  = selected

    def tomarConfirmacion(self,selected):
        self._confirmacion  = selected

    def buscarRT(self):
        for rt in self._recursosTecnologicos:
            if rt.sosRTDelTipoSeleccionado(self._tipoRTSeleccionado) and rt.buscarEstadoActual().esReservable():
                self.obtenerDatosRT(rt)
        self.agruparPorCI()
        self.asignarColorPorEstado()
                
                


    def obtenerDatosRT(self,rt):
        rt_estado_actual = rt.buscarEstadoActual().getNombreEstado()
        rt_nroInv = rt.getNumeroInventario()
        rt_modMarc = rt.miModeloYMarca()
        rt_CI = self.obtenerCIDelRT(rt)
        self._datosRTs.append(
            {
                'nroInv' : rt_nroInv,
                'modMarca' : rt_modMarc,
                'estadoActual' : rt_estado_actual,
                'CI_nombre' : rt_CI,
            }
        )
                
    def obtenerCIDelRT(self,rt):
        for centroInvestigacion in self._centrosInvestigacion:
            if centroInvestigacion.esTuRT(rt):
                return centroInvestigacion.getNombre()

    def agruparPorCI(self):
        '''Agrupa los RTs por el CI a los que pertenezcan'''
        for rt in self._datosRts:
            ci = rt.get('CI_nombre')
            cis = self.RtXCI.keys()
            rt = {'nroInv' : rt.get('nroInv'), 
                    'modMarca' : rt.get('modMarca'),
                        'estadoActual' : rt.get('estadoActual')
            }
            if ci in cis:
                self.RtXCI[ci].append(rt)
            else:
                self.RtXCI[ci] = [rt]


    def asignarColorPorEstado(self):
        for rt in self._datosRts:
            if rt.get('estadoActual') == 'Disponible':
                rt['estadoActual']={'nombre' : rt.get('estadoActual'), 'color' : 'Azul' }
            elif rt.get('estadoActual') == 'En Mantenimiento':
                rt['estadoActual']={'nombre' : rt.get('estadoActual'), 'color' : 'Verde' }
            elif rt.get('estadoActual') == 'Con inicio de mantenimiento correctivo':
                rt['estadoActual']={'nombre' : rt.get('estadoActual'), 'color' : 'Gris' }
            else: 
                pass


    def obtenerUsuarioLogueado(self):
        self._usuarioLogueado = self._sesion.getUsuarioSesion()

    def obtenerCIRTSeleccionado(self):
       self._ciDelRT = self._RTSeleccionado.getMiCI(self._centrosInvestigacion)

    def verificarCientificoDeCIRT(self):
        cientificos = self._ciDelRT.misCientificosActivos()
        for cientifico in cientificos:
            if cientifico.compararUsuario(self._usuarioLogueado):
                return True
        return False

    def getDateTimeActual():
        return datetime.now()

    def obtenerTurnosParaRT(self):
        fechaHoraActual = self.getDateTimeActual()
        self._turnosRT = self._RTSeleccionado.buscarTurnosDelRT()
    
    def ordenarTurnos(self):
        self._turnosRT = sorted(self._turnosRT, key=lambda x: x.fechaHoraInicio)
    
    def agruparTurnos(self):
        turnosAgrupados = {}
        for turno in self._turnosRT:
            turnosDia = []
            fechaTurno = turno.fechaHoraInicio.date()
            fechas = turnosAgrupados.keys()
            if fechaTurno not in fechas:
                turnosAgrupados[fechaTurno] = turnosDia
                turnosAgrupados[fechaTurno].append(turno)
            else:
                turnosAgrupados[fechaTurno].append(turno)
        return turnosAgrupados

    
    def asignarColorTurnoXDisp(self):
        turnosPorColor = {"Azul": [],
                          "Gris": [],
                          "Rojo": []}

        for turno in self._turnosRT:
            estadoTurno = turno.cambiosDeEstadoTurno[-1].estado.getNombre()
            if estadoTurno == "Disponible":
                turnosPorColor["Azul"].append(turno)
            if estadoTurno == "Con reserva pendiente de confirmacion":
                turnosPorColor["Gris"].append(turno)
            if estadoTurno.esReservado():
                turnosPorColor["Rojo"].append(turno)

        return turnosPorColor

    def confirmarTurno(self):
        estadoAsignar = None
        for estado in self._estados:
           if estado.esReservado() and estado.esAmbito('Turno'):
                estadoAsignar = estado
        
        self._turnoSeleccionado.reservar(estadoAsignar)

        self._usuarioLogueado.getEmailCientifico(self._ciDelRT.cientificos)

    def generarNotificacionConDatosTurno(self):
        pass
    def FinCU(self):
        pass
