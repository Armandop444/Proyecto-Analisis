from numpy import sign
from numpy.lib.scimath import sqrt
from FormulaEngine import convertir_funcion
from Utilidades import raiz, tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan

def muller(f, x0, x1, x2, tol):
    tabla = tablita(["X0", "X1", "X2","X3", "EA"])
    error = 1e3
    x3 = 0
    while error > tol:
        #c = f(x2)
        c = eval(convertir_funcion(f,var_n="x2"))
        fx0 = eval(convertir_funcion(f,var_n="x0")) 
        fx1 = eval(convertir_funcion(f,var_n="x1"))
        fx2 = eval(convertir_funcion(f,var_n="x2"))
        
        #b = ((x0 - x2)**2 * (f(x1) - f(x2)) - (x1 - x2)**2 *
        #     (f(x0) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        b = ((x0 - x2)**2 * (fx1 - fx2) - (x1 - x2)**2 *
             (fx0 - fx2)) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        #a = ((x1 - x2) * (f(x0) - f(x2)) - (x0 - x2) *
        #     (f(x1) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        a= ((x1 - x2) * (fx0 - fx2) - (x0 - x2) *
             (fx1 - fx2)) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        x3 = x2 - (2 * c) / (b + sign(b) * sqrt(b**2 - 4 * a * c))
        error = abs(x3 - x2)*100
        x0 = x1
        x1 = x2
        x2 = x3
        tabla.add_fila([x1, x2, x3, error])

    return tabla.get_tabla()


"""f="x**4-7*x**3+13*x**2+23*x-78"
print("efe: ",f)
a=muller(f,2,2.5,2.7,0.05)
print(a)"""