#Funciones que imprimer los elementos visibles del juego

from modulos.terminal import clear_terminal

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'

def imprimirTablero(tablero, snake, fruta, TABLERO_SIZE, var):
    """
    Recibe los componentes del juego (Tablero, Snake y Fruta) y los imprime en el
    orden y posiciones correspondientes.
    """
    clear_terminal()

    #Información superior
    print("SNAKE++")
    print(f"Nivel: {var['LEVEL']}  |  Tamaño: {len(snake)}")
    print('')

    #Agrega Snake al tablero
    for coord in snake:             
        tablero[coord[0]][coord[1]] = COLOR_VERDE + var['SNAKE_SYMBOL'] + COLOR_NORMAL

    #Agrega la fruta al tablero
    tablero[fruta[0]][fruta[1]] = COLOR_ROJO + var['FRUTA_SYMBOL'] + COLOR_NORMAL  

    #Impresión final del tablero
    for fila in range(TABLERO_SIZE[1]): 
            lst = tablero[fila]
            tableroFinal= ""
            for dot in lst:
                tableroFinal += dot
            print(tableroFinal)

    #Información inferior
    print('')
    print(f"Posición de la fruta: {fruta}")
    print(f"Tablero: {TABLERO_SIZE}")
    print(f"Mover:[w, a, s, d] | Salir:[Espacio/Enter]")