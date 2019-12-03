from mapa import *
from random import randint

def generar_laberinto(filas, columnas):
    """Generar un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """
    
    mapa = Mapa(filas, columnas)
    vecinas = []
    for coord_instancia in mapa: 
        if coord_instancia.fila % 2 != 0 and coord_instancia.columna % 2 != 0:  #Celdas vecinas, todas las celdas impares
            vecinas.append(coord_instancia)
    
    mapa = generar(mapa, vecinas[0], vecinas)
    return mapa

def generar(mapa, coord_actual,vecinas):
    '''
    Algoritmo que utiliza Backtracking para generar un laberinto, sin dejar espacios
    vacíos (de celdas impares) y tiene siempre solución.
    '''
    pila_actual = []
    while len(vecinas) > 0:    #Mientras no hayan celdas vecinas sin visitar
        mapa.desbloquear(coord_actual)
        for vecina in vecinas:
            if vecina == coord_actual:
                vecinas.remove(vecina)
        if len(vecinas) > 0:
            vecinas_locales = []    #Celdas vecinas relativas a coord_actual
            vecinas_locales.append(Coord(coord_actual.fila + 2, coord_actual.columna))
            vecinas_locales.append(Coord(coord_actual.fila - 2, coord_actual.columna))
            vecinas_locales.append(Coord(coord_actual.fila, coord_actual.columna + 2))
            vecinas_locales.append(Coord(coord_actual.fila, coord_actual.columna - 2))
            
            vecinas_stack = []
            #Comprueba que las celdas vecinas estén bloquedas y estén dentro del mapa.
            for coordenada in vecinas_locales:
                if mapa.celda_bloqueada(coordenada) and mapa.es_coord_valida(coordenada):
                    vecinas_stack.append(coordenada)
        
            if len(vecinas_stack) >= 1:
                vecina_random = randint(0, len(vecinas_stack) - 1)
                vecina = vecinas_stack[vecina_random]

                celda_intermedia = Coord((coord_actual.fila + vecina.fila)/2, (coord_actual.columna + vecina.columna)/2)
                
                mapa.desbloquear(vecina)
                mapa.desbloquear(celda_intermedia)
                if len(vecinas_stack) > 1:
                    pila_actual.append(coord_actual)
                coord_actual = vecina
            
            elif len(pila_actual) is not 0: 
                coord_actual = pila_actual.pop()

    return mapa
    
