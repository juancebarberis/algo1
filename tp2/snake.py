# NOMBRE_APELLIDO = JUAN CELESTINO BARBERIS
# PADRON = 105147
# MATERIA = 7540 Algoritmos y Programacion 1, curso Essaya.
# TP 2 - Snake++

from modulos._loader import *      #Import de todos los módulos.

def main():
    _VARIABLES = cargarVariablesNivel()
    _ESPECIALES = cargarEspeciales()  
    if _VARIABLES == None or _ESPECIALES == None: 
        return jugadorSalir('loadError')  
    cantidadNiveles = len(_VARIABLES)
    nivel = 0
    state = True

    while state == True:    #Ciclo de juego.
        #Variables iniciales de cada nivel.
        variables = _VARIABLES[nivel]  #Carga el diccionario del nivel correspondiente.
        fruta = generarFruta(variables)
        especialTablero = generarEspecial(variables, _ESPECIALES, fruta)
        movimiento = 'w'
        TABLERO_SIZE = variables['TABLERO_SIZE']
        posCeroCol  = TABLERO_SIZE[0] // 2
        posCeroFil  = TABLERO_SIZE[1] // 2
        snake   = [(posCeroFil, posCeroCol)]
        
        while True:     #Ciclo de nivel.

            snake, fruta = checkFruta(movimientoSnake(snake, movimiento), fruta, variables)
            snake, especialTablero, _ESPECIALES = checkEspecialTablero(snake, especialTablero, _ESPECIALES, variables, fruta)
            #Comprobación de colisiones de snake con el entorno.
            if not checkColision(snake, variables) or not checkAutoColision(snake):
                state = jugadorSalir('gameOver')
                break
            #Comprobación de nivel.
            if len(snake) == variables['SNAKE_MAX_LENGHT']:
                state = jugadorNivelUp(nivel + 1, cantidadNiveles)
                _ESPECIALES = jugadorLimpiarEspeciales(_ESPECIALES)
                nivel += 1
                break
            #Impresión general.
            imprimirTablero(snake, fruta, variables, _ESPECIALES, especialTablero)
            #Entradas por teclado.
            entrada, variables, snake, _ESPECIALES = inputJugada(movimiento, variables, _ESPECIALES, snake)
            if entrada == False:     
                state = jugadorSalir('pressEspace') 
                break    
            if not entrada == None: 
                movimiento = entrada

    if nivel > 0:
        print(f'Usted alcanzó hasta el nivel {nivel + 1}')
        print('Gracias por jugar.')

try:
    main()            #Esta línea ejecuta el juego.
except KeyboardInterrupt:
    clear_terminal()
except Exception as e:
    print(f'Algo salió mal...')
    print(f'Reporte el siguiente error: {e}')
    print('a juancebarberis@gmail.com')