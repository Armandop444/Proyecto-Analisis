#import numpy as np
from numpy import sqrt, linspace
from sympy import symbols, parse_expr, Subs
from FormulaEngine import convertir_funcion
# cuadratura de Gauss de dos puntos
def integraCuadGauss2p(fx,a,b):
    x = symbols('x')
    x0 = -1/sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(fx.subs(x,xa) + fx.subs(x,xb))
    return(area)

def gauss():
    # INGRESO
    ecuacion = input("ingrese la funcion\n")

    x = symbols('x')  # declaramos que x es un simbolo

    ecuacion=convertir_funcion(ecuacion)

    fx = parse_expr(ecuacion)  # funcion que evaluaremos
    #fx = lambda x: (np.exp(x)*np.sin(x))/(1+x**2)

    # intervalo de integración
    a = float(input("ingrese el punto a de la integral\n"))
    b = float(input("ingrese el punto b de la integral\n"))
    tramos = int(input("cuantos puntos desea evaluar\n"))


    # PROCEDIMIENTO
    muestras = tramos+1
    xi = linspace(a,b,muestras)
    area = 0
    for i in range(0,muestras-1,1):
        deltaA = integraCuadGauss2p(fx,xi[i],xi[i+1])
        area = area + deltaA
    # SALIDA
    print('Integral: ', area)
