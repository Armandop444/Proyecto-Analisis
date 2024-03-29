# Ejercicio9 Unidad1
# ln(1+x)
from Utilidades import tablita
from sympy import Pow, factorial
def ejercicio9(x,Es):
    Ea = 100000
    xn0 = 0.0
    xn1 = 0.0
    i=1
    #print("%-20s %-20s %-20s" % ("iteracion", "Xn1", "Ea"))
    tabla=tablita(["xn1","Ea"])
    while Ea>=Es:
        if x!=0:
            xn1 = xn0 + ((Pow(-1,i-1))*((Pow(x,i))/(i)))
            Ea = float(abs(((xn1 - xn0) /( xn1))) * 100)
            xn0=xn1
            #print("%-20d %-20s %-20s" % (i, xn1, Ea))
            tabla.add_fila([xn1,Ea])
        else:
            #print("%-20d %-20s %-20s" % (i, 0, 0))
            break
        i+=1
    return tabla.get_tabla()