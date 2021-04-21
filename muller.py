from numpy import sign
from numpy.lib.scimath import sqrt
from Utilidades import tablita


def muller(f, x0, x1, x2, tol):
    tabla = tablita(["X0", "X1", "X2","X3", "EA"])
    error = 1e3
    x3 = 0
    while error > tol:
        c = f(x2)
        b = ((x0 - x2)**2 * (f(x1) - f(x2)) - (x1 - x2)**2 *
             (f(x0) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        a = ((x1 - x2) * (f(x0) - f(x2)) - (x0 - x2) *
             (f(x1) - f(x2))) / ((x0 - x2) * (x1 - x2) * (x0 - x1))
        x3 = x2 - (2 * c) / (b + sign(b) * sqrt(b**2 - 4 * a * c))
        error = abs(x3 - x2)*100
        x0 = x1
        x1 = x2
        x2 = x3
        tabla.add_fila([x1, x2, x3, error])

    return tabla.get_tabla()


f=lambda x:x**4-7*x**3+13*x**2+23*x-78
muller(f,2,2.5,2.7,0.05)