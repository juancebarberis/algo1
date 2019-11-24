/*
Memoria dinamica (malloc, free) -> no entra
Cadenas y punteros (para manejar cadenas) -> entra
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_STRING 255

void pedir_palabra(char pal[]){
	printf("La palabra.\n");
	fgets(pal[], MAX_STRING, stdin);
	pal[strlen(pal) - 1] = '\0';
}

int main(int argc, char** argv[]) {
	char palabra[MAX_STRING];
	pedir_palabra(palabra[]);
	return 0;
}

