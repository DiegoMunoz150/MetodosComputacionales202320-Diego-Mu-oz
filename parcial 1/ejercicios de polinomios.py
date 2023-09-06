import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym

def polinomio (x):
    return 3*x**5+5*x**4-x**3

X=np.linspace(-2,2)


def derivda_inicial (po,x,h):
    return (po(x+h)-po(x))/h


def newton(x_0,po,epsilon):
    x_n=x_0
    while np.abs(po(x_n)) > epsilon: 
        x_n -= po(x_n)/derivda_inicial(po,x_n,0.0001)
        print(x_n,po(x_n))
    return x_n
