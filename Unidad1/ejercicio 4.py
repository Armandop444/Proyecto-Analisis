#Ejercicio 4 coseno por series de taylor por metodos numericos
import math
import numpy as np 

Cos__x = float(input ("ingrese el valor   del argumento de coseno : "))
X= math.radians(Cos__x)
ncf= float(input("ingrese el numero de cifras significativas : "))
xn0=0.0
nivel_De_Tolerancia=0.5*0.5*(math.pow(10,(2-ncf)))
Ea=100
i=0
print ("\n\n{:^4} {:^20} {:^20} ".format("iteracion ", "raiz","EA"))
while Ea>=nivel_De_Tolerancia:
  
    if Cos__x==0:
        print(i+1,"\t",xn0,"\t -")
        break
    else:
        xn1=xn0+float(((np.power(-1,i))*(np.power(X,(2*i))))/(math.factorial((2*i))))
        Ea=abs((xn1-xn0)/(xn1))*100
        xn0=xn1
        print("%-20d %-20s %-20s" % (i+1,xn1,Ea))
        #print(i+1,"\t",xn1,"\t",Ea)
    i+=1
