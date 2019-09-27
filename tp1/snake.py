# NOMBRE_APELLIDO = JUAN CELESTINO BARBERIS
# PADRÓN = 105147
# MATERIA = 7540 Algoritmos y Programación 1, curso Essaya
# TP 1 - Snake

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'

#Variables globales del juego

SNAKE_MAX_LENGHT = 10       #Largo máximo que puede alcanzar snake.
TABLERO_SIZE = 20           #Tamaño del tablero (ancho y alto).
SPEED = 1                   #Tiempo permitido por movimiento.
TIME = 100                  #Tiempo de juego.
SNAKE_SYMBOL = '#'          #Símbolo que caracteriza a snake.
FRUTA_SYMBOL = '+'          #Símbolo que caracteriza a la fruta.

from terminal import timed_input, clear_terminal
from random import randint

def main():
    """
    DOCUMENTACIÓN
    """
    fruta = generarFruta()
    movimiento = 'w'
    movimientoAnterior = 'w'
    posCero  = TABLERO_SIZE // 2
    snake   = [[posCero, posCero]]

    while True:
        clear_terminal()
        tablero = generarTablero()

        snake, fruta = moverSnake(snake, movimiento, movimientoAnterior, fruta)

        if len(snake) == SNAKE_MAX_LENGHT:
            print('¡Ganaste!')
            break

        imprimirTablero(tablero, snake, fruta)

        print(f"Actual: {movimiento} | Anterior: {movimientoAnterior} | Snake:{snake} | Fruta:{fruta}")  #DEBUG ZONE

        entrada = inputJugada()
        if entrada == False: 
            break      
        if not entrada == None: 
            movimientoAnterior = movimiento            
            movimiento = entrada

    print('Gracias por jugar!')

def moverSnake(snake, movimiento, movimientoAnterior, fruta):
    """"""
    if movimiento == "w": 
        snake.insert(0, (snake[0][0] - 1,snake[0][1]))
    if movimiento == "s":
        snake.insert(0, (snake[0][0] + 1,snake[0][1]))
    if movimiento == "a": 
        snake.insert(0, (snake[0][0],snake[0][1] - 1))
    if movimiento == "d": 
        snake.insert(0, (snake[0][0],snake[0][1] + 1))

    if snake[0][0] == fruta[0] and snake[0][1] == fruta[1]: 
        print('Nueva fruta')
        fruta = generarFruta()
    else: 
        snake.pop(-1)
        
    return snake, fruta

def inputJugada():
    """Recibe un input del jugador y comprueba que sea 
    una entrada válida. Si no es válida, devuelve una cadena vacía."""
    entrada = timed_input(SPEED)

    if entrada.isspace(): return False
    if entrada == 'w' or entrada == 'a' or entrada == 's' or entrada == 'd':
        return entrada

def generarTablero():
    """Genera el tablero de juego con el <TABLERO_SIZE> predefinido."""
    tablero = []
    for fil in range(TABLERO_SIZE):
        tablero.append([])
        for col in range(TABLERO_SIZE):
            tablero[fil].append('.') 
    return tablero

def imprimirTablero(tablero, snake, fruta):
    """Recibe una lista de listas y lo imprime en forma de tablero (matriz)."""
    print('Controles: [w, a, s, d]')
    print('Salir: [Espacio/Enter]')
    for coord in snake:             #Agrega Snake al tablero
        tablero[coord[0]][coord[1]] = COLOR_VERDE + SNAKE_SYMBOL + COLOR_NORMAL
    tablero[fruta[0]][fruta[1]] = COLOR_ROJO + FRUTA_SYMBOL + COLOR_NORMAL
    for fila in range(TABLERO_SIZE):
            lst = tablero[fila]
            tableroFinal= ""
            for dot in lst:
                tableroFinal += dot
            print(tableroFinal)

def generarSnake():
    """Recibe un largo (no mayor a SNAKE_MAX_LENGHT)"""
    return COLOR_VERDE + SNAKE_PART + COLOR_NORMAL

def generarFruta():
    """Genera dos coordenadas al azar en un rango de 0 hasta <TABLERO_SIZE>."""
    frutaCol = randint(0, TABLERO_SIZE - 1)
    frutaFil = randint(0, TABLERO_SIZE - 1)

    return [frutaCol, frutaFil]


main()              #Esta línea ejecuta el juego.