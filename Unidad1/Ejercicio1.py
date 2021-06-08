# Ejercicio1 Unidad1
# Ln(e+x)
from Utilidades import tablita
from sympy import exp, Pow
def ejercicio1(xn,Es):
    tabla =tablita(["xn","EA"])
    x = xn
    #print(Es)
    Ea = 100000
    xn0 = 1.0
    #print(xn0)
    xn1 = 0.0
    tabla.add_fila([xn0,"-"])
    i=2
    while Ea>=Es:
        if i % 2 != 0:
            xn1 =float( xn0 - ((Pow(x,i-1))/((i-1)*(Pow(exp(1),i-1)))))
            Ea = float(abs(((xn1 - xn0) / xn1)) * 100)
        else:
            xn1 =float( xn0 + ((Pow(x,i-1))/((i-1)*(Pow(exp(1),i-1)))))
            Ea = float(abs(((xn1 - xn0) / xn1)) * 100)
        xn0=xn1
        tabla.add_fila([xn1,Ea])
        i+=1
    return tabla.get_tabla()