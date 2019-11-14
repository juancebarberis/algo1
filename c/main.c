#include <stdio.h>

int sumar(int x, int y);

int main() {
	int arreglo[] = {1, 22, 3};
	printf(arreglo[1]);
	return 0;
} 

int sumar(int x, int y) {
	return x + y;
}