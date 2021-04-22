
from FormulaEngine import convertir_funcion
from Utilidades import raiz, tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, diff, Abs




def NewtonR(func, xi, es):
    tabla = tablita(["xi","f(xn)","df(xn)","d2f(xn)","x(n+1)","ea"])
    itera = 0
    dfx=str(diff(func))
    d2fx=str(diff(dfx))
    xa=0
    d2fxn=0.0
    dfxn=0.0
    fxn=0.0
    xnmas1=0.0
    ea=100.0
    convergencia=0.0
    fxn = eval(convertir_funcion(func,var_n="xi"))
    dfxn = eval(convertir_funcion(dfx,var_n="xi"))
    d2fxn = eval(convertir_funcion(d2fx,var_n="xi"))
    convergencia=Abs((fxn*d2fxn)/(dfxn**2))

    if convergencia<1 :
        print("condicion de convergencia<1 cumplido, la convergencia es: ")
        print(convergencia)
        print("")
        while ea > es:
            if itera==0:
                xa=xi
                fxn = eval(convertir_funcion(func,var_n="xi"))
                fxn=float(fxn)
                dfxn = eval(convertir_funcion(dfx,var_n="xi"))
                dfxn=float(dfxn)
                d2fxn = eval(convertir_funcion(d2fx,var_n="xi"))
                d2fxn=float(d2fxn)
                xnmas1 = xi-(fxn/dfxn)
                ea=(Abs((xnmas1-xi)/xnmas1))*100
            else:
                xa=xnmas1
                fxn = eval(convertir_funcion(func,var_n="xa"))
                fxn=float(fxn)
                dfxn = eval(convertir_funcion(dfx,var_n="xa"))
                dfxn=float(dfxn)
                d2fxn = eval(convertir_funcion(d2fx,var_n="xa"))
                d2fxn=float(d2fxn)
                xnmas1=xa-(fxn/dfxn)
                ea=(Abs((xnmas1-xa)/xnmas1))*100
            itera=itera+1
            tabla.add_fila([xa,fxn,dfxn,d2fxn,xnmas1,ea])
        print("la raiz es: {}".format(xnmas1))   
        return tabla.get_tabla()
        
    else:
        print("la convergencia es mayor que 1:\n" )
        return convergencia

#xi es igual a 0.5 para este ejercicio
#xf=float(input("ingrese el valor de xinicial\n"))
#funcion="x^3+x-1"
#a = NewtonR(funcion, (0.7), 0.05)
#print(a)