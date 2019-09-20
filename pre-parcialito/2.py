#3) Escribir una funci´on que pida cadenas al usuario hasta que ingrese una cadena vac´ıa.
#Debe devolver una lista de las palabras ingresadas. Por ejemplo:
#Cadena: hola co
#Cadena: mo
#Cadena: estas ?
#Cadena:
#Debe devolver: [’hola’, ’como’, ’estas’, ’?’]

def pedirCadenas():
    """"""

    resultado = []
    cadena = ''

    while True:
        entrada = input('Cadena:')

        if entrada == '':
            resultado = cadena.split()                    
            break

        cadena += entrada
    
    return resultado

print(pedirCadenas())