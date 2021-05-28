from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, Symbol,factorial, diff


def mul(b,n):
    m=1.0
    for i in range(n):
        m=m*(b-i)
    return m


def grange(xi,fi,funcion,punto,grado):

    x=Symbol("x")

    grado=grado+1
    px=0
    for i in range(grado):
        l=fi[i]
        for k in range(grado):
            if k!=i:
                #print("FI:",l)
                l=l*((x-xi[k])/(xi[i]-xi[k]))
                #print("xi:",xi[i])
                #print("xi2:",xi[k])
                #print("Polinomio: \n",l)
        px=px+l
    
    print("Polinomio sin simplificar:\n",px,"\n")
    px=px.expand()
    print("Polinomio simplificado:",px,"\n")
    
    if punto !="" and funcion!="":
        n=len(xi)
        error=0.0
        fac=factorial(n)
        f=funcion
        derivada=""
        for i in range(n):
            derivada=diff(f)
            f=str(derivada)
        m=mul(punto,n)
        mayor=0
        for i in range(len(xi)):
            if mayor<abs(xi[i]):
                mayor=xi[i]
        fderivada=derivada.subs(x,mayor)
        error=(fderivada/fac)*m
        px=px.subs(x,punto)
        print("Evaluacion:",px)
        print()
        print("Derivada:",derivada)
        print("Error",error)



    return 0

"""
xi = [0,0.5,1]
fi = [1,1.64,2.71]
g=grange(xi,fi,"2.71**x",0.25,2)
print(g)"""


cont = 0
numero = 0
final = input("Ingrese el grado del polinomio \n")
final = int(final)
xi = [""]*(final+1)
while cont < final+1:
    mensaje = "Ingrese el valor de Xi para la posicion: {0} \n".format(cont+1)
    numero = float(input(mensaje))
    xi[cont] = numero
    cont = cont+1
print(xi)
cont = 0
fi = [""]*(final+1)
while cont < final+1:
    #print("estoy en segundo bucle con el contador en {0}".format(cont))
    mensaje = "Ingrese el valor de fi para la posicion: {0} \n".format(cont+1)
    numero = float(input(mensaje))
    fi[cont] = numero
    cont = cont+1
print(fi)

funcion=0
punto=0
opcion=input("¿Ingresara una funcion para evaluar en un punto? 1.Si 2.No")
if opcion==1:
    funcion=input("Ingrese la funcion a evaluar")
    punto= input("Ingrese el punto a evaluar con la funcion {}".format(funcion))

g=grange(xi,fi,funcion,punto,final)
