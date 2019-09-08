#Ejercicio 2.5. Escribir un programa que le pregunte al usuario un número n e imprima los
#primeros n números triangulares, junto con su índice. Los números triangulares se obtienen
#mediante la suma de los números naturales desde 1 hasta n.

def numeroTriangular(numero):
    """Funcion que recibe un número y devuelve su Numero Triangular"""
    triangular = 0
    for i in range(1, numero + 1):
        triangular += i
    return triangular

#print de información
print('Ingrese un número entero para calcular su triangular.')

#input que le pregunta al usuario un número n
n = int(input('Ingrese un número: '))

#Ciclo for
for i in range(1, n + 1):
    
    print(i, '-', numeroTriangular(i))