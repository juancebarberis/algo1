
#include<stdio.h>

#define N 10

int factorial(int n);

int main() {
	int resultado = factorial(N);
	printf("El factorial de %d es %d\n", N, resultado);
	return 0;
}
/*
//Funcion iterativa
int factorial(int n){
	int i;
	int resultado = 1;
	for(i = n; i != 0; i--){
		resultado *= i;
	}
	return resultado;
}
*/
//Funcion recursiva
int factorial(int n){
	if(n != 0){
	  return factorial(n - 1) * n;	
	}
	return 1;
	}

	


