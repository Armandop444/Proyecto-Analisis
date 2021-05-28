#Ejercicio4
#e^x Serie de Taylor

def ejercicio5():
    import math
    x=float(input("Introduzca el valor del argumento: "))
    n=int(input("Introduzca el numero de cifras significativas: "))
    Es=0.5*(math.pow(10,(2-n)))
    Ea=10000
    xn0=0
    i=0
    print("%-20s %-20s %-20s" %("iteracion","Xn1","Ea"))
    while Ea>=Es:
        xn1=xn0+(math.pow(x,i))/math.factorial(i)
        Ea=abs((xn1-xn0)/(xn1))*100
        if Ea==0:
            break
        xn0=xn1
        print("%-20d %-20s %-20s" % (i+1,xn1,Ea))
        i+=1

ejercicio5()