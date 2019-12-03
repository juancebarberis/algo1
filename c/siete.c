/*
7) Escribir en C una programa que le solicite un número entero al usuario y muestre por
pantalla si el número ingresado es un número primo o no.
*/

#include<stdio.h>
#define MAX_LENGHT 10

//Devuelve 1 si es primo, 0 en caso contrario.
int es_primo(int n){
    int i;
    for(i = n - 1; i != 1;i -= 1){
        if(n % i == 0){
            printf("Divisible por %d\n", i);
            return 0;
        }
    }
    return 1;
}

int main(){
    char cadena[MAX_LENGHT];
    printf("\nIngrese un número:");
    fgets(cadena, MAX_LENGHT, stdin);
    if(es_primo(atoi(cadena)) == 1){
        printf("El número es primo.\n");
    }else{
        printf("El número no es primo.\n");
    }
    return 0;
}