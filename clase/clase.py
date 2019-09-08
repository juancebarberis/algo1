#2-9-19 clase de booleanos y condicionales

#Ejercicio 4.6. Suponiendo que el primer día del año fue lunes, escribir una función que reciba
##un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
##si recibe '3' debe devolver 'miércoles' , si recibe '9' debe devolver 'martes' .

def diaSemana(n):
    """"""
    resto = n % 7
    if resto == 0: return 'Domingo'
    if resto == 1: return 'Lunes'
    if resto == 2: return 'Martes'
    if resto == 3: return 'Miercoles'
    if resto == 4: return 'Jueves'
    if resto == 5: return 'Viernes'
    if resto == 6: return 'Sábado'

entrada = input()

salida = print(diaSemana(entrada))


#Ejercicio 4.5. Escribir funciones que resuelvan los siguientes problemas:
#a) Dado un año indicar si es bisiesto.
#Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
#excepto que también sea divisible por 400.
"""
def es_bisiesto(year):
    """"Dado un año, devuelve True si ese año es bisiesto.""""
    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0

entrada = int(input('Año: '))
call = es_bisiesto(entrada)
print(call)
"""
#Ejercicio 4.1. Escribir dos funciones que resuelvan los siguientes problemas:
#a) Dado un número entero n, indicar si es par o no.
"""
def es_par(n):
    """"Dado un n, devuelve True si es par.""""
    if n % 2 == 0:
        return True

print('Verificar si un número es par.')

nInput = int(input('Ingrese un número a verificar: ') or exit()) 

if es_par(nInput) == True:
    print('El número ingresado es par :D')
else:
    print('El número ingresado no es par :(')
"""

#b) Dado un número entero n, indicar si es primo o no.
"""
def es_primo(n):
    """"Dado un n, devuelve True si es primo.""""
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
        
print('Verificar si un número es primo.')

nInput = int(input('Ingrese un número a verificar: ') or exit()) 

print(es_primo(nInput))
"""