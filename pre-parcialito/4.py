#Escribir un programa que pida al usuario que ingrese un total de 16 n´umeros, y luego
#los imprima en 4 columnas y 4 filas.

def main(datos):
    """"""
    lista = list(datos)
    print(lista[0:4])    
    print(lista[4:8])    
    print(lista[8:12])    
    print(lista[12:16])    

while True:
    entrada = input('Ingrese 16 números:')
    if not len(entrada) == 16 or not entrada.isdigit():
         continue
    main(entrada)