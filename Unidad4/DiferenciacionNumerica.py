from sympy import *
#hacia delante
x=Symbol("x")
def diffforwardfunc(funcion, xo, h, nivelderivada):
    funcion=parse_expr(funcion)
    funcdiff=parse_expr("1")
    respuesta=0
    if nivelderivada==1:
        funcdiff=((funcion.subs(x,(xo+h)))-(funcion.subs(x,(xo))))/(h)
        respuesta=funcdiff
    elif nivelderivada==2:
        funcdiff=(-(funcion.subs(x,(xo+2*h)))+4*(funcion.subs(x,(xo+h)))-3*(funcion.subs(x,xo)))/(2*h)
        respuesta=funcdiff
    else:
        print("error en la seleccion de nivel de derivada")
    return float(respuesta)

funcion="-(0.10*(x**4))-(0.15*(x**3))-(0.5*(x**2))-(0.25*x)+1.2"
xo=0.5
h=0.1
uwu=diffforwardfunc(funcion,xo,h,1)
print(uwu)

