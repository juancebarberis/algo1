#Ejercicio 6.4. Escribir una función que reciba una cadena que contiene un largo número en-
#tero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
#'1234567890' , debe devolver '1.234.567.890'.

def separarMiles(n):
    """Recibe <n> un conjunto de numeros enteros, y devuelve <n> separado en miles."""

    numero = list(n[::-1])
    #exit(numero[::-3])
    for c in range(3, len(n) + 1, 4):
        numero.insert(c, '.')
    return numero[::-1]
    

z = input('Ingrese un numero a convertir en entero:')
call = separarMiles(z)
print(call)
 