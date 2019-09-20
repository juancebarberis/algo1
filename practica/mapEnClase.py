def map(seq, funcion):
    res = []

    for elem in seq:
        res.append(funcion(elem))
    return res

def por_2(n): return n * 2

seq = [1,2,3,4,5,6,7,8]
print(map(seq, por_2))