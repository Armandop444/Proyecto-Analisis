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

def diffbackwardfunc(funcion,xo,h,nivelderivada):
    respuesta=0
    error=0.0
    funcion=parse_expr(funcion)
    funcdiff=parse_expr("1")
    if nivelderivada==1:
        funcdiff=(-(funcion.subs(x,(xo-h)))+(funcion.subs(x,(xo))))/(h)
        respuesta=funcdiff
    elif nivelderivada==2:
        funcdiff=((funcion.subs(x,(xo-2*h)))-4*(funcion.subs(x,(xo-h)))+3*(funcion.subs(x,xo)))/(2*h)
        respuesta=funcdiff
    else:
        print("error en la seleccion de nivel de derivada")
    return float(respuesta)


#opcionmetodo
#1=centradasegundoorden
#2=centradacuartoorden
#3=3puntos
#4=5puntos
def diffcentralfunc(funcion,xo,h,opcionmetodo):
    #codigo
    respuesta=0
    return float(respuesta)




funcion="log(x)"
xo=5
h=0.05
uwu=diffbackwardfunc(funcion,xo,h,2)
print(uwu)

