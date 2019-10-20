#Este módulo contiene funciones del tipo input que intervienen en la jugabilidad
#y el movimiento de Snake.

from modulos.terminal import timed_input

def inputJugada(movimiento, variables, _ESPECIALES, snake):
    """
    Comprueba lo ingresado por el usuario desde el teclado.
    Evalúa si pertenece a un movimiento, un especial, o a un cierre del juego.
    """
    entrada = timed_input(float(variables['SPEED']))
    #Condicionales de 'salir del juego'.
    if entrada.isspace():   #Para salir del juego, presiona <SPACE>
        return False, variables, snake, _ESPECIALES  
    #Condicionales de movimiento
    if entrada == 'w' and not movimiento == 's': 
        return entrada, variables, snake, _ESPECIALES
    elif entrada == 'a' and not movimiento == 'd':
        return entrada, variables, snake, _ESPECIALES
    elif entrada == 's' and not movimiento == 'w':
        return entrada, variables, snake, _ESPECIALES
    elif entrada == 'd' and not movimiento == 'a':
        return entrada, variables, snake, _ESPECIALES
    #Condicionales de especiales
    especiales = variables['SPECIALS']
    if especiales == [] or especiales[0] == '':
        return movimiento, variables, snake, _ESPECIALES
    for i in range(len(especiales)):
        if entrada == _ESPECIALES[especiales[i]]['E_KEY'] and int(_ESPECIALES[especiales[i]]['E_CANT']) > 0:
            if _ESPECIALES[especiales[i]]['E_TYPE'] == 'VELOCIDAD':
                velocidad = float(variables['SPEED'])
                velocidad += float(_ESPECIALES[especiales[i]]['E_VALUE'])
                variables['SPEED'] = str(velocidad)
                _ESPECIALES[especiales[i]]['E_CANT'] = int(_ESPECIALES[especiales[i]]['E_CANT'])-1
                break
            if _ESPECIALES[especiales[i]]['E_TYPE'] == 'LARGO':
                if len(snake) == 1:
                    break
                if int(_ESPECIALES[especiales[i]]['E_VALUE']) == -1:
                    snake.pop(-1)
                if int(_ESPECIALES[especiales[i]]['E_VALUE']) == 1:
                    if movimiento == 'w': snake.insert(0, (snake[0][0] - 1, snake[0][1]))
                    if movimiento == 's': snake.insert(0, (snake[0][0] + 1, snake[0][1]))
                    if movimiento == 'a': snake.insert(0, (snake[0][0], snake[0][1] - 1))
                    if movimiento == 'd': snake.insert(0, (snake[0][0], snake[0][1] + 1))
                _ESPECIALES[especiales[i]]['E_CANT'] = int(_ESPECIALES[especiales[i]]['E_CANT'])-1
                break
    return movimiento, variables, snake, _ESPECIALES