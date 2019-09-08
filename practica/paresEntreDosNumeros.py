#ej 2.4
def imprimirParesEntreDosNumeros(inferior, superior):
    """Imprime todos los pares entre dos números"""

    for i in range(inferior + inferior % 2, superior + 1, 2):
        print(i)


inferior = int(input('Numero inferior: '))
superior = int(input('Numero superior: '))

funcion = imprimirParesEntreDosNumeros(inferior, superior)