#Este módulo contiene funciones que interactuan directamente con el jugador.

from modulos.terminal import clear_terminal, timed_input

def jugadorSalir(motivo):
    """
    Limpia la terminal e imprime un mensaje acorde al motivo
    de finalización del juego.
    """
    if motivo == 'pressEspace':
        clear_terminal()
        print('¡Gracias por jugar!')
        return False

    if motivo == 'gameOver':
        clear_terminal()
        print('¡Game Over! :(')
        return False

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
