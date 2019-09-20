#1) Escribir una funci´on que reciba por par´ametro una lista de n´umeros y devuelva otra lista
#con los n´umeros de la ingresada que terminan en cero. Por ejemplo, si se recibe la lista: [4, 23,
#40, -7, 0, 14, 1000, -760] debe devolver [40, 0, 1000, -760].

def soloTerminanEnCero(lista):
    """"""
    resultado = []
    for n in lista:
        numero = str(n)
        if numero[:-2:-1] == '0':
            resultado.append(n)
    return resultado

numeros = [1, 2, 4, 0, 30, 21, 500, 3, 5000]

print(soloTerminanEnCero(numeros))
