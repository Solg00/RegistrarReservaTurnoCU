from RecursoTecnologico import RecursoTecnologico
from Estado import Estado
from Turno import Turno
from CambioDeEstadoTurno import CambioDeEstadoTurno
from CambioEstadoRT import CambioEstadoRT
from Modelo import Modelo
from Marca import Marca
from TipoRecursoTecnologico import TipoRecursoTecnologico
from CentroDeInvestigacion import CentroDeInvestigacion
from PersonalCientifico import PersonalCientifico
from AsignacionCientificoDelCI import AsignacionCientificoDelCI
from Usuario import Usuario
from Sesion import Sesion
from datetime import datetime


# >>> Estados
estadoDisponibleRt = Estado("Disponible", "Esta disponible", "RT", True, False)
estadoMantenimientoRt = Estado("Mantenimiento", "Esta en Mantenimiento", "RT", False, False)
estadoDisponibleTu = Estado("Disponible", "Esta disponible", "Turno", True, False)
estadoReservadoTu = Estado("Reservado", "Esta reservado", "Turno", False, True)
estadoPendienteTu = Estado("Con reserva pendiente de confirmacion", "Pendiente", "Turno", False, True)
estadosRepo = [estadoDisponibleRt, estadoMantenimientoRt, estadoDisponibleTu, estadoReservadoTu, estadoPendienteTu]

# >>> Modelos
mod1 = Modelo("RX3021C")
mod2 = Modelo("LG1121D")
mod3 = Modelo("LasS5")
mod4 = Modelo("EX80")
modelosRepo = [mod1, mod2, mod3, mod4]

# >>> Marcas
marc1 = Marca("Panasonic", [mod1,mod2])
marc2 = Marca("EPSON", [mod3,mod4])
marcasRepo = [marc1, marc2]

# >>> TiposRT
tipo1= TipoRecursoTecnologico("Varios","Dispositivos varios...")
tipo2= TipoRecursoTecnologico("Impresoras","Dispositivos para mostar el contenido...")
rtTipoRepo = [tipo1, tipo2]


# >>> Turnos
turno1 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 10, 0, 0), datetime(2022, 6, 30, 11, 0, 0), [CambioDeEstadoTurno(estadoReservadoTu)])
turno2 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 11, 0, 0), datetime(2022, 6, 30, 12, 0, 0), [CambioDeEstadoTurno(estadoDisponibleTu)])
turno3 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 12, 0, 0), datetime(2022, 6, 30, 13, 0, 0), [CambioDeEstadoTurno(estadoPendienteTu)])
turno4 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 13, 0, 0), datetime(2022, 6, 30, 14, 0, 0), [CambioDeEstadoTurno(estadoDisponibleTu)])
turno5 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 14, 0, 0), datetime(2022, 6, 30, 15, 0, 0), [CambioDeEstadoTurno(estadoReservadoTu)])

turno6 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 10, 0, 0), datetime(2022, 6, 30, 11, 0, 0), [CambioDeEstadoTurno(estadoReservadoTu)])
turno7 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 11, 0, 0), datetime(2022, 6, 30, 12, 0, 0), [CambioDeEstadoTurno(estadoDisponibleTu)])

turno8 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 10, 0, 0), datetime(2022, 6, 30, 11, 0, 0), [CambioDeEstadoTurno(estadoReservadoTu)])
turno9 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 11, 0, 0), datetime(2022, 6, 30, 12, 0, 0), [CambioDeEstadoTurno(estadoDisponibleTu)])
turno10 = Turno(datetime(2022, 6, 20, 4, 0, 0), 4, datetime(2022, 6, 30, 12, 0, 0), datetime(2022, 6, 30, 13, 0, 0), [CambioDeEstadoTurno(estadoPendienteTu)])
turnosRepo = [turno1, turno2, turno3, turno4, turno5, turno6, turno7, turno8, turno9, turno10]

# >>> RT
rt1= RecursoTecnologico(1, "imagen.png", 0,  20, 22, mod1, tipo1, [CambioEstadoRT(estadoDisponibleRt)],[turno1,turno2,turno3,turno4,turno5])
rt2= RecursoTecnologico(2, "imagen.png", 0,  20, 22, mod2, tipo1, [CambioEstadoRT(estadoDisponibleRt)],[turno6,turno7])
rt3= RecursoTecnologico(3, "imagen.png", 0,  20, 22, mod3, tipo2, [CambioEstadoRT(estadoDisponibleRt)],[turno8,turno9,turno10])
rt4= RecursoTecnologico(3, "imagen.png", 0,  20, 22, mod4, tipo2, [CambioEstadoRT(estadoDisponibleRt)],[])
rTRepo = [rt1, rt2, rt3, rt4]

# >>> Usuarios
user1=Usuario("Edu12","pass1",True)
user2=Usuario("Mica32","pass2",True)

# >>> Cientificos
cient1=PersonalCientifico(7001,"Eduardo","Apellido1",22778484,"mail1","mail2",318245685,user1)
cient2=PersonalCientifico(7032,"Micaela","Apellido2",24778484,"mail3","mail4",318245685,user2)


# >>> Asignaciones Cientificos
asigCient1 = AsignacionCientificoDelCI(datetime.now().date(), None, cient1)
asigCient2 = AsignacionCientificoDelCI(datetime.now().date(), None, cient2)

# >>> Centros Investigacion
ci1= CentroDeInvestigacion("Mecanica","MEC","Av. avenida 500","Edificio1",1,"22.55.60","ej@gm.com",50058,datetime(2020, 4, 10, 17, 00, 0),"reglamento","cracteristicas generales",22,None,None,[asigCient1],[rt1,rt3])
ci2= CentroDeInvestigacion("Sonido","SON","Av. avenida 500","Edificio2",1,"22.55.60","ej@gm.com",50058,datetime(2020, 4, 10, 17, 00, 0),"reglamento","cracteristicas generales",22,None,None,[asigCient2],[rt2,rt4])
centrosRepo = [ci1,ci2]










# >>> Sesion
sesion=Sesion(user1)
