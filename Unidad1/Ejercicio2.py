# Ejercicio2 Unidad1
# e^x^2
def ejercicio2():
    import math
    import numpy as np
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese la cantidad de cifras significativas: "))
    Es = 0.5 * (math.pow(10,(2-n)))
    #print(Es)
    Ea = 100000
    i = 1
    xn0 = 1.0+ math.pow(x,2)
    #print(xn0)
    xn1 = 0.0
    print("%-20s %-20s %-20s" % ("iteracion", "Xn1", "Ea"))
    print("%-20d %-20s %-20s" % (i, xn0, "-"))
    i=2
    while Ea>=Es:
        xn1 = xn0 +((np.power(x,(2*(i))))/math.factorial(i))
        Ea = float(abs(((xn1 - xn0) / xn1)) * 100)
        xn0=xn1
        print("%-20d %-20s %-20s" % (i, xn1, Ea))
        i+=1

ejercicio2()