#Funciones que imprimer los elementos visibles del juego

from modulos.terminal import clear_terminal
from modulos.generar import generarTablero

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'

def imprimirTablero(snake, fruta, variables, _ESPECIALES, especialTablero):
    """
    Recibe los componentes del juego y los imprime en el
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
    #Agregar especial de tablero
    if especialTablero:
        tablero[especialTablero['COORDS'][0]][especialTablero['COORDS'][1]] = especialTablero['SYMBOL']
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
    print(f"Velocidad: {variables['SPEED']}")
    print('')
    print('ESPECIALES:')
    print('SIMBOLO  ||TECLA ||CANTIDAD ||DESCRIPCION')
    try:
        for especial in variables['SPECIALS']:
            datos = _ESPECIALES[especial]
            print(f"{especial}        ||{datos['E_KEY']}     ||{datos['E_CANT']}        ||{datos['E_DESC']}")
    except:    
        print('No hay especiales para este nivel :(')
    print(f"{COLOR_VERDE}Mover:{COLOR_NORMAL}[w, a, s, d] | {COLOR_ROJO}Salir:{COLOR_NORMAL}[Espacio/Enter]")