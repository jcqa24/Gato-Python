def movplayer(T) :
    while 1:
        a = int(input("Ingresa una casilla donde tirar\n")) - 1
        if a < 0 or a > 8:
            print("Casilla no valida")
        else :
            if T[a] != 'X' and T[a] != 'O':
                T[a] = 'X'
                return a
            else :
               print("La casilla esta ocupada")
