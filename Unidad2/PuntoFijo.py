from FormulaEngine import convertir_funcion
from Utilidades import raiz, tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan

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
