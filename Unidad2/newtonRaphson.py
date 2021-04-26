from FormulaEngine import convertir_funcion
from Utilidades import raiz, tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, diff, symbols

def NewtonRaphson(funcion:str, xo: float, es: float):
    tabla = tablita(['Xn','f(Xn)',"f'(Xn)", "Xn+1","EA"])
    ea = 100
    
    funcion = convertir_funcion(funcion,var_n='xo')
    
    #Calcular derivadas
    x = symbols('xo')
    df = diff(funcion,x)
    
    while ea > es:
        fx = float(eval(funcion))
        dfx = float(eval(str(df)))
        
        xn = xo - (fx/dfx)
        ea = abs((xn-xo)/xn) * 100
        tabla.add_fila([xo,fx,dfx,xn,ea])
        xo = xn
    return tabla.get_tabla()