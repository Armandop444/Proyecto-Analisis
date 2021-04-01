from sympy import *
import numpy as np
from tabulate import tabulate

#ecuacion=input("ingrese la funcion\n")
# funcion que se evaluara
x = symbols('x') # declaramos que x es un simbolo

#esto es del ccodigo de alejandro
#if"^"in ecuacion:
#    ecuacion=ecuacion.replace("^","**")
#aqui termina el codigo del ale

#func = parse_expr(ecuacion)# funcion que evaluaremos


# metodo de la biseccion
def FalsaP(func, x1, x2, es):
    itera = 1
    contenido = []
    
    xr = 0
    ea = 100

    # incio del bucle
    while ea > es:
        
        f1 = func.subs(x, x1)  # reamplazmos x por x1 y evaluamos la funcion
        f2 = func.subs(x, x2)
        
        xanterior = xr
        
        xr = (x1-((f1*(x1-x2))/(f1-f2)))
        fr = func.subs(x, xr)
        if xr != 0:
            ea = abs((xr - xanterior) / xr) * 100
        test = f1 * fr
        
        # agregamos valores a la fila de la iteracion
        contenido.append([itera, x1,x2,xr,ea])
        itera += 1

        if test < 0:
            x2 = xr
        elif test > 0:
            x1 = xr
        else:
            ea = 0

    return tabulate(contenido, headers=["Iteracion","X1","X2","Xr","EA"],tablefmt="orgtbl")

#x1=float(input("ingrese el valor de x1\n"))
#x2=float(input("ingrese el valor de x2\n"))
#a = FalsaP(func, x1, x2, 0.00001)
#print(a)