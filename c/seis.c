/*
6) Escribir en C un programa que pida al usuario un valor mı́nimo, un valor máximo y un
número n, e imprima una tabla con los cuadrados de los números entre mı́nimo y máximo cada
n números. Por ejemplo (mı́nimo = 0, máximo = 17, n = 5) debe mostrar:
0 0
5 25
10 100
15 225
*/

#include<stdio.h>
#include<string.h>
#define MAX_LENGHT 10

void imprimir_tabla_cuadrados(int min, int max, int n){
    int i;
    for(i = min; i < max + 1; i += n){
        printf("%d | %d \n", i, i * i);
    }
}

int main() {
    //Pedir números
    char min[MAX_LENGHT], max[MAX_LENGHT], n[MAX_LENGHT];
    printf("Ingrese un mínimo:");
    fgets(min, MAX_LENGHT, stdin);
    printf("Ingrese un máximo:");
    fgets(max, MAX_LENGHT, stdin);
    printf("Ingrese un n:");
    fgets(n, MAX_LENGHT, stdin);
    printf("\n");
    imprimir_tabla_cuadrados(atoi(min), atoi(max), atoi(n));
    return 0;
}