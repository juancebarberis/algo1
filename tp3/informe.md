<div style=" margin-top:3em; 
             margin-bottom:2.6em ">
    <div style="text-align:center;">
        <h1 style="border-bottom: 1px solid black;">
            Informe<br> 
            Backtracking <br>
        </h1>
        <h3>
            75.40 Algoritmos y Programacion I<br>
            Cátedra Essaya<br>
        </h3>
    </div>
    <h4 style=" font-weight:300;
                margin-top:3em;">
        Grupo: B7 <br> 
        Integrantes: GUTIERREZ, SERENA
y BARBERIS, JUAN CELESTINO <br>
        Corrector: Javier Di Santo
    </h4>
</div>


# Diseño del programa:
El laberinto funciona gracias a la implementación y el funcionamiento de tres módulos principales que entre sí realizan distintas funciones. 


En primer lugar, el módulo laberinto se encarga de generar, mediante un algoritmo de backtracking iterativo, un laberinto que siempre tiene solución y no deja espacios vacíos. 


El segundo módulo ia, es el encargado de resolver mediante una “inteligencia artificial”, el laberinto generado. Se encarga de recorrer caminos al azar recordando por donde pasó y marcando un camino por donde es posible pasar, si llega a un punto sin salida, vuelve sobre sus pasos hasta poder tomar otro camino. 


El tercer módulo es el programado por la cátedra, que se encarga de juntar todo lo demás y ponerlo a funcionar y graficar los elementos en pantalla. De este módulo no se tocó nada (así lo decía el enunciado).


Y por último, se implementan las clases que comunican los módulos entre sí, se encuentran en el archivo mapa.py que fueron implementadas por nosotros.



## Estructura de datos:
Implementamos los métodos de las clases Mapa y Coord de manera tal que el programa se ejecute de manera correcta en relación al código que el módulo tp3.py requiere. Siguiendo la documentación de las funciones indicadas, los datos están estructurados en forma de listas (generalmente) implementadas ya por Python. Alguna de ellas son utilizadas en forma de pilas para los algoritmos de generación y de resolución del laberinto. 
