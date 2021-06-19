import numpy as np
from sympy import symbols, parse_expr, Subs
from FormulaEngine import convertir_funcion,comprobarpunto

def integraCuadGaussp(fx,a,b,tramos,t,w):
    x = symbols('x')
    muestras=tramos+1

    area=0
    for i in range(0, muestras - 1, 1):
        x0=((b+a)*(t[i])+(b-a))/2
        #print(w[i]*(fx.subs(x, x0)))
        #print(w[i]," *", (fx.subs(x, x0)))
        area =area+(w[i]*(fx.subs(x, x0)))

    return(((b-a)/2)*area)

def gauss():
    # INGRESO
    ecuacion = input("Ingrese la funcion\n")

    x = symbols('x')

    ecuacion=convertir_funcion(ecuacion)

    fx = parse_expr(ecuacion)

    i = 1
    while i == 1:
        aa = input("Ingrese el intervalo inferior\n")
        a = comprobarpunto(aa)
        bb = input("Ingrese el intervalo superior\n")
        b = comprobarpunto(bb)
        if a > b:
            a = 0
            print("el intervalo inferior no puede ser mayor que el superior")
        else:
            a = 1
            break

    tramos = int(input("Cuantos puntos desea evaluar\n"))

    [t, w] = np.polynomial.legendre.leggauss(tramos)
    #print('w\n', w)
    #print('x\n', t)
    muestras = tramos+1

    area = 0
    area= integraCuadGaussp(fx,a,b,tramos,t,w)

    print('Integral: ', float(eval(str(area))))