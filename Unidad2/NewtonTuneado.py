from FormulaEngine import convertir_funcion, raiz
from Utilidades import tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, diff, symbols,sqrt

def NewtonTuneado(funcion: str, xo: float, es: float):
    tabla = tablita(["Xn","f(Xn)", "f'(Xn)","f''(Xn)", "Xn+1","EA"])
    
    funcion = convertir_funcion(funcion,var_n='xo')
    
    #Calcular derivadas
    x = symbols('xo')
    fx = float(eval(funcion))
    df = diff(funcion,x)
    ddf = diff(df,x)
    ea = 100
    convergencia=abs((fx*float(eval(str(ddf))))/(float(eval(str(df))))**2)#Encontrando el valor de la convergencia
    if(convergencia<1):
        while ea > es:
            fx = float(eval(funcion))
            dfx = float(eval(str(df)))
            ddfx = float(eval(str(ddf)))
            xn = xo - ((fx*dfx) /((dfx**2)-fx*ddfx))
            ea = abs((xn-xo)/xn) * 100
            tabla.add_fila([xo,fx,dfx,ddfx,xn,ea])
            xo=xn
            
        return tabla.get_tabla()
    else:
        return "No existe raiz"
