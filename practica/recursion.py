def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

def invertir_cola(cola):
    if cola.esta_vacia():
        return
    e = cola.desencolar()
    invertir_cola(cola)
    cola.encolar(e)

def fibonacci(n):
    return _fibonacci(n, {0: 0, 1: 1})

def _fibonacci(n, d):
    if n in d:
        return d[n]
    d[n] = _fibonacci(n - 1, d) + _fibonacci(n - 2, d)
    print(d)
    return d[n]