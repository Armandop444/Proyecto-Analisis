import numpy as np
from Utilidades import tablita
from FormulaEngine import convertir_funcion
from sympy import *

def f(xi, yi, funcion):
    valor = 0
    if "x" in funcion:
        funcion = funcion.replace("x", str(xi))
    if "y" in funcion:
        funcion = funcion.replace("y", str(yi))
    valor = eval(funcion)
    return valor

def eulermod(dy, x0, y0, h, muestras):
    
    tabla=tablita(["xi","yi"],show_iteracion=False)
    tamano = muestras+1
    estimado = np.zeros(shape=(tamano, 2), dtype=float)

    # incluye el punto [x0,y0]
    estimado[0] = [x0, y0]
    tabla.add_fila(estimado[0])
    xi = x0
    yi = y0
    for i in range(1, tamano, 1):
        k=yi+h*f(xi,yi,dy)

        yi = yi+(h/2)*(f(xi,yi,dy)+f(xi+h,k,dy))
        xi = xi + h

        estimado[i] = [xi, yi]
        tabla.add_fila(estimado[i])
    tabla.print_table()
    return (estimado)

def euler():
    dy=input("Ingrese y'")
    dy=convertir_funcion(dy)

    x0 = float(input("ingrese X0\n"))
    y0 = float(input("ingrese Y0\n"))
    h = float(input("ingrese h\n"))
    i=x0
    muestras=0
    pregunta = input(
        "Como quiere operar\n1.Con # de iteraciones\n2.Evaluacion en un punto de f(x)")
    if pregunta == "2":
        xF = float(input("Ingrese el punto de f(x)"))
        muestras = 0
        while i < xF:
            muestras = muestras+1
            i += h
    else:
        muestras = int(input("Ingrese el # de iteraciones que desea hacer"))

    # PROCEDIMIENTO
    eulermod(dy, x0, y0, h, muestras)
euler()