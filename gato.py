import random


def imp(T):
    print("\n")
    print(" "+T[0]+" | "+T[1]," | ",T[2])
    print("------------")
    print(" "+T[3]+" | "+T[4]," | ",T[5])
    print("------------")
    print(" "+T[6]+" | "+T[7]," | ",T[8]) 
    print("\n")

def movboot(T):
    print("Tiro de boot")
    if T[4] != 'X' and T[4] != 'O' :
        T[4] = 'O'
        return 1
    else :
        while 1 :
            b = random.randint(0,8)
            if T[b] != 'X' and T[b] != 'O' :
                T[b] = 'O'
                return 1

def movplayer(T) :
    a = int(input("Ingresa una casilla donde tirar\n")) - 1
    if T[a] != 'X' and T[a] != 'O':
        T[a] = 'X'

def BuscarC1(T,c):
    print("#")
    if T[0] == c :
        if T[1] == c and T[2] == c :
            return 1
        if T[3] == c and T[6] == c:
            return 1
    return 0




def ganador(T,g) :
    if g == 1 :
        return  BuscarC1(T,'X')
    return 0


T = ["1","2","3","4","5","6","7","8","9"]

turnos = 0
#1 - Player , 2 = boot
player = 1
g = 0
imp(T)

while (turnos <= 9) and (g == 0) :
    if player == 1 :
        movplayer(T)
        g = ganador(T,player) 
        print(g)
        player = 2
    else :
        movboot(T)
        g = ganador(T,player) 
        print(g)
        player = 1
    turnos += 1
    imp(T)

