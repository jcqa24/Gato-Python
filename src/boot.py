def boot(T,B,P):
    a = MovGanar(T,B) 
    if a :
        return a
    b = MovPerder(T,P) 
    if b :
        return b
    c =  Mov(T)
    if c :
        return c
    return 0

def MovGanar(T,B):
    if ( 0 in B ) and (1 in B):
        if T[2] != "O" and T[2] != "X" :
            T[2] = "O"
            return 2
    return False
        
def MovPerder(T,P):
    if 0 in P:
        if 3 in P:
            T[6] = "O"
            return 6
        if 6 in P:
            T[3] = "O"
            return 3
        if 1 in P:
            T[2] = "O"
            return 2
        if 2 in P:
            T[1] = "O"
            return 1
        if 4 in P:
            T[8] = "O"
            return 8
        if 8 in P:
            T[4] = "O"
            return 4
    return False
def Mov(T):
    C = [4,0,2,6,8,1,3,5,7]
    for c in C:
        if T[c] != "X" and T[c] != "O":
            T[c]="O"
            return c
        
