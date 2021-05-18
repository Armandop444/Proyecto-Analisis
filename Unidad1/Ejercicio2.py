# Ejercicio2 Unidad1
# e^x^2
def ejercicio2():
    import math
    x = float(input("Ingrese el valor de x: "))
    n = int(input("Ingrese la cantidad de cifras significativas: "))
    Es = 0.5 * (math.pow(10,(2-n)))
    #print(Es)
    Ea = 100000
    i = 1
    xn0 = 1.0+ math.pow(x,2)
    #print(xn0)
    xn1 = 0.0
    print("Iteracion|\t Valor Aproximado |\tEa")
    print(i,"\t|\t ",xn0,"\t|\t - ")
    i=2
    while Ea>=Es:
        xn1 = xn0 +((math.pow(x,(2*(i-1))))/math.factorial(i))
        Ea = float(abs(((xn1 - xn0) / xn1)) * 100)
        xn0=xn1
        print(i, "\t|\t", xn1, "\t|\t", Ea)
        i+=1

ejercicio2()