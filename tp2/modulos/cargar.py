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
    print('Cargando niveles de juego.')
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
                print('¡Nivel ' + str(nivel) + ' cargado exitosamente!')
                nivel += 1
        except Exception as e:
            if nivel == 1: 
                print('No existen niveles cargados en el juego.')
                variablesDeNivel = None
            break
    return variablesDeNivel

def cargarEspeciales():
    return True