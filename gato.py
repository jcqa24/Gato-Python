from src.view import imp
from src.basicboot import basic
from src.player import movplayer
from src.search import ganador 
from src.boot import boot
def nivel():
    print("Seleciona el nivel a jugar")
    print("1 - Nivel Facil")
    print("2 - Nivel Medio")
    print("3 - Nivel Dificil")
    return int(input())
    

def main() :
    T = ["1","2","3","4","5","6","7","8","9"]
    B = []
    P = []
    l = nivel()
    turnos = 0
    #1 - Player , 2 = boot
    player = 1
    g = 0
    imp(T)

    while (turnos <= 9) :
        if player == 1 :
            P.append(movplayer(T))
            g = ganador(T,player)
            if g :
                print("Ganaste!!!!!")
                imp(T)
                break
            player = 2
        else :
            if l == 1 :
                basic(T)
            elif l == 2:
                boot(T,B,P)
            else :
                print("BooT en construccion")
            g = ganador(T,player)
            if g :
                print("Perdiste")
                imp(T)
                break
            player = 1
        print("Tiros boot -> ",B)
        print("Tiros Jugador -> ",P)
        turnos += 1
        imp(T)


if __name__ == "__main__":
    main()
