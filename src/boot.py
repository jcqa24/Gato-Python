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
    pass

def Mov(T):
    pass
    #    C = [5,1,2]
#    for c in C:
        
