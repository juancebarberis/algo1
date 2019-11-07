from mapa import *

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
                if (fila % 2 == 0 and columna % 2 == 0) or fila in (0, filas - 1) or columna in (0, columnas - 1):
                    mapa.bloqueadas.append(coord_instancia)
    return mapa
