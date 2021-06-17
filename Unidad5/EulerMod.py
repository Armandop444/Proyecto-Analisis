import numpy as np
from Utilidades import tablita
from FormulaEngine import convertir_funcion
from sympy import *

def eulermod(d1y, x0, y0, h, muestras):
    
    tabla=tablita(["xi","yi"],show_iteracion=False)
    tamano = muestras+1
    estimado = np.zeros(shape=(tamano, 2), dtype=float)

    # incluye el punto [x0,y0]
    estimado[0] = [x0, y0]
    xi = x0
    yi = y0
    for i in range(1, tamano, 1):
        k=yi+h*d1y(xi,yi)

        yi = yi+(h/2)*(d1y(xi,yi)+d1y(xi+h,k))
        xi = xi + h

        estimado[i] = [xi, yi]
        tabla.add_fila(estimado[i])
    tabla.print_table()
    return (estimado)

dy=input("Ingrese y'")
dy=convertir_funcion(dy)
d1y = lambda x, y:  eval(dy)

#dy=input("Ingrese la y´")
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
puntosRK2 = eulermod(d1y, x0, y0, h, muestras)
xi = puntosRK2[:, 0]
yiRK2 = puntosRK2[:, 1]

# SALIDA
#print('estimado[xi,yi]')
#print(puntosRK2)