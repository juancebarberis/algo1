# NOMBRE_APELLIDO = JUAN CELESTINO BARBERIS
# PADRÓN = 105147
# MATERIA = 7540 Algoritmos y Programación 1, curso Essaya
# TP 1 - Snake

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'

#Parámetros globales del juego

SNAKE_MAX_LENGHT = 10
COLUMNAS = 25
FILAS = 15
VELOCIDAD = 1
TIEMPO = 100

from terminal import timed_input, clear_terminal
from random import randint


def generarFruta():
    """Genera una fruta al azar en el tablero."""
    frutaCol = randint(0, COLUMNAS - 1)
    frutaFil = randint(0, FILAS - 1)

    return frutaCol, frutaFil

def main():
    snake = 'O'
    tamañoSnake = 0
    fruta = '+'
    frutaCol, frutaFil = generarFruta()
    direccion = '+y'
    posX = (FILAS // 2)
    posY = (COLUMNAS//2)

    for t in range(0, TIEMPO):
        tablero = []
        clear_terminal()
        print('Tiempo restante: ' + str(TIEMPO - t))
        print(f'Score: {tamañoSnake}')

        #Construir tablero
        for fila in range(0, FILAS):
            tablero.append([]) 
            for col in range(0,COLUMNAS):
                tablero[fila].append('.')

        if direccion == '+y': posY -= 1
        if direccion == '-y': posY += 1
        
        if direccion == '+x': posX += 1
        if direccion == '-x': posX -= 1

        #Posicionar fruta
        tablero[frutaFil][frutaCol] = COLOR_ROJO + '+' + COLOR_NORMAL

        #Snake come la fruta
        if frutaFil == abs(posY) and frutaCol == abs(posX):
            tamañoSnake += 1
            frutaCol, frutaFil = generarFruta()

        tablero[(posY)][(posX)] = COLOR_VERDE + snake + COLOR_NORMAL 

        for s in range(0,tamañoSnake):
            if direccion == '+x': tablero[(posY + s)][(posX)] += snake 
            if direccion == '-x': tablero[(posY - s)][(posX)] += snake 
        
            if direccion == '+y': tablero[(posY)][(posX + s)] += snake 
            if direccion == '-y': tablero[(posY)][(posX - s)] += snake 

        #DEBUG ZONE
        #print(f"({posX}, {posY})")
        #END DEBUG ZONE

        if tamañoSnake == SNAKE_MAX_LENGHT: break           

        #Imprime el tablero
        for fila in range(0, FILAS):
            lst = tablero[fila]
            tableroFinal= ""
            for dot in lst:
                tableroFinal += dot
            print(tableroFinal)

        #Recibe el input y fija una direccion
        entrada = timed_input(VELOCIDAD)

        if entrada == '' or len(entrada) > 1: continue
        if entrada.isspace() == True: break

        if entrada == 'w': direccion = '+y'
        if entrada == 's': direccion = '-y'
        if entrada == 'd': direccion = '+x'
        if entrada == 'a': direccion = '-x' 

    print('Gracias por jugar!')  


#EXECUTION ZONE!
main()