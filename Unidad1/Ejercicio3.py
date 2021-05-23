#Ejercicio3
#Sen(x) Serie de Taylor

def ejercicio3():
    import math
    import numpy as np
    x=float(input("Introduzca el valor del argumento en grados: "))
    x= math.radians(x)
    n=int(input("Introduzca el numero de cifras significativas: "))
    Es=0.5*(math.pow(10,(2-n)))
    Ea=10000
    xn0=0.0
    i=0
    print("%-20s %-20s %-20s" %("iteracion","Xn1","Ea"))
    while Ea>=Es:
        if x==0:
            print(i+1,"\t",xn0,"\t -")
            break
        else:
            xn1=xn0+float(((np.power(-1,i))*(np.power(x,(2*i)+1)))/(math.factorial((2*i)+1)))
            Ea=abs((xn1-xn0)/(xn1))*100
            xn0=xn1
            print("%-20d %-20s %-20s" % (i+1,xn1,Ea))
        i+=1
