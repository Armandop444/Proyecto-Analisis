# Ejercicio7 Unidad1
# ch x
from Utilidades import raiz, tablita
from sympy import ln, exp, Pow, factorial
def ejercicio7(x,Es):
    tabla=tablita(["xn1","Ea"])
    Ea = 100000
    xn0 = 1.0
    xn1 = 0.0
    i=0
    #print("%-20s %-20s %-20s" % ("iteracion", "Xn1", "Ea"))
    tabla.add_fila([xn0,"-"])
    while Ea>=Es:
        if i!=0:
            xn1 = xn0 + ((Pow(x,2*i))/factorial(2*i))
            Ea = float(abs(((xn1 - xn0) /( xn1))) * 100)
            xn0=xn1
            #print("%-20d %-20s %-20s" % (i, xn1, Ea))
            tabla.add_fila([xn1,Ea])
        i+=1
    return tabla.get_tabla()