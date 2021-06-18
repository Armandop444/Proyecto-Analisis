import numpy as np
from sympy import symbols, parse_expr, Subs,cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
from FormulaEngine import convertir_funcion,castear,comprobarpunto
from Utilidades import limpiar

def trapeciotabla():
    cantPoints = int(input("Ingrese cantidad de puntos conocidos > "))
    if cantPoints < 2:
        print("\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n")
        trapeciotabla()
    points = [[], []]
    integs = []
    for i in range(cantPoints):
        print("\n( x", i, ",y", i, ")")
        x = float(eval(castear("Ingrese 'x'> ")))
        y = float(eval(castear("Ingrese 'y'> ")))
        points[0].append(x)
        points[1].append(y)
    for i in range(cantPoints - 1):
        integ = ((points[0][i + 1] - points[0][i]) / 2) * (points[1][i] + points[1][i + 1])
        integs.append(integ)
    print("\nIntegral: ", sum(integs))
def trapecio():
    option=int(input("Como desea usar el metodo del trapecio \n1.Ingresando tabla \n2.Ingresando funcion(trapecio compuesto) \n3.Ingresando funcion(trapecio simple)\n"))
    limpiar()
    if(option==1):
        trapeciotabla()
    if(option==2):
        ecuacion = input("Ingrese la funcion\n")

        x = symbols('x')  # declaramos que x es un simbolo

        ecuacion=convertir_funcion(ecuacion)

        fx = parse_expr(ecuacion)  # funcion que evaluaremos

        # intervalo de integración
        aa = input("Ingrese el intervalo inferior\n")
        a=comprobarpunto(aa)
        bb = input("Ingrese el intervalo superior\n")
        b=comprobarpunto(bb)
        tramos = int(input("Ingrese el numero de tramos\n"))


        h = (b - a) / tramos
        xi = a
        suma = fx.subs(x, xi)
        for i in range(0, tramos - 1, 1):
            xi = xi + h
            suma = suma + 2 * fx.subs(x, xi)
        suma = suma + fx.subs(x, b)
        area = h * (suma / 2)

        # SALIDA
        print('tramos: ', tramos)
        print('Integral: ', area)
    if(option==3):
        ecuacion = input("Ingrese la funcion\n")

        x = symbols('x')  # declaramos que x es un simbolo

        ecuacion=convertir_funcion(ecuacion)

        fx = parse_expr(ecuacion)  # funcion que evaluaremos
        # intervalo de integración
        aa = input("Ingrese el intervalo inferior\n")
        a=comprobarpunto(aa)
        bb = input("Ingrese el intervalo superior\n")
        b=comprobarpunto(bb)
        trapecio=(b-a)*((fx.subs(x,a)+fx.subs(x,b)/2))
        print("la proximacion es :",trapecio)
