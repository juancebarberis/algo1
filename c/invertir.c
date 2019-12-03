/*5) Escribir en C una función que pida al usuario que ingrese una cadena y la imprima
invertida.
*/

#include<stdio.h>
#include<string.h>
#define MAX_LENGHT 20

void imprimir_invertida(char cadena[], int longitud){
    int i;
    printf("Longitud:%d\n", longitud);
    printf("Cadena invertida:");
    for(i = longitud - 1; i != -1; --i){
        printf("%c",cadena[i]);
    }
    printf("\n");
}

int main(){
    char cadena[MAX_LENGHT];
    printf("Ingrese una cadena:");
    fgets(cadena, MAX_LENGHT, stdin);
    imprimir_invertida(cadena, strlen(cadena));
    return 0;
}