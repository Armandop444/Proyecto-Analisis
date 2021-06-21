import numpy as np
from sympy import *
from FormulaEngine import convertir_funcion,castear,comprobarpunto
from Utilidades import limpiar

x = symbols('x')  # declaramos que x es un simbolo

def prod(A):
    a = 1
    for i in range(len(A)):
        a = a * A[i]
    return a


def lagrange(A, n):
    results = []
    lfun = np.arange((len(A[0]))**2,dtype=float)
    lfun.shape = (len(A[0]),len(A[0]))
    for i in range(len(A[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:   lfun[i,j] = (n-A[0][j])/(A[0][i]-A[0][j])
    for i in range(len(A[1])):
        results.append(prod(lfun[i])*A[1][i])
    return sum(results)
def simpsonTabla():
    cantPoints = int(input("Ingrese cantidad de puntos conocidos> "))
    if cantPoints < 2:
        print ("\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n")
        simpsonTabla()
    integs = []
    points = [[],[]]
    midPoints = [[],[]]
    for i in range(cantPoints):
        print ("\n( x",i,",y",i,")")
        x = float(eval(castear("Ingrese 'x'> ")))
        y = float(eval(castear("Ingrese 'y'> ")))
        points[0].append(x)
        points[1].append(y)
    for i in range(len(points[0])-1):
        midPoints[0].append((points[0][i+1]+points[0][i])/2)
        midPoints[1].append(lagrange(points,midPoints[0][i]))
    for i in range(len(midPoints[0])):
        intg = ((points[0][i+1]-points[0][i])/6)*\
            (points[1][i]+(4*midPoints[1][i])+points[1][i+1])
        integs.append(intg)
    print ("\n\tIntegral: ",sum(integs))

def simpson(f, A, B):
    h = (B-A)/6
    return h * (f.subs(x,A) + 4*f.subs(x,(A+B)/2) + f.subs(x,B))
def simpson13(f, a, b):
    m=(a+b)/2
    intg=(b-a)/6*(f.subs(x,a)+4*f.subs(x,m)+f.subs(x,b))
    return intg

    return f

def simp():
    option=int(input("Como desea usar el metodo del simpson 1/3 \n1.Ingresando tabla \n2.Ingresando funcion( compuesto) \n3.Ingresando funcion( simple) \n"))
    limpiar()
    if(option==1):

        simpsonTabla()


    if(option==2):
        ecuacion = input("Ingrese la funcion\n")

        ecuacion=convertir_funcion(ecuacion)

        fx = parse_expr(ecuacion)  # funcion que evaluaremos

        # intervalo de integración
        aa = input("Ingrese el intervalo inferior\n")
        a=comprobarpunto(aa)
        bb = input("Ingrese el intervalo superior\n")
        b=comprobarpunto(bb)
        i = 1
        while i == 1:
            aa = input("Ingrese el intervalo inferior\n")
            a = comprobarpunto(aa)
            bb = input("Ingrese el intervalo superior\n")
            b = comprobarpunto(bb)
            if a > b:
                a=0
                print("el intervalo inferior no puede ser mayor que el superior")
            else:
                a=1
                break

        n = int(input("Ingrese el numero de tramos\n"))
        h = (b - a) / n
        suma = 0
        for i in range(n):
            b = a + h
            area = simpson13(fx, a, b)

            suma = suma + area
            a = b

        print("Integral : ",float(eval(str(suma))),"\n")


    if(option==3):
        ecuacion = input("Ingrese la funcion\n")

        x = symbols('x')  # declaramos que x es un simbolo

        ecuacion=convertir_funcion(ecuacion)

        fx = parse_expr(ecuacion)  # funcion que evaluaremos


        i = 1
        while i == 1:
            aa = input("Ingrese el intervalo inferior\n")
            a = comprobarpunto(aa)
            bb = input("Ingrese el intervalo superior\n")
            b = comprobarpunto(bb)
            if a > b:
                a=0
                print("el intervalo inferior no puede ser mayor que el superior")
            else:
                a=1
                break

        print("Integral : ",float(eval(str(simpson(fx,a,b)))))