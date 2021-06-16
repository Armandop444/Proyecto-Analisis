from numpy import zeros
from sympy import factorial,diff,Symbol,cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
from FormulaEngine import convertir_funcion
from Utilidades import tablita, limpiar
x=Symbol("x")

def imprimir(Matriz,nivel):
    tabla=tablita(["Xi","Yi"],show_iteracion=False)
    for xn in range(nivel):
        columna=[]
        for fx in range(2):
            columna.append(Matriz[xn,fx])
        tabla.add_fila(columna)
    tabla.print_table()

def f(xi, yi, funcion):
    valor = 0
    if "x" in funcion:
        funcion = funcion.replace("x", str(xi))
    if "y" in funcion:
        funcion = funcion.replace("y", str(yi))
    valor = eval(funcion)
    return valor

def calcularDerivadas(dy,tamanio):
    derivadas=[]
    for i in range(tamanio-1):
        if "y" in dy:
            dy=dy.replace("y", "f(x)")
        d= diff(dy)
        d=str(d)
        if "Derivative(f(x), x)" in d:
            dy=dy.replace("f(x)", "y")
            d=d.replace("Derivative(f(x), x)",dy)
        derivadas.append(str(d))
    return derivadas

def taylor(dy,x0,y0,h,tamanio,fx):
    derivadas=[]

    derivadas=calcularDerivadas(dy, tamanio)
    derivadas.insert(0, dy)
    tamanio = tamanio + 1
    i=x0
    a=0
    while i <= fx:
        a = a+1
        i += h
    estimado = zeros(shape=(a,2))
    estimado[0] = [x0,y0]
    x = x0
    y = y0
    muestras=1
    for i in range(1,a,1):
        y0=y
        for j in range(1,tamanio,1):
            if j>0:
                d2y= derivadas[j-1]
                y= y + f(x,y0,d2y)*(h**j/factorial(j))
                if i==1:
                    estimado[i]= [f(x,y,dy),f(x,y,dy)]
            else:
                y=y
        muestras+=1
        x = x+h
        estimado[i] = [x,y]
    imprimir(estimado, muestras)

dy="y-x"
dy=convertir_funcion(dy)
x0 = 1
y0 = 3
h = 0.5
orden = 3
fx=5

# PROCEDIMIENTO
puntos = taylor(dy,x0,y0,h,orden,fx)
