from sympy import *
import numpy as np
from tabulate import tabulate
from Utilidades import tablita


#ecuacion=input("ingrese la funcion\n")
# funcion que se evaluara
#x = symbols('x') # declaramos que x es un simbolo

#ecuacion=input("ingrese la funcion\n")
#funcion que se evaluara
x = symbols('x') # declaramos que x es un simbolo

#esto es del ccodigo de alejandro
#if"^"in ecuacion:
#    ecuacion=ecuacion.replace("^","**")
#aqui termina el codigo del ale

#func = parse_expr(ecuacion)# funcion que evaluaremos


def Sec(func, xnmenos, xn, es):
    tabla = tablita(["Xn-1","Xn","Xn+1","EA"])
    itera=1
    xnmas = 0
    ea=100.00

    #f1 = func.subs(x,xnmenos)  # reamplazmos x por x1xnmenos y evaluamos la funcion
    # incio del bucle
    
    funcion1=func.subs(x,xnmenos)
    funcion2=func.subs(x,xn)
    funcion=float(funcion1*funcion2)
    
    if(funcion<0.00):
        while ea>es:
            #xanterior=xnmenos
            funcion1=func.subs(x,xnmenos)
            funcion2=func.subs(x,xn)
            xnmas=float(xn-(funcion2*((xn-xnmenos)/(funcion2-funcion1))))
            #print(xnmas)
            if xnmas !=0 and itera!=0:
                ea = float(abs((xnmas - xn) / xnmas) * 100)
                
            # agregamos valores a la fila de la iteracion
            tabla.add_fila([xnmenos,xn,xnmas,ea])
            itera +=1
            
            #si se cumple lo anterior se da el cambio de valores
            xnmenos=float(xn)
            xn=float(xnmas)
            
        #print(f"\nEl valor de la raiz es: {xnmas}")
        #print(f"Con un error de : {ea}\n")

        return tabla.get_tabla()
        
    else:
        print("No existe raiz")

#a=Sec(func,0,1, 0.00001)
#print(a)