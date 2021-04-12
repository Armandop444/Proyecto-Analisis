from sympy import *
import numpy as np
from Utilidades import tablita

#ecuacion=input("ingrese la funcion\n")
# funcion que se evaluara
x = symbols('x') # declaramos que x es un simbolo

#esto es del ccodigo de alejandro
#if"^"in ecuacion:
#    ecuacion=ecuacion.replace("^","**")
#aqui termina el codigo del ale

#func = parse_expr(ecuacion)# funcion que evaluaremos


# metodo de la biseccion
def Bisec(func, x1, x2, es):
    tabla = tablita(["X1", "X2", "Xr", "EA"])
    xr = 0
    ea = 100
    f1 = func.subs(x,x1)  # reamplazmos x por x1 y evaluamos la funcion
    # inicio del bucle
    while ea > es:

        xanterior = xr
        xr = (x1 + x2) / 2
        fr = func.subs(x,xr)
        if xr != 0:
            ea = abs((xr - xanterior) / xr) * 100
        test = f1 * fr
        
        # agregamos valores a la fila de cada iteracion
        tabla.add_fila([x1,x2,xr,ea]) 
        if test < 0:
            x2 = xr
        elif test > 0:
            x1 = xr
            f1 = fr
        else:
            ea = 0
    return tabla.get_tabla()

#x1=float(input("ingrese el valor de x1\n"))
#x2=float(input("ingrese el valor de x2\n"))
#a = Bisec(func, x1, x2, 0.01 )
#print(a)