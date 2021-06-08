# Ejercicio6 Unidad1
# sh x
from Utilidades import raiz, tablita
from sympy import ln, exp, Pow, factorial
def ejercicio6(x,Es):
    tabla=tablita(["Xn1","Ea"])
    Ea = 100000
    xn0 = 0.0
    xn1 = 0.0
    i=0
    while Ea>=Es:
        xn1 = xn0 + ((Pow(x,(2*i)+1))/factorial((2*i)+1))
        Ea = float(abs(((xn1 - xn0) /( xn1))) * 100)
        xn0=xn1
        #print("%-20d %-20s %-20s" % (i, xn1, Ea))
        tabla.add_fila([xn1,Ea])
        i+=1
    return tabla.get_tabla()