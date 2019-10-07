#Este módulo contiene funciones del tipo input que intervienen en la jugabilidad
#y el movimiento de Snake.

from modulos.terminal import timed_input

def inputJugada(movimiento, SPEED):
    """Recibe la variable de movimiento. Recibe, medianta input la
    jugada y comprueba que sea válida. Si no es válida, devuelve <NoneType>.
    Comprueba que lo ingresado no sea el opuesto del movimiento anterior."""
    
    entrada = timed_input(SPEED)

    if entrada.isspace():   #Para salir del juego, presiona <SPACE>
        return False  

    if entrada == 'w' and not movimiento == 's': 
        return entrada
    elif entrada == 'a' and not movimiento == 'd':
        return entrada
    elif entrada == 's' and not movimiento == 'w':
        return entrada
    elif entrada == 'd' and not movimiento == 'a':
        return entrada
    return movimiento