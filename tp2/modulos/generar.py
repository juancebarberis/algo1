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

def generarFruta(TABLERO_SIZE):
    """Genera dos coordenadas al azar en un rango hasta <TABLERO_SIZE>.
    Devuelve las coordenadas en una lista."""
    frutaFil = randint(0, TABLERO_SIZE[1] - 1)
    frutaCol = randint(0, TABLERO_SIZE[0] - 1)

    return (frutaFil, frutaCol)