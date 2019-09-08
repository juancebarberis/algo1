#Ejercicio 2.7. Escribir un programa que imprima por pantalla todas las fichas de dominó, de
#una por línea y sin repetir.

for i in range(0,7):
    for j in range(i, 7):
        print(i, ' - ', j)