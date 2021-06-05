#Ejercicio3
#Sen(x) Serie de Taylor
from Utilidades import raiz, tablita
from sympy import ln, exp, Pow, factorial
from math import radians
def ejercicio3(x,Es):
    tabla=tablita(["Xn1,Ea"])
    x= radians(x)
    Ea=10000
    xn0=0.0
    i=0
    while Ea>=Es:
        if x==0:
            #print(i+1,"\t",xn0,"\t -")
            tabla.add_fila([xn0,"-"])
            break
        else:
            xn1=xn0+float(((Pow(-1,i))*(Pow(x,(2*i)+1)))/(factorial((2*i)+1)))
            Ea=abs((xn1-xn0)/(xn1))*100
            xn0=xn1
            #print("%-20d %-20s %-20s" % (i+1,xn1,Ea))
            tabla.add_fila([xn1,Ea])
        i+=1
    
    return tabla.get_tabla()