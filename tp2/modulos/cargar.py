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