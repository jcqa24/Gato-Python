import random

def basic(T):
    print("Tiro de boot")
    if T[4] != 'X' and T[4] != 'O' :
        T[4] = 'O'
        return 4
    else :
        while 1 :
            b = random.randint(0,8)
            if T[b] != 'X' and T[b] != 'O' :
                T[b] = 'O'
                return b
