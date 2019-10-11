#11 de Octubre de 2019

class Fraccion:
    '''
    Documentación.
    '''
    def __init__(self, num, den):
        '''.'''
        self.num = num
        self.den = den

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, otra):
        denominador = self.den * otra.den
        numerador = self.num * otra.den + otra.num * self.den
        return Fraccion(numerador, denominador)

fr1 = Fraccion(1, 4)
fr2 = Fraccion(3, 5)

print(fr1 + fr2)