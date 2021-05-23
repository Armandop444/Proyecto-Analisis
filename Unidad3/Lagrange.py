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


    print("PX:\n",px,"\n")
    px=px.expand()
    print("Simplificado:",px,"\n")
    px=px.subs(x,punto)
    print("Evaluacion:",px)
    print()
    print("Derivada:",derivada)
    print("Error",error)
    return 0


xi = [0,0.5,1]
fi = [1,1.64,2.71]
g=grange(xi,fi,"2.71**x",0.25,2)
print(g)
