
from modulos.generar import generarFruta, generarEspecial

def checkColision(snake, variables):
    """Recibe <SNAKE>. Comprueba que la nueva posición no esté fuera de los límites
    del tablero o que no colisione contra un obstaculo del nivel.
     Devuelve <False> en caso de estar fuera de los límites."""
    TABLERO_SIZE = variables['TABLERO_SIZE']
    #Comprobación de Snake con los bordes.
    if snake[0][0] == -1 or snake[0][1] == -1:
        return False
    if snake[0][0] == TABLERO_SIZE[1] or snake[0][1] == TABLERO_SIZE[0]:
        return False
    #Comprobación de Snake con los obstaculos.
    try:
        obstaculos = variables['OBSTACLE'].split(';')
        for obstaculo in obstaculos:
                coordObstaculo = obstaculo.split(',')
                tuplaObstaculo = (int(coordObstaculo[0]), int(coordObstaculo[1]))
                if snake[0] == tuplaObstaculo:
                    return False
    except:
        obstaculos = None
    return True

def checkAutoColision(snake):
    """Recibe <SNAKE>. Comprueba que la nueva posición no esté sobre otra parte del
    cuerpo de la serpiente. Devuelve <False> en caso de colisionar consigo misma."""
    cabezaSnake = snake[0]
    for i in range(2,len(snake)):
        if snake[i] == cabezaSnake: return False
    return True

def checkFruta(snake, fruta, variables):
    """Recibe <SNAKE> con la nueva pieza de movimientoSnake() y la posición de
    la <FRUTA>. Comprueba si la nueva pieza está en la misma posición de la fruta.
    Si las posiciones coinciden, genera una nueva fruta con generarFruta() y no
    elimina la última pieza de <SNAKE>. De lo contrario, elimina la última pieza de <SNAKE>.
    Devuelve <SNAKE> y <FRUTA>"""
    
    if snake[0] == fruta: 
        fruta = generarFruta(variables)
    else: 
        snake.pop(-1)
        
    return snake, fruta

def checkEspecialTablero(snake, especialTablero, especiales, variables, fruta):
    '''
    Comprueba que Snake haya activado un especial, de ser así, genera un nuevo especialTablero
    y agrega una unidad al especial correspondiente.
    '''
    if not especialTablero: #Si el nivel no tiene especiales
        return snake, especialTablero, especiales
    
    if snake[0] == especialTablero['COORDS']:
        cantidad = int(especiales[especialTablero['SYMBOL']]['E_CANT']) 
        cantidad += 1
        especiales[especialTablero['SYMBOL']]['E_CANT'] = str(cantidad)
        especialTablero = generarEspecial(variables, especiales, fruta)
    return snake, especialTablero, especiales

