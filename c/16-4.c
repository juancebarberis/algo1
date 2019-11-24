/*
Ejercicio 16.4. Usando las funciones printf y sizeof , escribir un programa que imprima el
tamaño en bytes de cada uno de los siguientes tipos: bool , char , short , int , long , float , double ,
bool* , char* , short* , int* , long* , float* , double* .
*/

#include<stdio.h>
#include<stdbool.h>

int main(){
    printf("%ld\n",sizeof(int));
    printf("%ld\n",sizeof(bool));
    printf("%ld\n",sizeof(char));
    printf("%ld\n",sizeof(short));
    printf("%ld\n",sizeof(long));
    printf("%ld\n",sizeof(float));
    return 0;
}