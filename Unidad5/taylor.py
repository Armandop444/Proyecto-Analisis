from numpy import zeros
from sympy import factorial,diff,Symbol,cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
x=Symbol("x")

def f(xi, yi, funcion):
    valor = 0
    if "x" in funcion:
        funcion = funcion.replace("x", str(xi))
    if "y" in funcion:
        funcion = funcion.replace("y", str(yi))
    valor = eval(funcion)
    return valor

def calcularDerivadas(dy,muestras):
    derivadas=[]
    for i in range(muestras-1):
        if "y" in dy:
            dy=dy.replace("y", "f(x)")
        d= diff(dy)
        d=str(d)
        if "Derivative(f(x), x)" in d:
            dy=dy.replace("f(x)", "y")
            d=d.replace("Derivative(f(x), x)",dy)
        derivadas.append(str(d))
    return derivadas

def taylor(dy,x0,y0,h,muestras,fx):
    derivadas=[]

    derivadas=calcularDerivadas(dy, muestras)
    derivadas.insert(0, dy)
    tamano = muestras + 1
    estimado = zeros(shape=(fx,2))
    estimado[0] = [x0,y0]
    x = x0
    y = y0
    for i in range(1,fx,1):
        y0=y
        for j in range(1,tamano,1):
            if j>0:
                d2y= derivadas[j-1]
                y= y + f(x,y0,d2y)*(h**j/factorial(j))
                if i==1:
                    estimado[i]= [f(x,y,dy),f(x,y,dy)]
            else:
                y=y
        x = x+h
        estimado[i] = [x,y]
    return(estimado)

dy="y-cos(x)"
x0 = 1
y0 = 3
h = 1
muestras = 3
fx=5

# PROCEDIMIENTO
puntos = taylor(dy,x0,y0,h,muestras,fx)

# SALIDA
print('estimado[xi, yi]')
print(puntos)