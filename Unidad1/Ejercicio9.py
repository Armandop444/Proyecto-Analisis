# Ejercicio9 Unidad1
# ln(1+x)
def ejercicio9():
    import math
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese la cantidad de cifras significativas: "))
    Es = 0.5 * (math.pow(10,(2-n)))
    Ea = 100000
    xn0 = 0.0
    xn1 = 0.0
    i=1
    print("%-20s %-20s %-20s" % ("iteracion", "Xn1", "Ea"))
    while Ea>=Es:
        if x!=0:
            xn1 = xn0 + ((math.pow(-1,i-1))*((math.pow(x,i))/(i)))
            Ea = float(abs(((xn1 - xn0) /( xn1))) * 100)
            xn0=xn1
            print("%-20d %-20s %-20s" % (i, xn1, Ea))
        else:
            print("%-20d %-20s %-20s" % (i, 0, 0))
            break
        i+=1


ejercicio9()