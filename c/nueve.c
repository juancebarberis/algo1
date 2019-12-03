/*
9) Escribir en C un programa que pida al usuario dos palabras. El programa debe impri-
mir ambas palabras en una lı́nea, separadas por una secuencia de puntos de forma tal que la
longitud total de la lı́nea sea de 30 caracteres. Ejemplo:
Primera palabra: Hola
Segunda palabra: Mundo
Hola.....................Mundo
*/

#include<stdio.h>
#include<string.h>
#define MAX_LENGHT 30

void imprimir_treinta(char primera[], char segunda[]){
    int long_ambas = strlen(primera) + strlen(segunda) - 2;
    int i;
    printf("%s", primera);
    for(i = MAX_LENGHT - long_ambas; i != 0; i -= 1){
        printf(".");
    }
    printf("%s", segunda);
    printf("\n");
}

int main(){
    
    char palabra_1[MAX_LENGHT], palabra_2[MAX_LENGHT];
    printf("Ingrese la primera palabra:");
    fgets(palabra_1, MAX_LENGHT, stdin);
    printf("Ingrese la segunda palabra:");
    fgets(palabra_2, MAX_LENGHT, stdin);
    palabra_1[strlen(palabra_1) - 1] = '\0';
    palabra_2[strlen(palabra_2) - 1] = '\0';
    imprimir_treinta(palabra_1, palabra_2);
    return 0;
}
