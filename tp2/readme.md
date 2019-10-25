
<div style=" margin-top:3em; 
             margin-bottom:2.6em ">
    <div style="text-align:center;">
        <h1 style="border-bottom: 1px solid black;">
            Informe<br> 
            Snake++ <br>
        </h1>
        <h3>
            75.40 Algoritmos y Programacion I<br>
            Cátedra Essaya<br>
        </h3>
    </div>
    <h4 style=" font-weight:300;
                margin-top:3em;">
        Alumno: Barberis, Juan Celestino<br> 
        Padrón: 105147 <br>
        Corrector: Javier Di Santo
    </h4>
</div>

## Diseño del programa

### Estructura de datos

El programa realiza una carga inicial de los niveles y especiales, y almacena en memoria los mismos para ser utilizados de manera eficiente. 
Para los niveles ser utiliza texto plano, con la extensión .txt y los especiales en .csv.
Se implementó de esta manera ya que son archivos fáciles de leer desde Python, en especial los archivos CSV, para los cuales utilicé la librería nativa: csv.

Una vez que los datos se encuentran en memoria, estos se organizan principalmente en diccionarios, ya que el sistema de key:value es muy eficiente y facilita mucho el utilizar los datos en el código.

### Añadiendo funcionalidades.

Snake++ está basado en Snake (primer TP), por lo que se reutilizó el código base para implementar todas las características solicitadas en la consigna. La dificultad inicial fue modularizar todo el código y al final, que ese código no se convierta en un 'spaghetti code'. 

La cantidad de líneas código comparado con el anterior trabajo práctico es mayor, por lo que es necesaria una documentación más extensa y específica para que el corrector no enloquezca durante la lectura.

De haber sabido que el código de mi primer Snake iba a ser reutilizado y repotenciado para el siguiente TP, hubiese hecho uso de mayor cantidad de funciones auxiliares, para facilitar el trabajo en algunos aspectos.

## Conclusión

Trabajo práctico muy entretenido como siempre, fue todo una experiencia repotenciar mi anterior código para ampliarlo en funcionalidades.

