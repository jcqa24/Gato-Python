def BuscarC1(T,c):
    if T[0] == c :
        if T[1] == c and T[2] == c :
            return 1
        if T[3] == c and T[6] == c:
            return 1
    return 0


def BuscarC9(T,c):
    if T[8] == c:
        if T[5] == T[2] == c :
            return 1
        if T[7] == T[6] == c :
            return 1
    return 0

def BuscarC5(T,c):
    if T[4] == c :
        if T[3] == T[5] == c :
           return 1
        if T[1] == T[7] == c :
            return 1
        if T[0] == T[8] == c :
            return 1
        if T[2] == T[6] == c :
            return 1
    return 0


def ganador(T,g) :
    if g == 1 :
        if  BuscarC1(T,'X') :
            return 1
        if BuscarC9(T,'X') :
            return 1
        if BuscarC5(T,'X') :
            return 1
    else :
        if  BuscarC1(T,'O') :
            return 1
        if BuscarC9(T,'O') :
            return 1
        if BuscarC5(T,'O') :
            return 1
    return 0

