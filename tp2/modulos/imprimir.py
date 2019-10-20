#Funciones que imprimer los elementos visibles del juego

from modulos.terminal import clear_terminal
from modulos.generar import generarTablero

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'

def imprimirTablero(snake, fruta, variables):
    """
    Recibe los componentes del juego (Tablero, Snake y Fruta) y los imprime en el
    orden y posiciones correspondientes.
    """
    tablero = generarTablero(variables['TABLERO_SIZE'])
    clear_terminal()
    #Agrega Snake al tablero
    for coord in snake:             
        tablero[coord[0]][coord[1]] = COLOR_VERDE + variables['SNAKE_SYMBOL'] + COLOR_NORMAL
    #Agrega la fruta al tablero
    try:
        tablero[fruta[0]][fruta[1]] = COLOR_ROJO + variables['FRUTA_SYMBOL'] + COLOR_NORMAL  
    except:
        print('Error al colocar la fruta.')
    #Agregar Obstaculos al tablero
    try:
        obstaculos = variables['OBSTACLE'].split(';')
        for obstaculo in obstaculos:
            coordenadasObstaculo = obstaculo.split(',')
            try:
                tablero[int(coordenadasObstaculo[0])][int(coordenadasObstaculo[1])] = '@'
            except:
                continue
    except:
        obstaculos = None
    #Información superior
    print("SNAKE++")
    print(f"Nivel: {variables['LEVEL']}  |  Tamaño: {len(snake)}")
    print('')
    #Impresión final del tablero
    for fila in range(variables['TABLERO_SIZE'][1]): 
            lst = tablero[fila]
            tableroFinal= ""
            for dot in lst:
                tableroFinal += dot
            print(tableroFinal)
    #Información inferior
    print('')
    print(f"Posición de la fruta: {fruta}")
    print(f"Posición de la snake: {snake}")
    print(f"Tablero: {variables['TABLERO_SIZE']}")
    print(f"{COLOR_VERDE}Mover:{COLOR_NORMAL}[w, a, s, d] | {COLOR_ROJO}Salir:{COLOR_NORMAL}[Espacio/Enter]")