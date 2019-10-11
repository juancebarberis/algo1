# NOMBRE_APELLIDO = JUAN CELESTINO BARBERIS
# PADRON = 105147
# MATERIA = 7540 Algoritmos y Programacion 1, curso Essaya.
# TP 2 - Snake++

from modulos.loader import *      #Import de todos los módulos.

def main():
    _VARIABLES = cargarVariablesNivel()
    _ESPECIALES = cargarEspeciales()  
    if _VARIABLES == None or _ESPECIALES == None: 
        return jugadorSalir('loadError')  
    cantidadNiveles = len(_VARIABLES)
    #cantidadEspeciales = len(_ESPECIALES)        #¡No todavía!
    nivel = 0
    state = True

    while state == True:    #Ciclo de juego
        
        variables = _VARIABLES[nivel]  #Carga el diccionario del nivel correspondiente.
        TABLERO_SIZE = (variables['TABLERO_COLUMNAS'], variables['TABLERO_FILAS'])
        fruta = generarFruta(TABLERO_SIZE)
        movimiento = 'w'
        posCeroCol  = TABLERO_SIZE[0] // 2
        posCeroFil  = TABLERO_SIZE[1] // 2
        snake   = [(posCeroFil, posCeroCol)]
        
        while True:     #Ciclo de nivel

            snake, fruta = checkFruta(movimientoSnake(snake, movimiento), fruta, TABLERO_SIZE)

            if not checkBordes(snake, TABLERO_SIZE) or not checkAutoColision(snake):
                state = jugadorSalir('gameOver')
                break
            if len(snake) == variables['SNAKE_MAX_LENGHT']:
                state = jugadorNivelUp(nivel + 1, cantidadNiveles)
                nivel += 1
                break

            imprimirTablero(generarTablero(TABLERO_SIZE), snake, fruta, TABLERO_SIZE, variables)

            entrada = inputJugada(movimiento, float(variables['SPEED']))
            if entrada == False:     
                state = jugadorSalir('pressEspace') 
                break    
            if not entrada == None: 
                movimiento = entrada
    if nivel > 0:
        print(f'Usted alcanzó hasta el nivel {nivel + 1}')

main()              #Esta línea ejecuta el juego.
