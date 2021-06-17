from FormulaEngine import convertir_funcion,raiz
from Utilidades import tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, diff, symbols, parse_expr

def NewtonRaphson(funcion:str, xo: float, es: float):
    x = symbols('xo')
    tabla = tablita(['Xn','f(Xn)',"f'(Xn)", "Xn+1","EA"])
    ea = 100
    
    funcion = convertir_funcion(funcion,var_n='xo')
    #Calcular derivadas
    fx=float(eval(funcion))
    df = diff(funcion,x)#Haciendo la primer derivada
    df2= diff(df,x)#haciendo la segunda derivada
    convergencia=abs((fx*float(eval(str(df2))))/(float(eval(str(df))))**2)#Encontrando el valor de la convergencia
    if(convergencia<1):#convergencia
        while ea > es:
            fx = float(eval(funcion))
            dfx = float(eval(str(df)))
            
            xn = xo - (fx/dfx)
            ea = abs((xn-xo)/xn) * 100
            tabla.add_fila([xo,fx,dfx,xn,ea])
            xo = xn
        return tabla.get_tabla()
    else:
        return "No existe raiz"