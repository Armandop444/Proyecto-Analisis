from sympy import *
import pandas as pd
import numpy as np


#ecuacion=input("ingrese la funcion\n")
# funcion que se evaluara
#x = symbols('x') # declaramos que x es un simbolo

ecuacion=input("ingrese la funcion\n")
#funcion que se evaluara
x = symbols('x') # declaramos que x es un simbolo

#esto es del ccodigo de alejandro
if"^"in ecuacion:
    ecuacion=ecuacion.replace("^","**")
#aqui termina el codigo del ale

func = parse_expr(ecuacion)# funcion que evaluaremos


def Sec(func, xnmenos, xn, es):
    
    itera=0
    v_itera = np.array([])  # vector q almacena valores de itera
    v_xnmenos=np.array([])     # vector q almacena valores de xn-1
    v_xn=np.array([])     # vector q almacena valores de xn
    xnmas = 0
    v_xnmas=np.array([])     # vector q almacena valores de xn+1
    ea=100.00
    v_ea=np.array([])     # vector q almacena valores de ea
    #f1 = func.subs(x,xnmenos)  # reamplazmos x por x1xnmenos y evaluamos la funcion
    # incio del bucle
    funcion1=func.subs(x,xnmenos)
    funcion2=func.subs(x,xn)
    funcion=float(funcion1*funcion2)
    if(funcion<0.00):
        print(f"Raiz existente: {funcion}")
        while ea>es:
            #xanterior=xnmenos
            funcion1=func.subs(x,xnmenos)
            funcion2=func.subs(x,xn)
            xnmas=float(xn-(funcion2*((xn-xnmenos)/(funcion2-funcion1))))
            #print(xnmas)
            itera=itera+1
            if xnmas !=0 and itera!=0:
                ea = float(abs((xnmas - xn) / xnmas) * 100)
            # agregamos valores a los vectores vacios
            v_itera = np.append(v_itera, itera)
            v_xnmenos = np.append(v_xnmenos, xnmenos)
            v_xn = np.append(v_xn, xn)
            v_xnmas = np.append(v_xnmas, xnmas)
            v_ea = np.append(v_ea, ea)
            #si se cumple lo anterior se da el cambio de valores
            xnmenos=float(xn)
            xn=float(xnmas)
        print(f"El valor de la raiz es: {xnmas}")
        print(f"Con un error de : {ea}")
        #representamos datos en panda
        iteracion = pd.Series(v_itera, name="Iteracion")
        xnmenos = pd.Series(v_xnmenos, name="xn-1")
        xn = pd.Series(v_xn, name="xn")
        xnmas = pd.Series(v_xnmas, name="xn+1")
        ea = pd.Series(v_ea, name="ea%")
        tabla = pd.concat([iteracion, xnmenos, xn, xnmas, ea], axis=1)  # unimos en columnas
        return tabla  
        
    else:
        print("No existe raiz")

a=Sec(func,0,1, 0.00001)
print(a)