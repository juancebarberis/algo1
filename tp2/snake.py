# NOMBRE_APELLIDO = JUAN CELESTINO BARBERIS
# PADRON = 105147
# MATERIA = 7540 Algoritmos y Programacion 1, curso Essaya
# TP 2 - Snake++

from modulos.init import *      #Import de todos los módulos.

def main():
    _VARS = cargarVariablesNivel()
    ESP = cargarEspeciales()            
    nivel = 0
    state = True

    while state == True:    #Ciclo del juego
        
        var = _VARS[nivel]  #Carga el diccionario del nivel correspondiente.
        TABLERO_SIZE = (var['TABLERO_COLUMNAS'], var['TABLERO_FILAS'])
        fruta = generarFruta(TABLERO_SIZE)
        movimiento = 'w'
        posCeroCol  = TABLERO_SIZE[0] // 2
        posCeroFil  = TABLERO_SIZE[1] // 2
        snake   = [(posCeroFil, posCeroCol)]
        
        while True:     #Ciclo del nivel

            snake, fruta = checkFruta(movimientoSnake(snake, movimiento), fruta, TABLERO_SIZE)

            if not checkBordes(snake, TABLERO_SIZE) or not checkAutoColision(snake):
                state = jugadorSalir('gameOver')
                break
            if len(snake) == var['SNAKE_MAX_LENGHT']:
                state = jugadorNivelUp(nivel + 1, len(_VARS))
                nivel += 1
                break

            imprimirTablero(generarTablero(TABLERO_SIZE), snake, fruta, TABLERO_SIZE, var)

            entrada = inputJugada(movimiento, float(var['SPEED']))
            if entrada == False:     
                state = jugadorSalir('pressEspace') 
                break    
            if not entrada == None: 
                movimiento = entrada
    print(f'Usted alcanzó el nivel {nivel + 1}')

main()              #Esta línea ejecuta el juego.
