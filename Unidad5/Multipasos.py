from kutta4orden import KuttaGrado4

def f(xi, yi, funcion):
    valor = 0
    if "x" in funcion:
        funcion = funcion.replace("x", str(xi))
    if "y" in funcion:
        funcion = funcion.replace("y", str(yi))
    valor = eval(funcion)
    return valor

def adams_bash2(f,x0,y0,h,xF):
    muestras = 0
    i=x0
    while i < xF:
        muestras = muestras+1
        i += h

    lista=KuttaGrado4(f, x0, y0, h, muestras)
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[1]+(h/2)*(3*f(x[1],y[1])-(f(x[0],y[0])))
    y2=f(xF,y)
    lista[2]=[x[2],y]
    print("La tabla es:\n",lista)
    print(f"El valor de prediccion de f({x[2]}, {y}): ",y2)
    moul1paso(f, h, lista)


def adams_bash3(f,x0,y0,h,xF):
    muestras = 0
    i=x0
    while i < xF:
        muestras = muestras+1
        i += h

    lista=KuttaGrado4(f, x0, y0, h, muestras)
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[2]+(h/12)*(23*f(x[2],y[2])-16*f(x[1],y[1])+5*f(x[0],y[0]))
    y3=f(xF,y)
    lista[3]=[x[3],y]
    print("La tabla es:\n",lista)
    print(f"El valor de prediccion de f({x[3]}, {y}): ",y3)
    moul2paso(f, h, lista)


def adams_bash4(f,x0,y0,h,xF):
    muestras = 0
    i=x0
    while i < xF:
        muestras = muestras+1
        i += h

    lista=KuttaGrado4(f, x0, y0, h, muestras)
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[3]+(h/24)*(55*(f(x[3],y[3]))-59*f(x[2],y[2])+37*(f(x[1],y[1]))-9*(f(x[0],y[0])))
    y4=f(xF,y)
    lista[len(x-1)]=[xF,y]
    print("La tabla es:\n",lista)
    print(f"El valor de prediccion de f({xF}, {y}): ",y4)
    moul3paso(f, h, lista)

def moul1paso(f,h,lista):
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[1]+(h/2)*((f(x[2],y[2]))+f(x[1],y[1]))
    print("El valor de correcion es: ",y)


def moul2paso(f,h,lista):
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[2]+(h/12)*((5*f(x[2],y[2]))+8*f(x[1],y[1])-f(x[0],y[0]))
    print("El valor de correcion es: ",y)


def moul3paso(f,h,lista):
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[3]+(h/24)*(9*(f(x[4],y[4]))+19*f(x[3],y[3])-5*(f(x[2],y[2]))+(f(x[1],y[1])))
    print("El valor de correcion es: ",y)




def main():
    d=input("Ingrese y'")
    f=lambda x,y: eval(d)
    x0=float(input("Ingrese el valor de x0: "))
    y0=float(input("Ingrese el valor de y0: "))
    h=float(input("Ingrese el valor de H: "))
    xF=float(input("Ingrese el valor de x a evaluar en f(x)"))
    bash3pasos(f, x0, y0, h, xF)

main()