#Ejercicio 7.10. Matrices.
#a) Escribir una función que reciba dos matrices y devuelva la suma.
#b) Escribir una función que reciba dos matrices y devuelva el producto.
#c) ⋆ Escribir una función que opere sobre una matriz y mediante eliminación gaussiana de-
#vuelva una matriz triangular superior.
#d) ⋆ Escribir una función que indique si un grupo de vectores, recibidos mediante una
#lista, son linealmente independientes o no.

A = [(2,1), (4,1)]
B = [(4,0), (2,8)]

def sumarMatrices(A, B):
    """"""
    resultado = []
    for i in range(len(A)):
        nuevaFila = []
        for e in range(len(A[i])):
            nuevaFila.append(A[i][e] + B[i][e])
        resultado.append(nuevaFila)
    return resultado

print('A')
for fila in A:
    print(fila)
print('B')
for fila in B:
    print(fila)
print('Resultado!:')
res = sumarMatrices(A, B)

print(f"{res[0]}")
print(f"{res[1]}")
