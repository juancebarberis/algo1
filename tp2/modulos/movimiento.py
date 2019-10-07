
def movimientoSnake(snake, movimiento):
    """Recibe <SNAKE> y un <MOVIMIENTO>. Agrega una nueva pieza en la
    dirección que recibe por <MOVIMIENTO>. Devuelve <SNAKE> con la nueva pieza."""

    if movimiento == "w": 
        snake.insert(0, (snake[0][0] - 1,snake[0][1]))
    if movimiento == "s":
        snake.insert(0, (snake[0][0] + 1,snake[0][1]))
    if movimiento == "a": 
        snake.insert(0, (snake[0][0],snake[0][1] - 1))
    if movimiento == "d": 
        snake.insert(0, (snake[0][0],snake[0][1] + 1))
    
    return snake