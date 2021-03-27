from sympy import *
import pandas as pd
import numpy as np

ecuacion=input("ingrese la funcion\n")
# funcion que se evaluara
x = symbols('x') # declaramos que x es un simbolo

#esto es del ccodigo de alejandro
if"^"in ecuacion:
    ecuacion=ecuacion.replace("^","**")
#aqui termina el codigo del ale

func = parse_expr(ecuacion)# funcion que evaluaremos


# metodo de la biseccion
def Bisec(func, x1, x2, es):
    itera = 0
    v_itera = np.array([])  # vector q almacena valores de itera
    v_x1 = np.array([])  # vector q alamacena valores de x1
    v_x2 = np.array([])  # vector q alamcena valores de x2
    xr = 0
    v_xr = np.array([])  # vector q almacena valroes de xr
    ea = 100
    v_ea = np.array([])  # vector q alamcena valore s de ea
    f1 = func.subs(x,x1)  # reamplazmos x por x1 y evaluamos la funcion
    # incio del bucle
    while ea > es:

        xanterior = xr
        xr = (x1 + x2) / 2
        fr = func.subs(x,xr)
        itera = itera + 1
        if xr != 0:
            ea = abs((xr - xanterior) / xr) * 100
        test = f1 * fr
        # agregamos valores a los vectores vacios
        v_itera = np.append(v_itera, itera)
        v_x1 = np.append(v_x1, x1)
        v_x2 = np.append(v_x2, x2)
        v_xr = np.append(v_xr, xr)
        v_ea = np.append(v_ea, ea)

        if test < 0:
            x2 = xr
        elif test > 0:
            x1 = xr
            f1 = fr
        else:
            ea = 0
    # representamos datos en pandas
    iteracion = pd.Series(v_itera, name="Iteracion")
    x1 = pd.Series(v_x1, name="x1")
    x2 = pd.Series(v_x2, name="x2")
    xr = pd.Series(v_xr, name="xr")
    ea = pd.Series(v_ea, name="ea%")
    tabla = pd.concat([iteracion, x1, x2, xr, ea], axis=1)  # unimos en columnas
    return tabla

x1=float(input("ingrese el valor de x1\n"))
x2=float(input("ingrese el valor de x2\n"))
a = Bisec(func, x1, x2, 0.01 )
print(a)

