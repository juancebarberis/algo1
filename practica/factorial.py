#ej 1.4
def factorial(n):
    """Devuelve el factorial de n"""
    factorial = 1
    for i in range(1, n + 1):    
        factorial *= i

    return print(factorial)

inputFactorial = int(input('Ingrese para factorial: '))
function = factorial(inputFactorial)

for i in range(5):
    valor = int(input('Ingrese un valor: '))
    print(i +1, valor, factorial(valor))