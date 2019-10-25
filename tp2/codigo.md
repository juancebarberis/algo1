## main.py
```python

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

```

## _loader.py

```python

#Modulo de carga. 
#Se encarga de cargar todos los imports necesarios para que el juego funcione.

from random import randint
from modulos.check import *
from modulos.generar import *
from modulos.imprimir import *
from modulos.input import *
from modulos.movimiento import *
from modulos.jugador import *
from modulos.cargar import *
from modulos.terminal import clear_terminal, timed_input

```

## cargar.py

```python
#Modulo que interactua con los archivos del juego. 
#Niveles y especiales, interactuan con las funciones de este módulo.

import csv

KEYS_DE_NIVEL = (   #Keys de nivel que son obligatorias para que el juego funcione.
    'LEVEL',
    'SNAKE_MAX_LENGHT',
    'TABLERO_COLUMNAS',
    'TABLERO_FILAS',
    'SPEED',
    'SNAKE_SYMBOL',
    'FRUTA_SYMBOL'
    )

def cargarVariablesNivel():
    '''
    Realiza la carga inicial de todos los niveles del juego
    y los devuelve en una lista de diccionarios.
    Cada diccionario en la lista representa a un nivel.
    '''
    nivel = 1
    variablesDeNivel = []
    print('Cargando niveles de juego...')
    while True:
        try:
            with open('config/niveles/nivel_' + str(nivel) + '.txt', mode='r') as archivoNivel:
                dictIndividual = {}
                dictIndividual['LEVEL'] = nivel
                for linea in archivoNivel.readlines():
                    l = linea.rstrip()
                    if l.startswith('#') or not linea.strip(): continue 
                    if ':' in l: 
                        parametro = l.split(':')
                        try:
                            dictIndividual[parametro[0]] = int(parametro[1])
                        except:
                            dictIndividual[parametro[0]] = parametro[1]
                #Casos especiales.
                dictIndividual['TABLERO_SIZE'] = (dictIndividual['TABLERO_COLUMNAS'], dictIndividual['TABLERO_FILAS'])
                try:
                    dictIndividual['SPECIALS'] = dictIndividual['SPECIALS'].split(',')
                except:
                    dictIndividual['SPECIALS'] = []
                #Fin de casos especiales.
                variablesDeNivel.append(dictIndividual)
                nivel += 1
        except:
            if nivel == 1: 
                print(f'No existen niveles cargados en el juego.')
                return None
            break
    if comprobarKeys(variablesDeNivel, nivel):
        return variablesDeNivel

def comprobarKeys(listaDeDiccionarios, nivel):
    '''
    Recibe una lista de diccionarios y comprueba que todas las keys
    necesarias para que el juego funcione, existan.
    Devuelve False en caso de faltar una key.
    '''
    print(f'Comprobando variables de nivel...')
    for nivel in range(nivel-1):
        for key in KEYS_DE_NIVEL:
            if key not in listaDeDiccionarios[nivel]:
                print(f'Error al cargar {key} en nivel {nivel + 1}')
                return False
    return True

def cargarEspeciales():
    '''
    Realiza la carga inicial de todos los especiales que se encuentran en
    /config/especiales.csv
    Devuelve un diccionario de diccionarios, donde la key del diccionario padre
    es el símbolo del especial.
    '''
    especiales = {}
    cantidadDeFilas = 0
    with open('config/especiales.csv') as espFile:
        espRead = csv.reader(espFile)
        for fila in espRead:
            cantidadDeFilas += 1
            especiales[fila[0]]  = {
                                    'E_SYMBOL': fila[0],
                                    'E_TYPE': fila[1],
                                    'E_VALUE': fila[2],
                                    'E_CANT': 0,
                                    'E_KEY': fila[3],
                                    'E_DESC': fila[4],
                                    }    
        especiales['TOTAL'] = cantidadDeFilas                           
    return especiales
```

## generar.py

