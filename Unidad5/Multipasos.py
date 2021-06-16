from Unidad5.Kuttaorden4 import KuttaGrado4
from sympy import factorial,diff,Symbol,cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
from FormulaEngine import convertir_funcion
from Utilidades import tablita, limpiar

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

def adams_bash2(funcion,x0,y0,h,xF):
    muestras = 0
    i=x0
    while i <= xF:
        muestras = muestras+1
        i += h

    lista=KuttaGrado4(funcion, x0, y0, h, muestras)
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[1]+(h/2)*(3*f(x[1],y[1],funcion)-(f(x[0],y[0],funcion)))
    y2=f(xF,y,funcion)
    lista[2]=[x[2],y]
    imprimir(lista, muestras)
    print(f"El valor de prediccion de f({x[2]}, {y}): ",y2)
    moul1paso(funcion, h, lista)


def adams_bash3(funcion,x0,y0,h,xF):
    muestras = 0
    i=x0
    while i <= xF:
        muestras = muestras+1
        i += h

    lista=KuttaGrado4(funcion, x0, y0, h, muestras)
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[2]+(h/12)*(23*f(x[2],y[2],funcion)-16*f(x[1],y[1],funcion)+5*f(x[0],y[0],funcion))
    y3=f(xF,y,funcion)
    lista[3]=[x[3],y]
    imprimir(lista, muestras)
    print(f"El valor de prediccion de f({x[3]}, {y}): ",y3)
    moul2paso(funcion, h, lista)


def adams_bash4(funcion,x0,y0,h,xF):
    muestras = 0
    i=x0
    while i <= xF:
        muestras = muestras+1
        i += h

    lista=KuttaGrado4(funcion, x0, y0, h, muestras)
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[3]+(h/24)*(55*(f(x[3],y[3],funcion))-59*f(x[2],y[2],funcion)+37*(f(x[1],y[1],funcion))-9*(f(x[0],y[0],funcion)))
    y4=f(xF,y,funcion)
    lista[4]=[x[4],y]
    imprimir(lista, muestras)
    print(f"El valor de prediccion de f({x[4]}, {y}): ",y4)
    moul3paso(funcion, h, lista)

def moul1paso(funcion,h,lista):
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[1]+(h/2)*((f(x[2],y[2],funcion))+f(x[1],y[1],funcion))
    print("El valor de correcion es: ",y)


def moul2paso(funcion,h,lista):
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[2]+(h/12)*((5*f(x[2],y[2],funcion))+8*f(x[1],y[1],funcion)-f(x[0],y[0],funcion))
    print("El valor de correcion es: ",y)


def moul3paso(funcion,h,lista):
    x = lista[:, 0]
    y = lista[:, 1]
    y=y[3]+(h/24)*(9*(f(x[4],y[4],funcion))+19*f(x[3],y[3],funcion)-5*(f(x[2],y[2],funcion))+(f(x[1],y[1],funcion)))
    print("El valor de correcion es: ",y)




def main():
    limpiar()
    print("Multipasos")
    opcion=int(input("Metodos de Adams-Bashforth:\n1.Con 2 pasos\n2.Con 3 pasos\n3.Con 4 pasos\n"))
    if opcion>0 and opcion<4:
        d=input("Ingrese y'\n")
        d=convertir_funcion(d)
        x0=float(input("Ingrese el valor de x0: "))
        y0=float(input("Ingrese el valor de y0: "))
        h=float(input("Ingrese el valor de H: "))
        xF=float(input("Ingrese el valor de x a evaluar en f(x) "))
        limpiar()
    if opcion==1:
        adams_bash2(d, x0, y0, h, xF)
    elif opcion==2:
        adams_bash3(d, x0, y0, h, xF)
    elif opcion==3:
        adams_bash4(d, x0, y0, h, xF)
    else:
        print("Opcion no valida")