#Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
#a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
#'s,e,p,a,r,a,r'
#b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
#debería devolver 'mi_archivo_de_texto.txt'
#c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
#'X' debería devolver 'su clave es: XXXX'
#d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
#'255.255.255.0'

def intercalar(cadena, caracter):
    """..."""
    intercalado = ''
    for s in cadena:
        intercalado += s + caracter
    print(intercalado[:-1]) 

def intercalarCopado(cadena, caracter):
    return caracter.join(cadena)

def ocultar(cadena):
    """..."""
    oculto = ''
    for s in cadena:
        if s.isdigit():
            oculto += 'X'
        
    return oculto 

def ocultarConLista(cadena):
    caracteres = list(cadena)

    for i in range(len(caracteres)):
        c = caracteres[i]
        if c.isdigit():
            caracteres[i] = 'X'
  
    return ''.join(caracteres)
            

entradaCadena = input('Ingrese cadena: ')
#entradaCaracter = input('Ingrese caracter: ')
#intercalar(entradaCadena, entradaCaracter)
#print(intercalarCopado(entradaCadena, entradaCaracter))
print('A lo salvaje ' + ocultar(entradaCadena))
print('Con lista ' + ocultarConLista(entradaCadena))

