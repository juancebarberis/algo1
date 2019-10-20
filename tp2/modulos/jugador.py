#Este módulo contiene funciones que interactuan directamente con el jugador.

from modulos.terminal import clear_terminal, timed_input

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'

def jugadorSalir(motivo):
    """
    Limpia la terminal e imprime un mensaje acorde al motivo
    de finalización del juego.
    """
    if motivo == 'pressEspace':
        clear_terminal()
        print(f'{COLOR_VERDE}¡Gracias por jugar!{COLOR_NORMAL}')
        return False

    if motivo == 'gameOver':
        clear_terminal()
        print(f'{COLOR_ROJO}¡Game Over! :({COLOR_NORMAL}')
        return False
    
    if motivo == 'loadError':
        print(f'{COLOR_ROJO}Error a la hora de cargar los archivos necesarios para ejecutar el juego.{COLOR_NORMAL}')

def jugadorNivelUp(nivelActual, ultimoNivel):
    '''
    El jugador sube de nivel.
    '''
    clear_terminal()
    print('¡Felicidades! Completaste el nivel.')
    print('')
    print('')
    inputNull = ''
    print('Presione cualquier tecla para continuar.')
    while inputNull == '':
        inputNull = timed_input(0.1)
    if nivelActual == ultimoNivel: 
        return False
    return True
