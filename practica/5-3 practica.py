#Ejercicio 5.3. Manejo de contraseñas
#a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
#rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
#b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
#tos.
#c) Modificar el programa anterior para que después de cada intento agregue una pausa
#cada vez mayor, utilizando la función sleep del módulo time .
#d) Modificar el programa anterior para que sea una función que devuelva si el usuario
#ingresó o no la contraseña correctamente, mediante un valor booleano ( True o False ).

PASS = 'contra'
INTENTOS = 3

def logIn(contrasena):
    logIn = contrasena
    for i in range(INTENTOS - 1):
        if logIn == PASS:
            return True
        else:
            logIn = input('Contraseña: ')
    return False

def main():
    
    start = logIn(input('Contraseña: '))

    if not start:
        exit('Adiós! Excedió el límite de intentos.')

    print('Bienvenido!!!')

main()



