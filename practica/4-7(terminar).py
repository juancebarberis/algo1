#Ejercicio 4.7. ⋆ Escribir un programa que reciba como entrada un entero representando un
#año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números
#romanos.

def aRomanos(n):
    if 1 <= n <= 9:
        c1 = n%10
        c2 = 0
        c3 = 0
        c4 = 0
    elif 10 <= n <= 99:
        c1 = n%10
        c2 = (n%100 - c1) / 10
        c3 = 0
        c4 = 0
    elif 100 <= n <= 999:
        c1 = n%10
        c2 = (n%100 - c1) / 10
        c3 = (n%100 - c1 - c2*10) / 100
        c4 = 0
    else:
        c1 = n%10
        c2 = (n%100 - c1) / 10
        c3 = (n%100 - c1 - c2*10) / 100
        c4 = (n%100 - c1 - c2 - c3) / 1000
    

entrada = int(input('Ingrese un número (hasta 4 digitos): '))
salida = aRomanos(entrada)

print(salida)