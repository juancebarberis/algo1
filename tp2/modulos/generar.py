#Funciones que generan elementos a partir de parámetros recibidos.

from random import randint

def generarFruta(variables):
    """Genera dos coordenadas al azar en un rango hasta <TABLERO_SIZE>.
    Devuelve las coordenadas en una tupla.
    """
    TABLERO_SIZE = variables['TABLERO_SIZE']
    frutaFil = randint(0, TABLERO_SIZE[1] - 1)
    frutaCol = randint(0, TABLERO_SIZE[0] - 1)
    fruta = (frutaFil, frutaCol)
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
        for obstaculo in variables['OBSTACLE']:
                while obstaculo == especial:
                    Fil = randint(0, TABLERO_SIZE[1] - 1)
                    Col = randint(0, TABLERO_SIZE[0] - 1)
                    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    except:
        pass
    while fruta == especial:
                    Fil = randint(0, TABLERO_SIZE[1] - 1)
                    Col = randint(0, TABLERO_SIZE[0] - 1)
                    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    return especial