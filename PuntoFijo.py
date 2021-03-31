from FormulaEngine import convertir_funcion
from math import *
from tabulate import tabulate
from Utilidades import raiz

def PuntoFijo(funcion, es, x):
    ea = 100
    funcion = convertir_funcion(funcion)
    contenido = []
    i = 1
    while ea > es:
        xn = eval(funcion)
        ea = abs((xn-x)/xn) * 100
        contenido.append([i,x,xn,ea])
        print(f"{x}  | {xn}   | {ea}")
        x = xn
        i += 1
    print(tabulate(contenido, headers= ["Iteracion", "X","g(X)","EA"],tablefmt="orgtbl"))
