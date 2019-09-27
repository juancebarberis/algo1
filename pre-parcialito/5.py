#Escribir una funci´on que reciba dos secuencias y devuelva una lista con los elementos
#comunes a ambas, sin repetir ninguno.

secA = [1, 2, 3, 4, 7, 8, 9]
secB = [5, 4, 1, 2, 5, 2]

#Resultado [1, 2, 4]

def valoresComunes(A, B):
    """Recibe dos secuencias y devuelve una lista con los elementos en común
    en ambas secuencias (sin repetir)."""
    resultado = []
    
    for elementA in A:
        for elementB in B:
            print(f'Comparando {elementA} | {elementB}')
            if elementA == elementB:
                if elementA in resultado or elementB in resultado:
                    continue
                else:resultado.append(elementA)
    return resultado

print(valoresComunes(secA, secB))