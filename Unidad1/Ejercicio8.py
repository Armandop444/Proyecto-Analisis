# Ejercicio8 Unidad1
# arcsen x
from Utilidades import tablita
from sympy import Pow, factorial
def ejercicio8(x,Es):
    Ea = 100000
    xn0 = 0.0
    xn1 = 0.0
    i=0
    tabla=tablita(["xn1","Ea"])
    while Ea>=Es:
        if x!=0:
            xn1 = xn0 + (((factorial(2*i))/(Pow(((Pow(2,i))*factorial(i)),2)))*((Pow(x,(2*i)+1))/(((2*i)+1))))
            Ea = float(abs(((xn1 - xn0) /( xn1))) * 100)
            xn0=xn1
            tabla.add_fila([xn1,Ea])
        else:
            tabla.add_fila([0,0])
            break
        i+=1
    return tabla.get_tabla()