from FormulaEngine import convertir_funcion
from math import cos, sin, tan, asin, log, exp
from tabulate import tabulate
from Utilidades import raiz, tablita

def PuntoFijo(funcion: str, es: float, x: float):
    ea = 100
    funcion = convertir_funcion(funcion)
    tabla = tablita(["X","g(X)","EA"])
    while ea > es:
        xn = eval(funcion)
        ea = abs((xn-x)/xn) * 100
        tabla.add_fila([x,xn,ea])
        x = xn
    return tabla.get_tabla()
