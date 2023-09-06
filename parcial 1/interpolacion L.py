def lix(X,i):
    P=1
    x=sym.symbols('x')
    for k in range(0,len(X)):
        if k != i:
            P=P*(x-X[k])/(X[i]-X[k])
    return (P)

#print(lix(o,0))

def Lix(Y,X,f):
    L=0
    for i in range(0,len(Y)):
        L += Y[i]*f(X,i)

    return(L)

print(Lix(l,o,lix))