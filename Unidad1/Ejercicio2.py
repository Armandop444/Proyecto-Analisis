# Ejercicio2 Unidad1
# e^x^2
from Utilidades import raiz, tablita
from sympy import exp, Pow, factorial
def ejercicio2(x,Es):
    tabla=tablita(["xn","ea"])
    #print(Es)
    Ea = 100000
    i = 1
    xn0 = 1.0+ Pow(x,2)
    tabla.add_fila([xn0,"-"])
    #print(xn0)
    xn1 = 0.0
    #print("%-20s %-20s %-20s" % ("iteracion", "Xn1", "Ea"))
    #print("%-20d %-20s %-20s" % (i, xn0, "-"))
    i=2
    while Ea>=Es:
        xn1 = xn0 +((Pow(x,(2*(i))))/factorial(i))
        Ea = float(abs(((xn1 - xn0) / xn1)) * 100)
        xn0=xn1
        #print("%-20d %-20s %-20s" % (i, xn1, Ea))
        tabla.add_fila([xn1,Ea])
        i+=1

    return tabla.get_tabla()
