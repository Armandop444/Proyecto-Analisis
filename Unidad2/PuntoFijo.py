from FormulaEngine import convertir_funcion, raiz
from Utilidades import tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, diff, symbols, parse_expr,sqrt



def PuntoFijo(funcion: str, es: float, x: float):
    xo=symbols("x")
    ea = 100
    funcion = convertir_funcion(funcion)
    tabla = tablita(["X","g(X)","EA"])
    derivada=diff(parse_expr(funcion),xo)#haciendo la primer derivada
    deveval=float(eval(str(derivada)))#evaluando en el punto x de la primer derivada
    if(deveval<1):#convergencia
        while ea > es:
            xn = eval(funcion)
            ea = abs((xn-x)/xn) * 100
            tabla.add_fila([x,xn,ea])
            x = xn
        return tabla.get_tabla()
    else:
        return "No existe raiz"
