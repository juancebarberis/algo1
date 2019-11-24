#include<stdbool.h>
#include<stdio.h>
#include<stdlib.h>

/*
Recibe un arreglo con un /0 al final y calcula la cantidad de elementos que tiene le arreglo
*/

int len(char* arreglo[]){
    int suma = 0;
    for(int i = 1; arreglo[i] != 0; i++){
        printf("%ld\n", sizeof(arreglo[i]));
        suma += 1;
    }
    return suma;
}

int main(int argc, char* argv[]){
    printf("La cantidad de elementos en el arreglo es: %d\n", len(argv));
    return 0;
}