```python
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

def generarFruta(variables):
    """Genera dos coordenadas al azar en un rango hasta <TABLERO_SIZE>.
    Devuelve las coordenadas en una lista.
    Comprueba que la fruta generada, no esté en la misma posición que un
    obstáculo. De ser así, genera otra."""
    TABLERO_SIZE = variables['TABLERO_SIZE']
    frutaFil = randint(0, TABLERO_SIZE[1] - 1)
    frutaCol = randint(0, TABLERO_SIZE[0] - 1)
    fruta = (frutaFil, frutaCol)
    try:
        obstaculos = variables['OBSTACLE'].split(';')
        for obstaculo in obstaculos:
                coordObstaculo = obstaculo.split(',')
                tuplaObstaculo = (int(coordObstaculo[0]), int(coordObstaculo[1]))
                if tuplaObstaculo == fruta:
                    frutaFil = randint(0, TABLERO_SIZE[1] - 1)
                    frutaCol = randint(0, TABLERO_SIZE[0] - 1)
                    fruta = (frutaFil, frutaCol)
    except:
        obstaculos = None
    return fruta

def generarEspecial(variables, especiales, fruta):
    '''
    Genera un diccionario con una coordenada aleatoria y selecciona
    aleatoriamente un especial de dicho nivel que se mostrará en el tablero.
    '''
    if variables['SPECIALS'] == [] or variables['SPECIALS'][0] == '':
        return False     #No hay especiales en este nivel.

    TABLERO_SIZE = variables['TABLERO_SIZE']
    randomSymbol = randint(0, len(variables['SPECIALS']) - 1)
    Fil = randint(0, TABLERO_SIZE[1] - 1)
    Col = randint(0, TABLERO_SIZE[0] - 1)
    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    try:
        obstaculos = variables['OBSTACLE'].split(';')
        for obstaculo in obstaculos:
                coordObstaculo = obstaculo.split(',')
                tuplaObstaculo = (int(coordObstaculo[0]), int(coordObstaculo[1]))
                if tuplaObstaculo == especial:
                    Fil = randint(0, TABLERO_SIZE[1] - 1)
                    Col = randint(0, TABLERO_SIZE[0] - 1)
                    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    except:
        obstaculos = None
    if fruta == especial:
                    Fil = randint(0, TABLERO_SIZE[1] - 1)
                    Col = randint(0, TABLERO_SIZE[0] - 1)
                    especial = {'COORDS': (Fil, Col), 'SYMBOL': variables['SPECIALS'][randomSymbol]}
    return especial
```

## imprimir.py

```python 
#Funciones que imprimer los elementos visibles del juego

from modulos.terminal import clear_terminal
from modulos.generar import generarTablero

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'
COLOR_AMARILLO = '\033[93m'
COLOR_AZUL = '\033[94m'

def imprimirTablero(snake, fruta, variables, _ESPECIALES, especialTablero):
    """
    Recibe los componentes del juego y los imprime en el
    orden y posiciones correspondientes.
    """
    tablero = generarTablero(variables['TABLERO_SIZE'])
    clear_terminal()
    #Agrega Snake al tablero
    for coord in snake:             
        tablero[coord[0]][coord[1]] = COLOR_VERDE + variables['SNAKE_SYMBOL'] + COLOR_NORMAL
    #Agrega la fruta al tablero
    try:
        tablero[fruta[0]][fruta[1]] = COLOR_ROJO + variables['FRUTA_SYMBOL'] + COLOR_NORMAL  
    except:
        print('Error al colocar la fruta.')
    #Agregar Obstaculos al tablero
    try:
        obstaculos = variables['OBSTACLE'].split(';')
        for obstaculo in obstaculos:
            coordenadasObstaculo = obstaculo.split(',')
            try:
                tablero[int(coordenadasObstaculo[0])][int(coordenadasObstaculo[1])] = COLOR_AZUL + '#' + COLOR_NORMAL
            except:
                continue
    except:
        obstaculos = None
    #Agregar especial de tablero
    if especialTablero:
        tablero[especialTablero['COORDS'][0]][especialTablero['COORDS'][1]] = COLOR_AMARILLO + especialTablero['SYMBOL'] + COLOR_NORMAL
    #Información superior
    print("SNAKE++")
    print(f"Nivel: {variables['LEVEL']}  |  Tamaño: {len(snake)}")
    #Impresión final del tablero
    for fila in range(variables['TABLERO_SIZE'][1]): 
            lst = tablero[fila]
            tableroFinal= ""
            for dot in lst:
                tableroFinal += dot
            print(tableroFinal)
    #Información inferior
    print('')
    print(f"Velocidad: {variables['SPEED']}")
    print('')
    print('ESPECIALES:')
    print('SIMBOLO  ||TECLA ||CANTIDAD ||DESCRIPCION')
    try:
        for especial in variables['SPECIALS']:
            datos = _ESPECIALES[especial]
            print(f"{especial}        ||{datos['E_KEY']}     ||{datos['E_CANT']}        ||{datos['E_DESC']}")
    except:    
        print('No hay especiales para este nivel :(')
    print(f"{COLOR_VERDE}Mover:{COLOR_NORMAL}[w, a, s, d] | {COLOR_ROJO}Salir:{COLOR_NORMAL}[Espacio/Enter]")
```

## input.py

