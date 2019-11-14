from random import randint
from mapa import *

class IA:
    """
    Inteligencia artificial para resolver un laberinto.

    Se simula un jugador que comienza en la celda de origen, y mediante
    el método avanzar() el jugador hace un movimiento.

    Ejemplo:
        >>> mapa = Mapa(10, 10)
        >>> ia = IA()
        >>> ia.coord_jugador()
        Coord(0, 0)
        >>> while ia.coord_jugador() != mapa.destino()
        ...     ia.avanzar()
        >>> ia.coord_jugador()
        Coord(9, 9)
    """

    def __init__(self, mapa):
        """Constructor.

        Argumentos:
            mapa (Mapa): El mapa con el laberinto a resolver
        """
        self.mapa = mapa
        self.bloquedas = self.mapa.bloqueadas
        self.jugador = self.mapa.origen()
        self.visitadas = []
        self.caminito = []

    def coord_jugador(self):
        """Coordenadas del "jugador".

        Devuelve las coordenadas de la celda en la que se encuentra el jugador.

        Devuelve:
            Coord: Coordenadas del "jugador"

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> ia.coord_jugador()
            Coord(0, 0)
            >>> ia.avanzar()
            >>> ia.coord_jugador()
            Coord(1, 0)
            >>> ia.avanzar()
            >>> ia.coord_jugador()
            Coord(2, 0)
        """
        return self.jugador

    def visitados(self):
        """Celdas visitadas.

        Devuelve:
            secuencia<Coord>: Devuelve la lista (o cualqueir otra secuencia) de
            de celdas visitadas al menos una vez por el jugador desde que
            comenzó la simulación.

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> ia.avanzar()
            >>> ia.avanzar()
            >>> ia.avanzar()
            >>> ia.visitados()
            [Coord(0, 0), Coord(1, 0),  Coord(2, 0)]
        """
        return self.visitadas

    def camino(self):
        """Camino principal calculado.

        Devuelve:
            secuencia<Coord>: Devuelve la lista (o cualqueir otra secuencia) de
            de celdas que componen el camino desde el origen hasta la posición
            del jugador. Esta lista debe ser un subconjunto de visitados().

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> for i in range(6):
            ...     ia.avanzar()
            >>> ia.visitados()
            [Coord(0, 0), Coord(1, 0), Coord(1, 1),  Coord(2, 0),  Coord(3, 0),  Coord(4, 0)]
            >>> ia.camino()
            [Coord(0, 0), Coord(1, 0),  Coord(2, 0),  Coord(3, 0),  Coord(4, 0)]

        Nota:
            La celda actual en la que está el jugador puede no estar en la
            lista devuelta (esto tal vez permite simplificar la
            implementación).
        """
        return self.caminito

    def avanzar(self):
        """Avanza un paso en la simulación.

        Si el jugador no está en la celda destino, y hay algún movimiento
        posible hacia una celda no visitada, se efectúa ese movimiento.
        """
        if self.coord_jugador() != self.mapa.destino():
            celdas_posibles = {}    #Celdas a las que se puede mover la simulación
            celdas_posibles[1] = Coord(self.jugador.fila + 1, self.jugador.columna)
            celdas_posibles[2] = Coord(self.jugador.fila - 1, self.jugador.columna)
            celdas_posibles[3] = Coord(self.jugador.fila, self.jugador.columna + 1)
            celdas_posibles[4] = Coord(self.jugador.fila, self.jugador.columna - 1)
            
            celdas_validas = []   
            for clave in celdas_posibles:
                if celdas_posibles[clave] not in self.bloquedas and celdas_posibles[clave] not in self.visitadas:
                    celdas_validas.append(celdas_posibles[clave])
            
            if len(celdas_validas) == 0:    #Si no hay movimientos válidos
                self.jugador = self.caminito.pop()
            else:
                movimiento = randint(0, len(celdas_validas) - 1)
                self.caminito.append(self.jugador)
                self.jugador = celdas_validas[movimiento]
            self.visitadas.append(self.jugador)

        if self.coord_jugador() == self.mapa.destino():
            return

