import numpy as np
from sympy import symbols, parse_expr, Subs
from FormulaEngine import convertir_funcion

def integraCuadGaussp(fx,a,b,tramos,t,w):
    x = symbols('x')
    muestras=tramos+1

    area=0
    for i in range(0, muestras - 1, 1):
        x0=((b+a)*(t[i])+(b-a))/2
        print(w[i]*(fx.subs(x, x0)))
        print(w[i]," *", (fx.subs(x, x0)))
        area =area+(w[i]*(fx.subs(x, x0)))

    return(((b-a)/2)*area)

def gauss():
    # INGRESO
    ecuacion = input("ingrese la funcion\n")

    x = symbols('x')

    ecuacion=convertir_funcion(ecuacion)

    fx = parse_expr(ecuacion)

    a = float(input("ingrese el punto a de la integral\n"))
    b = float(input("ingrese el punto b de la integral\n"))
    tramos = int(input("cuantos puntos desea evaluar\n"))

    [t, w] = np.polynomial.legendre.leggauss(tramos)
    print('w\n', w)
    print('x\n', t)
    muestras = tramos+1

    area = 0
    area= integraCuadGaussp(fx,a,b,tramos,t,w)

    print('Integral: ', area)