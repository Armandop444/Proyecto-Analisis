from sympy import *
import numpy as np
from sympy.solvers.diophantine.diophantine import length
from FormulaEngine import convertir_funcion, reconvertir_funcion
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, Symbol,factorial, diff, parse_expr, Abs,sqrt
from Unidad4.DiferenciacionNumerica import *
from Utilidades import tablita, limpiar


x = symbols('x')
#para primer nivel preguntar por la diferencia finita entre atras ,centrada y hacia adelante
#atras y adelante primera o segunda diferencia, centrada segunda y cuarta diferenciacion y elegir 3 o 5 puntos
#
#func ="-(0.10*x**4)-(0.15*x**3)-(0.5*x**2)-(0.25*x)+1.2"
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

def nivel5(D1,D2):
    respuesta=((256/255)*D2)-((1/255)*D1)
    return respuesta

def nivel6(D1,D2):
    respuesta=((1024/1023)*D2)-((1/1023)*D1)
    return respuesta

def nivel7(D1,D2):
    respuesta=((4096/4095)*D2)-((1/4095)*D1)
    return respuesta

def imprimir(Matriz,nivel):
    cabeceros=[]
    cabeceros.append("H")
    for i in range(nivel):
        mensaje="Nivel "+str(i+1)
        cabeceros.append(mensaje)
    print("La matriz Resultante es:\n")
    tabla=tablita(cabeceros,show_iteracion=False)
    for xn in range(nivel):
        columna=[]
        for fx in range((nivel+1)):
            columna.append(Matriz[xn,fx])
        tabla.add_fila(columna)
    tabla.print_table()

def CalcularError(func,x,Matriz,nivel):
    #(f(x)-f(xn))/f(x)
    d=diff(func)
    error=float(((eval(convertir_funcion(str(d),var_n="x")))-(Matriz[nivel-1,nivel]))/(eval(convertir_funcion(str(d),var_n="x"))))*100
    #print(Matriz[nivel-1,nivel])
    #print(eval(convertir_funcion(str(d),var_n="x")))
    return error

def Richardson():
    texto=False
    func=input("Ingrese la funcion a evaluar\n")
    func=convertir_funcion(func)
    x=float(input("Ingrese el punto a evaluar en la funcion\n"))
    h=input("Ingrese el valor de h\n")
    nivel=int(input("Ingrese el nivel de la diferenciacion (Entre 2 y 7)\n"))
    limpiar()
    #↓↓↓↓↓creando matriz↓↓↓↓↓
    Matriz = np.zeros((nivel, nivel+1))
    #Matriz=[]
    Matriz=llenarH(h,Matriz,nivel)
    print("Eliga el metodo de Diferencias Divididas: \n1.Hacia Adelante\n2.Hacia Atras\n3.Centrado")
    metodo=Integer(input(""))
    limpiar()
    #print(metodo)
    if metodo==1:
        print("Eliga el orden de la diferencia hacia adelante: \n1.Primer orden \n2.Segundo orden")
        orden=Integer(input(""))
        limpiar()
        #Primer nivel
        for i in range(nivel):
            #print((str(Matriz[i,0])))
            PrimerNumero=Matriz[i,0]
            Matriz[i,1]=str(diffforwardfunc(func,x,PrimerNumero,orden,texto))
        #segundo nivel
        for i in range (1,nivel,1):
            Matriz[i,2]=nivel2(Matriz[i-1,1],Matriz[i,1])
        #tercer nivel
        for i in range(2,nivel,1):
            Matriz[i,3]=nivel3(Matriz[i-1,2],Matriz[i,2])
        #cuarto nivel
        for i in range(3,nivel,1):
            Matriz[i,4]=nivel3(Matriz[i-1,3],Matriz[i,3])
        #quinto nivel
        for i in range(4,nivel,1):
            Matriz[i,5]=nivel5(Matriz[i-1,4],Matriz[i,4])
        #sexto nivel
        for i in range(5,nivel,1):
            Matriz[i,6]=nivel6(Matriz[i-1,5],Matriz[i,5])
        #septimo nivel
        for i in range(6,nivel,1):
            Matriz[i,7]=nivel7(Matriz[i-1,6],Matriz[i,6])
        imprimir(Matriz,nivel)
        print("El error calculado es:")
        print(f"{CalcularError(func,x,Matriz,nivel)}%")
        
    elif metodo==2:#------------------------------------------------------------------------------------
        print("Eliga el orden de la diferencia hacia atras: \n1.Primer orden \n2.Segundo orden")
        orden=Integer(input(""))
        limpiar()
        for i in range(nivel):
            #print((str(Matriz[i,0])))
            PrimerNumero=Matriz[i,0]
            Matriz[i,1]=str(diffbackwardfunc(func,x,PrimerNumero,orden,texto))
        #segundo nivel
        for i in range (1,nivel,1):
            Matriz[i,2]=nivel2(Matriz[i-1,1],Matriz[i,1])
        #tercer nivel
        for i in range(2,nivel,1):
            Matriz[i,3]=nivel3(Matriz[i-1,2],Matriz[i,2])
        #cuarto nivel
        for i in range(3,nivel,1):
            Matriz[i,4]=nivel3(Matriz[i-1,3],Matriz[i,3])
        #quinto nivel
        for i in range(4,nivel,1):
            Matriz[i,5]=nivel5(Matriz[i-1,4],Matriz[i,4])
        #sexto nivel
        for i in range(5,nivel,1):
            Matriz[i,6]=nivel6(Matriz[i-1,5],Matriz[i,5])
        #septimo nivel
        for i in range(6,nivel,1):
            Matriz[i,7]=nivel7(Matriz[i-1,6],Matriz[i,6])
        imprimir(Matriz,nivel)
        print("El error calculado es:")
        print(f"{CalcularError(func,x,Matriz,nivel)}%")
        
    elif metodo==3:#------------------------------------------------------------------------------------
        print("Eliga el orden de la diferencia centrada: \n1.Segundo orden\n2.cuarto orden\n3.De 3 puntos\n4.De 5 puntos")
        orden=Integer(input(""))
        limpiar()
        for i in range(nivel):
            #print((str(Matriz[i,0])))
            PrimerNumero=Matriz[i,0]
            Matriz[i,1]=str(diffcentralfunc(func,x,PrimerNumero,orden,texto))
        #segundo nivel
        for i in range (1,nivel,1):
            Matriz[i,2]=nivel2(Matriz[i-1,1],Matriz[i,1])
        #tercer nivel
        for i in range(2,nivel,1):
            Matriz[i,3]=nivel3(Matriz[i-1,2],Matriz[i,2])
        #cuarto nivel
        for i in range(3,nivel,1):
            Matriz[i,4]=nivel3(Matriz[i-1,3],Matriz[i,3])
        #quinto nivel
        for i in range(4,nivel,1):
            Matriz[i,5]=nivel5(Matriz[i-1,4],Matriz[i,4])
        #sexto nivel
        for i in range(5,nivel,1):
            Matriz[i,6]=nivel6(Matriz[i-1,5],Matriz[i,5])
        #septimo nivel
        for i in range(6,nivel,1):
            Matriz[i,7]=nivel7(Matriz[i-1,6],Matriz[i,6])
        imprimir(Matriz,nivel)
        print("El error calculado es:")
        print(f"{CalcularError(func,x,Matriz,nivel)}%")
        
    else:#------------------------------------------------------------------------------------
        print("Error en la eleccion del metodo")
