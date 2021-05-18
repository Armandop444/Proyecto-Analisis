# Ejercicio1 Unidad1
# Ln(e+x)
def ejercicio1():
    import math
    import numpy as np
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese la cantidad de cifras significativas: "))
    Es = 0.5 * (math.pow(10,(2-n)))
    #print(Es)
    Ea = 100000
    xn0 = 1.0
    #print(xn0)
    xn1 = 0.0
    i=1
    print("Iteracion|\t Valor Aproximado |\tEa")
    print(i,"\t|\t ",xn0,"\t|\t - ")
    i=2
    while Ea>=Es:
        if i % 2 != 0:
            xn1 =float( xn0 - ((np.power(x,i-1))/((i-1)*(np.power(np.exp(1),i-1)))))
            Ea = float(abs(((xn1 - xn0) / xn1)) * 100)
            print(xn1, " - ")
        else:
            xn1 =float( xn0 + ((np.power(x,i-1))/((i-1)*(np.power(np.exp(1),i-1)))))
            Ea = float(abs(((xn1 - xn0) / xn1)) * 100)
            print(xn1, " + ")
        xn0=xn1
        print(i, "\t|\t", xn1, "\t|\t", Ea)
        i+=1
ejercicio1()