#include <stdio.h>
#include <stdlib.h>
#define HOLA "juancito"

const char NOMBRE[] = {"juan es un crack"};
int main(int argc, char* argv[]){
    printf("%s\n", NOMBRE);
        printf("Hola mi nombre es " HOLA "\n");
    for(int i = 1; i<argc; i++){
        
        printf("El argumento numero %d es el %d\n", i, atoi(argv[i]));
    }
    return 0;
}
