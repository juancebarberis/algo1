#3) Escribir una funci´on que reciba una palabra y devuelva una lista con todas las rotaciones
#de esa palabra. Por ejemplo, si recibe: ’rotar’, debe devolver:
#[’rotar’,’otarr’,’tarro’,’arrot’,’rrota’]

def rotacionesDeUnaPalabra(palabra):
    """"""
    res = []
    for i in range(len(palabra)):
        res.append(palabra[::-1])
    return res

entrada = input('Ingrese una palabra:')
print(rotacionesDeUnaPalabra(entrada))