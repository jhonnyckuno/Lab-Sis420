import random

laberinto = []

for pocicionFila in range( 0, 7 ):
    fila = []
    for pocicionColumna in range(0,11):
        fila.append("#")
    laberinto.append(fila)

filaAleatoria = random.randint(0,6)
columnaAleatoria = random.randint(0,10)

laberinto[ filaAleatoria ][ columnaAleatoria ] = " "

numeroParedes = 30
numeroEspacios = 77 - numeroParedes

x = filaAleatoria
y = columnaAleatoria

# ----
while True:
    if(numeroEspacios == 1):
        break

    arriba = [x-1, y]
    abajo = [x+1, y]
    izquierda = [x, y-1]
    derecha = [x, y+1]

    movientos = [arriba, abajo, izquierda, derecha]

    numeroAleatorio = random.randint(0,3)

    sgtMovimiento = movientos[ numeroAleatorio ]

    while True:
        if( sgtMovimiento[0] >= 0 and sgtMovimiento[0] < 7 and sgtMovimiento[1] >= 0 and sgtMovimiento[1] < 11):

            if(laberinto[ sgtMovimiento[0] ] [ sgtMovimiento[1] ] == "#"):
                laberinto[sgtMovimiento[0]][sgtMovimiento[1]] = " "
                x = sgtMovimiento[0]
                y = sgtMovimiento[1]
                numeroEspacios = numeroEspacios - 1
                break
            elif( laberinto[ sgtMovimiento[0] ] [ sgtMovimiento[1] ] == " " ):
                x = sgtMovimiento[0]
                y = sgtMovimiento[1]
                break
        else:
            numeroAleatorio = random.randint(0,len(movientos)-1 )
            sgtMovimiento = movientos[ numeroAleatorio ]

    # print("----------------")
    # for fila in laberinto:
    #     print("".join(fila))




for fila in laberinto:
    print("".join(fila))
