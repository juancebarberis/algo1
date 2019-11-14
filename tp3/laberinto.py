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
    
    for fila in range(filas):
            for columna in range(columnas):
                coord_instancia = Coord(fila, columna)
                mapa.coords.append(coord_instancia)
                if fila in (0, filas - 1) or columna in (0, columnas - 1):  #Comprobación de bordes del mapa
                    mapa.invalidos.append(coord_instancia)
                if fila % 2 != 0 and columna % 2 != 0:  #Celdas vecinas, todas las celdas impares
                    mapa.vecinas.append(coord_instancia)
                mapa.bloqueadas.append(coord_instancia) #Bloqueo de todas las coordenadas
    
    mapa = generar(mapa, mapa.vecinas[0])
    return mapa

def generar(mapa, coord_actual):
    '''
    Algoritmo que utiliza Backtracking para generar un laberinto, sin dejar espacios
    vacíos (de celdas impares) y tiene siempre solución.
    '''
    pila_actual = []
    while len(mapa.vecinas) > 0:    #Mientras no hayan celdas vecinas sin visitar
        mapa.desbloquear(coord_actual)
        for vecina in mapa.vecinas:
            if vecina == coord_actual:
                mapa.vecinas.remove(vecina)
        if len(mapa.vecinas) > 0:
            vecinas_locales = {}    #Celdas vecinas relativas a coord_actual
            vecinas_locales[1] = Coord(coord_actual.fila + 2, coord_actual.columna)
            vecinas_locales[2] = Coord(coord_actual.fila - 2, coord_actual.columna)
            vecinas_locales[3] = Coord(coord_actual.fila, coord_actual.columna + 2)
            vecinas_locales[4] = Coord(coord_actual.fila, coord_actual.columna - 2)
            vecinas_stack = []
            #Comprueba que las celdas vecinas estén bloquedas y estén dentro del mapa.
            for key in vecinas_locales:
                if vecinas_locales[key] in mapa.bloqueadas and vecinas_locales[key] not in mapa.invalidos:
                    vecinas_stack.append(vecinas_locales[key])
        
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
    
