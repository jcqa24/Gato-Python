def movplayer(T) :
    a = int(input("Ingresa una casilla donde tirar\n")) - 1
    if T[a] != 'X' and T[a] != 'O':
        T[a] = 'X'

