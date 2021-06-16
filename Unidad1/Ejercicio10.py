# Ejercicio9 Unidad1
# 1/1+x^2
#-1<x<1
from Utilidades import tablita
from sympy import Pow, factorial
def ejercicio10(x,Es):
    Ea = 100000
    xn0 = 0.0
    xn1 = 0.0
    i=0
    tabla=tablita(["xn1","Ea"])
    while Ea>=Es:
        if x!=0:
            xn1 = xn0 + ((Pow(-1,i))*((Pow(x,2*i))))
            Ea = float(abs(((xn1 - xn0) /( xn1))) * 100)
            xn0=xn1
            tabla.add_fila([xn1,Ea])
        else:
            
            tabla.add_fila([0,0])
            break
        i+=1
    return tabla.get_tabla()
