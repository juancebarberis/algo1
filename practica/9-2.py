#Ejercicio 9.2. Diccionarios usados para contar.

#a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
#de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
#hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1} .

#a)

def main(texto):
    """"""
    resultado = {}
    for palabra in texto.split():
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado

print(main('que lindo dia que hace hoy'))