```python
#Este módulo contiene funciones del tipo input que intervienen en la jugabilidad
#y el movimiento de Snake.

from modulos.terminal import timed_input

def inputJugada(movimiento, variables, _ESPECIALES, snake):
    """
    Comprueba lo ingresado por el usuario desde el teclado.
    Evalúa si pertenece a un movimiento, un especial, o a un cierre del juego.
    """
    entrada = timed_input(float(variables['SPEED']))
    #Condicionales de 'salir del juego'.
    if entrada.isspace():   #Para salir del juego, presiona <SPACE>
        return False, variables, snake, _ESPECIALES  
    #Condicionales de movimiento
    if entrada == 'w' and not movimiento == 's': 
        return entrada, variables, snake, _ESPECIALES
    elif entrada == 'a' and not movimiento == 'd':
        return entrada, variables, snake, _ESPECIALES
    elif entrada == 's' and not movimiento == 'w':
        return entrada, variables, snake, _ESPECIALES
    elif entrada == 'd' and not movimiento == 'a':
        return entrada, variables, snake, _ESPECIALES
    #Condicionales de especiales
    especiales = variables['SPECIALS']
    if especiales == [] or especiales[0] == '':
        return movimiento, variables, snake, _ESPECIALES
    for i in range(len(especiales)):
        if entrada == _ESPECIALES[especiales[i]]['E_KEY'] and int(_ESPECIALES[especiales[i]]['E_CANT']) > 0:
            if _ESPECIALES[especiales[i]]['E_TYPE'] == 'VELOCIDAD':
                velocidad = float(variables['SPEED'])
                velocidad += float(_ESPECIALES[especiales[i]]['E_VALUE'])
                variables['SPEED'] = str(velocidad)
                _ESPECIALES[especiales[i]]['E_CANT'] = int(_ESPECIALES[especiales[i]]['E_CANT'])-1
                break
            if _ESPECIALES[especiales[i]]['E_TYPE'] == 'LARGO':
                if len(snake) == 1:
                    break
                if int(_ESPECIALES[especiales[i]]['E_VALUE']) == -1:
                    snake.pop(-1)
                if int(_ESPECIALES[especiales[i]]['E_VALUE']) == 1:
                    if movimiento == 'w': snake.insert(0, (snake[0][0] - 1, snake[0][1]))
                    if movimiento == 's': snake.insert(0, (snake[0][0] + 1, snake[0][1]))
                    if movimiento == 'a': snake.insert(0, (snake[0][0], snake[0][1] - 1))
                    if movimiento == 'd': snake.insert(0, (snake[0][0], snake[0][1] + 1))
                _ESPECIALES[especiales[i]]['E_CANT'] = int(_ESPECIALES[especiales[i]]['E_CANT'])-1
                break
    return movimiento, variables, snake, _ESPECIALES
```

## jugador.py

```python
#Este módulo contiene funciones que interactuan directamente con el jugador.

from modulos.terminal import clear_terminal, timed_input
from modulos.cargar import cargarEspeciales

COLOR_VERDE = '\033[92m'
COLOR_ROJO = '\033[91m'
COLOR_NORMAL = '\033[0m'

def jugadorSalir(motivo):
    """
    Limpia la terminal e imprime un mensaje acorde al motivo
    de finalización del juego.
    """
    if motivo == 'pressEspace':
        clear_terminal()
        print(f'{COLOR_VERDE}¡Gracias por jugar!{COLOR_NORMAL}')
        return False

    if motivo == 'gameOver':
        clear_terminal()
        print(f'{COLOR_ROJO}¡Game Over! :({COLOR_NORMAL}')
        return False
    
    if motivo == 'loadError':
        print(f'{COLOR_ROJO}Error a la hora de cargar los archivos necesarios para ejecutar el juego.{COLOR_NORMAL}')

def jugadorNivelUp(nivelActual, ultimoNivel):
    '''
    El jugador sube de nivel.
    '''
    clear_terminal()
    print('¡Felicidades! Completaste el nivel.')
    print('')
    print('')
    inputNull = ''
    print('Presione cualquier tecla para continuar.')
    while inputNull == '':
        inputNull = timed_input(0.1)
    if nivelActual == ultimoNivel: 
        return False
    return True

def jugadorLimpiarEspeciales(especiales):
    '''
    Limpia la cantidad de especiales disponibles para el siguiente nivel.
    '''
    return cargarEspeciales()
```

## movimiento.py

```python

def movimientoSnake(snake, movimiento):
    """Recibe <SNAKE> y un <MOVIMIENTO>. Agrega una nueva pieza en la
    dirección que recibe por <MOVIMIENTO>. Devuelve <SNAKE> con la nueva pieza."""

    if movimiento == "w": 
        snake.insert(0, (snake[0][0] - 1,snake[0][1]))
    if movimiento == "s":
        snake.insert(0, (snake[0][0] + 1,snake[0][1]))
    if movimiento == "a": 
        snake.insert(0, (snake[0][0],snake[0][1] - 1))
    if movimiento == "d": 
        snake.insert(0, (snake[0][0],snake[0][1] + 1))
    
    return snake
```

## terminal.py

(No se modificó nada, es el mismo que facilitó la cátedra).