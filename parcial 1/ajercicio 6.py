def polinomio(x):
    return ((np.e)**(-x))*(-x)

#h=0.05

def muller(f,x,h):
    #h=0.05
    #a=f(x[0],x[1],x[2]) 
    #a = ( f(x[1],x[2])-f(x[0], x1) )/h
    a = ((((f(x[2])-f(x[1]))/h)-((f(x[1])-f(x[0]))/h))/h)
    b = ((f(x[1])-f(x[0]))/h)-((x[1]+x[0])*((((f(x[2])-f(x[1]))/h)-((f(x[1])-f(x[0]))/h))/h))
    c = f(x[0])+x[0]*((f(x[2])-f(x[1]))/h)+x[0]*x[1]*((((f(x[2])-f(x[1]))/h)-((f(x[1])-f(x[0]))/h))/h)
    return ([((-2*c)/(b+np.sqrt((b)**2-4*(a)*(c)))),((-2*c)/(b-np.sqrt((b)**2-4*(a)*(c))))])


x_3 = muller(polinomio, X,0.0001)

while np.abs(x_3[1]-x_3[0]) > 10e-3:
    x_1=x_3[1]
    x_33=x_3[0]
    x_2=(x_1+x_33)/2
    T=[x_1,x_2,x_33]
    x_3 = muller(polinomio,T,0.0001)
    print(x_3)
