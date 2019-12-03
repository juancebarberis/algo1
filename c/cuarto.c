//Ejercicio 3 del parcialito cuatro.

#include<stdio.h>
#include<string.h>
#define MAX_LENGHT 16
#define PASS "essaya19"

int main(){
    char entrada[MAX_LENGHT];
    printf("Por favor, ingrese su clave:");
    fgets(entrada, MAX_LENGHT, stdin);
    entrada[strlen(entrada) - 1] = '\0';
    while(strcmp(entrada, PASS) != 0){
        if(strcmp("*",entrada) == 0){
            printf("Usted ha salido del sistema.\n");
            return 0;
        }
        printf("\n");
        printf("Clave incorrecta. Escriba * para cancelar, o vuelva a intentarlo:");
        fgets(entrada, MAX_LENGHT, stdin);
        entrada[strlen(entrada) - 1] = '\0';
    }
    printf("Bienvenido/a al sistema.\n");
    return 0;
}