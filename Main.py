from InterfazDeTurno import InterfazDeReservaTurno as interfaz
from GestorDeCURegReservaDeTurno import GestorDeCURegReservaDeTurno as gestor
import datosEjemplo as dt


gestor = gestor(dt.rTRepo, dt.rtTipoRepo, dt.centrosRepo, dt.sesion, dt.estadosRepo)
interfaz = interfaz()


def main():
    # interfaz.opcionReservarTurnoRT()
    interfaz.mostrarTurnos(turnosAgrupadosDelRt, turnosAgrupadosPorColorDelRt)
    # gestor.registrarTurno()
    # gestor.buscarTiposRT()


if __name__ == '__main__':
    main()
