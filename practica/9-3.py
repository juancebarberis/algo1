#Ejercicio 9.3. Continuación de la agenda.
#Escribir un programa que vaya solicitando al usuario que ingrese nombres.
#a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
#el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
#b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#El usuario puede utilizar la cadena ”*”, para salir del programa.

AGENDA = {
    'aaa': '123456789',
    'bbb': '987239874',
    'ccc': '203984209'
}

def main(agenda):

    while True:
        entrada = input('Ingrese un nombre:')

        if entrada == "*": break

        if entrada in agenda:
            print(f"{entrada}, número: {agenda[entrada]}")

            ask = input('¿Desea modificar el número? [y/n]:')
            if ask == 'y':
                agenda[entrada] = input('Ingrese el número nuevo:')
                print(f'Número de {entrada} actualizado.')

            print('')
            
    return True

main(AGENDA)
