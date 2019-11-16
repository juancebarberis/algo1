#include<stdio.h>

int promedio_array(int array, int n){
	int i;
	int suma;
	for(i = 0; i != n; i++){
		suma += array[i];
	}
	return suma/n;
}

const numero = 5;
const arreglo[] = {19, 10, 8, 17, 9};

int main(){
	int promedio = promedio_array(arreglo, numero);
	printf("El promedio de el arreglo es: %d\n", promedio);
	return 0;
}
