#Ejercicio 4 coseno por series de taylor por metodos numericos
from Utilidades import tablita
from sympy import Pow, factorial
from math import radians
def ejercicio4(x,es):
    tabla=tablita(["Raiz","Ea"])
    #Cos__x = float(input ("ingrese el valor del argumento de coseno : "))
    X= radians(x)
    #ncf= float(input("ingrese el numero de cifras significativas : "))
    xn0=0.0
    #nivel_De_Tolerancia=0.5*0.5*(Pow(10,(2-ncf)))
    Ea=100
    i=0
    #print ("\n\n{:^4} {:^20} {:^20} ".format("iteracion ", "raiz","EA"))
    while Ea>=es:
        
        if x==0:
            #print(i+1,"\t",xn0,"\t -")
            tabla.add_fila([xn0,"-"])
            break
        else:
            xn1=xn0+float(((Pow(-1,i))*(Pow(X,(2*i))))/(factorial((2*i))))
            Ea=abs((xn1-xn0)/(xn1))*100
            xn0=xn1
            #print("%-20d %-20s %-20s" % (i+1,xn1,Ea))
            tabla.add_fila([xn1,Ea])
        i+=1
    return tabla.get_tabla()