#Funciones que generan elementos a partir de parámetros recibidos.

from random import randint

def generarTablero(TABLERO_SIZE):
    """Genera el tablero base de juego a partir de <TABLERO_SIZE>
    que recibe en forma de tupla."""
    tablero = []
    for fil in range(TABLERO_SIZE[1]):
        tablero.append([])
        for col in range(TABLERO_SIZE[0]):
            tablero[fil].append('.') 
    return tablero

def generarFruta(variables):
    """Genera dos coordenadas al azar en un rango hasta <TABLERO_SIZE>.
    Devuelve las coordenadas en una lista.
    Comprueba que la fruta generada, no esté en la misma posición que un
    obstáculo. De ser así, genera otra."""
    TABLERO_SIZE = variables['TABLERO_SIZE']
    frutaFil = randint(0, TABLERO_SIZE[1] - 1)
    frutaCol = randint(0, TABLERO_SIZE[0] - 1)
    fruta = (frutaFil, frutaCol)
    try:
        obstaculos = variables['OBSTACLE'].split(';')
        for obstaculo in obstaculos:
                coordObstaculo = obstaculo.split(',')
                tuplaObstaculo = (int(coordObstaculo[0]), int(coordObstaculo[1]))
                if tuplaObstaculo == fruta:
                    frutaFil = randint(0, TABLERO_SIZE[1] - 1)
                    frutaCol = randint(0, TABLERO_SIZE[0] - 1)
                    fruta = (frutaFil, frutaCol)
    except:
        obstaculos = None
    return fruta

def generarEspecial(variables, especiales, fruta):
    '''
    Genera un diccionario con una coordenada aleatoria y selecciona
    aleatoriamente un especial de dicho nivel que se mostrará en el tablero.
    '''
    if variables['SPECIALS'] == [] or variables['SPECIALS'][0] == '':
        return False     #No hay especiales en este nivel.

    TABLERO_SIZE = variables['TABLERO_SIZE']
    randomSymbol = randint(0, len(variables['SPECIALS']) - 1)
    Fil = randint(0, TABLERO_SIZE[1] - 1)
    Col = randint(0, TABLERO_SIZE[0] - 1)
    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    try:
        obstaculos = variables['OBSTACLE'].split(';')
        for obstaculo in obstaculos:
                coordObstaculo = obstaculo.split(',')
                tuplaObstaculo = (int(coordObstaculo[0]), int(coordObstaculo[1]))
                if tuplaObstaculo == especial:
                    Fil = randint(0, TABLERO_SIZE[1] - 1)
                    Col = randint(0, TABLERO_SIZE[0] - 1)
                    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    except:
        obstaculos = None
    if fruta == especial:
                    Fil = randint(0, TABLERO_SIZE[1] - 1)
                    Col = randint(0, TABLERO_SIZE[0] - 1)
                    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    return especial