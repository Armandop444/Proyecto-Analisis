from FormulaEngine import convertir_funcion, raiz
from Utilidades import tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan

def Sec(func, xnmenos, xn, es):
    tabla = tablita(["Xn-1","Xn","Xn+1","EA"])
    itera=1
    xnmas = 0
    ea=100.00
    
    funcion1=eval(convertir_funcion(func,var_n="xnmenos"))
    funcion2=eval(convertir_funcion(func,var_n="xn"))
    funcion=float(funcion1*funcion2)
    
    if(funcion<0.00):
        while ea>es:
            #xanterior=xnmenos
            funcion1=eval(convertir_funcion(func,var_n="xnmenos"))
            funcion2=eval(convertir_funcion(func,var_n="xn"))
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
        return tabla.get_tabla()
        
    else:
        print("No existe raiz")