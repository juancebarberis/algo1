/*
10) Escribir en C un programa que pida al usuario que ingrese 10 números enteros e imprima
el mı́nimo, el máximo y el promedio.
*/

#include<stdio.h>
#define MAX 10

int minimo(int arreglo[]){
    int min = arreglo[0];
    int i;
    for(i = 1; i != MAX; i++){
        if(arreglo[i] < min){
            min = arreglo[i];
        }
    }
    return min;
}

int maximo(int arreglo[]){
    int max = arreglo[0];
    int i;
    for(i = 1; i != MAX; i++){
        if(arreglo[i] > max){
            max = arreglo[i];
        }
    }
    return max;
}

int promedio(int arreglo[]){
    int i;
    int prom;
    for(i = 0; i != MAX; i++){
        prom += arreglo[i];
    }
    return prom / 10;
}

int main(){
    int arreglo_numeros[MAX];
    
    for(int i = 0; i != MAX; i++){
        printf("Registro %d -> ",i);
        char entrada[MAX];
        fgets(entrada, MAX, stdin);
        printf("\n");
        arreglo_numeros[i] = atoi(entrada);
    }
    printf("Mínimo:%d\n",minimo(arreglo_numeros));
    printf("Máximo:%d\n",maximo(arreglo_numeros));
    printf("Promedio:%d\n",promedio(arreglo_numeros));
    return 0;
}