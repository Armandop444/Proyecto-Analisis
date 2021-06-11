#from Utilidades import limpiar, tablita
from sympy import *
import numpy as np
from FormulaEngine import convertir_funcion, reconvertir_funcion
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, Symbol,factorial, diff, parse_expr, Abs
from DiferenciacionNumerica import *


x = symbols('x')
#para primer nivel preguntar por la diferencia finita entre atras ,centrada y hacia adelante
#atras y adelante primera o segunda diferencia, centrada segunda y cuarta diferenciacion y elegir 3 o 5 puntos
#
func ="-(0.10*x**4)-(0.15*x**3)-(0.5*x**2)-(0.25*x)+1.2"
#print(diffforwardfunc(func,0.5,0.1,2))#Hacia adelante 1 y 2 diferencia


#richarson necesita la funcion, el metodo*,diferencia*,nivel*, punto a evaluar, h

def llenarH(h,Matriz,nivel):
    hn=h
    for i in range(nivel):
        Matriz[i,0]=float(hn)
        hn=(Matriz[i,0])/2
    #print(Matriz)
    return Matriz

def nivel2(D1,D2):
    respuesta=((4/3)*D2)-((1/3)*D1)
    return respuesta

def nivel3(D1,D2):
    respuesta=((16/15)*D2)-((1/15)*D1)
    return respuesta

def nivel4(D1,D2):
    respuesta=((64/63)*D2)-((1/63)*D1)
    return respuesta

def CalcularError(func,x,Matriz,nivel):
    #(f(x)-f(xn))/f(x)
    error=float(((eval(convertir_funcion(str(func),var_n="x")))-(Matriz[nivel-1,nivel]))/(eval(convertir_funcion(str(func),var_n="x"))))
    return error

def Richardson():
    func=input("Ingrese la funcion a evaluar\n")
    x=float(input("Ingrese el punto a evaluar en la funcion\n"))
    h=input("Ingrese el valor de h\n")
    nivel=int(input("Ingrese el nivel de la diferenciacion (Entre 2 y 4)\n"))
    #↓↓↓↓↓creando matriz↓↓↓↓↓
    Matriz = np.zeros((nivel, nivel+1))
    Matriz=llenarH(h,Matriz,nivel)
    print("Eliga el metodo de Diferencias Divididas: \n1.Hacia Adelante\n2.Hacia Atras\n3.Centrado")
    metodo=Integer(input(""))
    #print(metodo)
    if metodo==1:
        print("Eliga el orden de la diferencia hacia adelante: \n1.Primer orden \n2.Segundo orden")
        orden=Integer(input(""))
        #Primer nivel
        for i in range(nivel):
            print((str(Matriz[i,0])))
            PrimerNumero=Matriz[i,0]
            Matriz[i,1]=str(diffforwardfunc(func,x,PrimerNumero,orden))
        #segundo nivel
        for i in range (1,nivel,1):
            Matriz[i,2]=nivel2(Matriz[i-1,1],Matriz[i,1])
        #tercer nivel
        for i in range(2,nivel,1):
            Matriz[i,3]=nivel3(Matriz[i-1,2],Matriz[i,2])
        #cuarto nivel
        for i in range(3,nivel,1):
            Matriz[i,4]=nivel3(Matriz[i-1,3],Matriz[i,3])
        print("La matriz Resultante es:\n")
        print(Matriz)
        print("El error calculado es:")
        print(CalcularError(func,x,Matriz,nivel))
        
    elif metodo==2:#------------------------------------------------------------------------------------
        print("Eliga el orden de la diferencia hacia atras: \n1.Primer orden \n2.Segundo orden")
        orden=Integer(input(""))
        for i in range(nivel):
            print((str(Matriz[i,0])))
            PrimerNumero=Matriz[i,0]
            Matriz[i,1]=str(diffbackwardfunc(func,x,PrimerNumero,orden))
        #segundo nivel
        for i in range (1,nivel,1):
            Matriz[i,2]=nivel2(Matriz[i-1,1],Matriz[i,1])
        #tercer nivel
        for i in range(2,nivel,1):
            Matriz[i,3]=nivel3(Matriz[i-1,2],Matriz[i,2])
        #cuarto nivel
        for i in range(3,nivel,1):
            Matriz[i,4]=nivel3(Matriz[i-1,3],Matriz[i,3])
        print(Matriz)
        print("El error calculado es:")
        print(CalcularError(func,x,Matriz,nivel))
        
    elif metodo==3:#------------------------------------------------------------------------------------
        print("Eliga el orden de la diferencia centrada: \n1.Segundo orden\n2.cuarto orden\n3.De 3 puntos\n4.De 5 puntos")
        orden=Integer(input(""))
        for i in range(nivel):
            print((str(Matriz[i,0])))
            PrimerNumero=Matriz[i,0]
            Matriz[i,1]=str(diffcentralfunc(func,x,PrimerNumero,orden))
        #segundo nivel
        for i in range (1,nivel,1):
            Matriz[i,2]=nivel2(Matriz[i-1,1],Matriz[i,1])
        #tercer nivel
        for i in range(2,nivel,1):
            Matriz[i,3]=nivel3(Matriz[i-1,2],Matriz[i,2])
        #cuarto nivel
        for i in range(3,nivel,1):
            Matriz[i,4]=nivel3(Matriz[i-1,3],Matriz[i,3])
        print(Matriz)
        print("El error calculado es:")
        print(CalcularError(func,x,Matriz,nivel))
        
    else:#------------------------------------------------------------------------------------
        print("Error en la eleccion del metodo")

Richardson()



