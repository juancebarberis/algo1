n = 3
secuencia = [1, "hola", True, None, 'elemento!', 324521] 
#print([x**2 for x in range(10)])

def f(x):
    return x ** 3

def es_par(x):
    if x % 2 == 0:
        return True

#print(list([f(x) for x in range(10) if es_par(x)]))

#print(list([1 if i == j else 0 for i in range(n)] for j in range(n)))

for i,e in enumerate(secuencia):
    print(f"Elemento:{e}, Índice:{i}")