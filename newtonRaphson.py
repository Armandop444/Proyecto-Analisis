from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import pandas as pd
import numpy as np
from tabulate import tabulate
from Utilidades import tablita


x = symbols('x')

def NewtonR(func, xi, es):
    tabla = tablita(["xi","f(xn)","df(xn)","d2f(xn)","x(n+1)","ea"])
    itera = 0
    dfx=diff(func)
    d2fx=diff(dfx)
    xa=0
    d2fxn=0.0
    dfxn=0.0
    fxn=0.0
    xnmas1=0.0
    ea=100.0
    convergencia=0.0
    fxn = func.subs(x,xi)
    fxn=float(fxn)
    dfxn = dfx.subs(x,xi)
    dfxn=float(dfxn)
    d2fxn = d2fx.subs(x,xi)
    d2fxn=float(d2fxn)
    convergencia=Abs((fxn*d2fxn)/(dfxn**2))

    if convergencia<1 :
        print("condicion de convergencia>0  cumplido, la convergencia es: ")
        print(convergencia)
        print("")
        while ea > es:
            if itera==0:
                xa=xi
                fxn = func.subs(x,xi)
                fxn=float(fxn)
                dfxn = dfx.subs(x,xi)
                dfxn=float(dfxn)
                d2fxn = d2fx.subs(x,xi)
                d2fxn=float(d2fxn)
                xnmas1=xi-(fxn/dfxn)
                ea=(Abs((xnmas1-xi)/xnmas1))*100
            else:
                xa=xnmas1
                fxn = func.subs(x,xa)
                fxn=float(fxn)
                dfxn = dfx.subs(x,xa)
                dfxn=float(dfxn)
                d2fxn = d2fx.subs(x,xa)
                d2fxn=float(d2fxn)
                xnmas1=xa-(fxn/dfxn)
                ea=(Abs((xnmas1-xa)/xnmas1))*100
            itera=itera+1
            tabla.add_fila([xa,fxn,dfxn,d2fxn,xnmas1,ea])
        print("la raiz es: {}".format(xnmas1))   
        return tabla.get_tabla()
        
    else:
        print("la convergencia es mayor que 0:\n" )
        return convergencia

#xi es igual a 0.5 para este ejercicio
#xf=float(input("ingrese el valor de xinicial\n"))
#funcion="(((x**2)+1)**(1/2))-tan(x)"
#a = NewtonR(parse_expr(funcion), xf, 1)
#print(a)