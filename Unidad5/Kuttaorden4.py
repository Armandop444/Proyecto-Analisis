from numpy import zeros
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
from Utilidades import tablita, limpiar
from FormulaEngine import convertir_funcion
def f(xi, yi, funcion):
    valor = 0
    if "x" in funcion:
        funcion = funcion.replace("x", str(xi))
    if "y" in funcion:
        funcion = funcion.replace("y", str(yi))
    valor = eval(funcion)
    return valor

def imprimir(Matriz,nivel):
    tabla=tablita(["Xi","Yi"],show_iteracion=False)
    for xn in range(nivel):
        columna=[]
        for fx in range(2):
            columna.append(Matriz[xn,fx])
        tabla.add_fila(columna)
    tabla.print_table()


def KuttaGrado4(dy, x0, y0, h,muestras):

    tamano = muestras + 1
    estimado = zeros(shape=(tamano, 2), dtype=float)

    # incluye el punto [x0,y0]
    estimado[0] = [x0, y0]
    xi = x0
    yi = y0
    for i in range(1, tamano, 1):
        K1 = h * f(xi, yi, dy)
        K2 = h * f(xi + h / 2, yi + K1 / 2, dy)
        K3 = h * f(xi + h / 2, yi + K2 / 2, dy)
        K4 = h * f(xi + h, yi + K3, dy)

        yi = yi + (1 / 6) * (K1 + 2 * K2 + 2 * K3 + K4)
        xi = xi + h

        estimado[i] = [xi, yi]
    return estimado

def Kutta():
    dy = input("Ingrese la y´")
    dy=convertir_funcion(dy)
    x0 = float(input("ingrese X0\n"))
    y0 = float(input("ingrese Y0\n"))
    h = float(input("ingrese h\n"))
    i = x0
    pregunta = input(
        "Como quiere operar\n1.Con # de iteraciones\n2.Evaluacion en un punto de f(x)")
    if pregunta == "2":
        xF = float(input("Ingrese el punto de f(x)"))
        muestras = 0
        while i <= xF:
            muestras = muestras+1
            i += h
    elif pregunta=="1":
        muestras = int(input("Ingrese el # de iteraciones que desea hacer"))
    estimado=KuttaGrado4(dy, x0, y0, h,muestras)
    limpiar()
    imprimir(estimado, muestras)
