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
SNAKE_PART = '#'            #Símbolo que caracteriza a snake.
FRUTA_SYMBOL = '+'          #Símbolo que caracteriza a la fruta.

from terminal import timed_input, clear_terminal
from random import randint

def main():
    """
    DOCUMENTACIÓN
    """
    FrutaFil, FrutaCol = generarFruta()
    movimiento = 'w'
    posCero  = TABLERO_SIZE // 2
    snake   = [SNAKE_PART]
    tablero = generarTablero()

    while True:
        clear_terminal()
        tablero[FrutaFil][FrutaCol] = COLOR_ROJO + FRUTA_SYMBOL + COLOR_NORMAL

        #Falta hacer que aparezca snake, y todo lo relacionado a su movimiento.

        imprimirTablero(tablero)

        print(f"{movimiento} | {snake}")  #DEBUG ZONE
        
        entrada = inputJugada()
        if entrada == False: 
            break
        if not entrada == None: 
            movimiento = entrada

    print('Gracias por jugar!')

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

def imprimirTablero(tablero):
    """Recibe una lista de listas y lo imprime en forma de tablero (matriz)."""
    print('Controles: [w, a, s, d]')
    print('Salir: [Espacio/Enter]')
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

    return frutaCol, frutaFil


main()              #Esta línea ejecuta el juego.