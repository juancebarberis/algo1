
from modulos.generar import generarFruta

def checkBordes(snake, TABLERO_SIZE):
    """Recibe <SNAKE>. Comprueba que la nueva posición no esté fuera de los límites
    del tablero. Devuelve <False> en caso de estar fuera de los límites."""

    if not (snake[0][0] == -1 or snake[0][1] == -1 or snake[0][0] == TABLERO_SIZE[1] or snake[0][1] == TABLERO_SIZE[0]): 
        return True

def checkAutoColision(snake):
    """Recibe <SNAKE>. Comprueba que la nueva posición no esté sobre otra parte del
    cuerpo de la serpiente. Devuelve <False> en caso de colisionar consigo misma."""
    cabezaSnake = snake[0]
    for i in range(2,len(snake)):
        if snake[i] == cabezaSnake: return False
    return True

def checkFruta(snake, fruta, TABLERO_SIZE):
    """Recibe <SNAKE> con la nueva pieza de movimientoSnake() y la posición de
    la <FRUTA>. Comprueba si la nueva pieza está en la misma posición de la fruta.
    Si las posiciones coinciden, genera una nueva fruta con generarFruta() y no
    elimina la última pieza de <SNAKE>. De lo contrario, elimina la última pieza de <SNAKE>.
    Devuelve <SNAKE> y <FRUTA>"""
    
    if snake[0] == fruta: 
        fruta = generarFruta(TABLERO_SIZE)
    else: 
        snake.pop(-1)
        
    return snake, fruta