#Modulo que interactua con los archivos del juego. 
#Niveles y especiales, interactuan con las funciones de este módulo.

import csv

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
                variablesDeNivel.append(dictIndividual)
                print('¡Nivel ' + str(nivel) + ' cargado exitosamente!')   #Solo para DEBUG
                nivel += 1
        except Exception as e:
            if nivel == 1: 
                print(f'No existen niveles cargados en el juego. {e}')
                variablesDeNivel = None
            break

    if comprobarKeys(variablesDeNivel):
        return variablesDeNivel

def comprobarKeys(listaDeDiccionarios):
    '''
    Recibe una lista de diccionarios y comprueba que todas las keys
    necesarias para que el juego funcione, existan.
    Devuelve False en caso de faltar una key.
    '''
    return False

def cargarEspeciales():
    return True