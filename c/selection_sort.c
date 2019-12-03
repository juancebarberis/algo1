/*
Ejercicio 16.8. Implementar una función que recibe un arreglo de números y su longitud y lo
ordena mediante el algoritmo de ordenamiento por selección.
*/

#include<stdio.h>

void selection(int longitud, int * arreglo){
	while(longitud > 0){
		int pos_actual = 0;
		for(int i = 0; i <= longitud; i++){
	  		if(arreglo[pos_actual] < arreglo[i]){
	  			pos_actual = i;
	  		}
		}
		int temporal_final = arreglo[longitud];
		int temporal_actual = arreglo[pos_actual];
		arreglo[longitud] = temporal_actual;
		arreglo[pos_actual] = temporal_final;
		longitud -= 1;
	}
	printf("Sorted\n");
	for(int j = 0; j != 10; j++){
		printf("[%d]", arreglo[j]);
	}
	printf("\n");
}

int main()
{
	int arreglo[] = {1, 5, 6, -2, 12, 10, 3, 2, 9, 8};
	int longitud = 9;
	printf("Unsorted\n");
	for(int j = 0; j != 10; j++){
		printf("[%d]", arreglo[j]);
	}
	printf("\n");
	selection(longitud, arreglo);
	return 0;
}