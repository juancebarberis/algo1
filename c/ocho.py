'''
8) Escribir una función recursiva que reciba una cadena y devuelva True si es un palı́ndromo
(se lee igual hacia adelante que hacia atrás) o False si no lo es.
neuquen
'''

def es_palindromo(cadena):
    '''
    Recibe: una cadena de texto.

    Devuelve: True si la palabra es un palíndromo, False en caso contrario.
    '''
    indice = 0
    return _es_palindromo(cadena, indice)

def _es_palindromo(cadena, indice):
    if indice == len(cadena) // 2:
        return True
    if cadena[indice] == cadena[len(cadena) - 1 - indice]:
        indice += 1
        return _es_palindromo(cadena, indice)
    return False

entrada = input("Ingrese una cadena:")
print(es_palindromo(entrada))