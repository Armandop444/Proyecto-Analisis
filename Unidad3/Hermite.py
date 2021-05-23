from sympy import *
#el grado de una funcion mediante polinomios de hermite es dado por 2n+1
def hermite(xn,fxn,dfxn,punto):
    ls=[]
    lsdiff=[]
    h=[]
    hvar=parse_expr("1")
    hgorritovar=parse_expr("1")
    hgorrito=[]
    x=Symbol("x")
    grado=0
    for i in xn:
        grado=grado+1
    print("se obtendrá una funcion de grado {0}, debido a que son {1} datos en xn".format(((2*(grado-1))+1),grado))
    #grado=grado+1
    polhermite=0
    l=parse_expr("1")
    for i in range(grado):
        for k in range(grado):
            if k!=i:
                l=l*((x-xn[k])/(xn[i]-xn[k]))
        l=l.expand()
        ls.append(l)
        lsdiff.append(l.diff(x))
        #print(l)
        l=parse_expr("1")
    #print(ls)
    #print(lsdiff)
    for i in range(grado):
        hvar=(1-2*(x-xn[i])*((lsdiff[i]).subs(x,xn[i])))*((ls[i])**2)
        hgorritovar=(x-xn[i])*((ls[i])**2)
        hvar=hvar.expand()
        hgorritovar=hgorritovar.expand()
        h.append(hvar)
        hgorrito.append(hgorritovar)
    #print(h)
    #print(hgorrito)
    for i in range(grado):
        polhermite=polhermite+((fxn[i])*(h[i]))+((dfxn[i])*(hgorrito[i]))
    polhermite=polhermite.expand()
    print("el polinomio es: ")
    print(polhermite)
    print("")
    if punto!="":
        print("el valor del punto dado ({0}) en el polinomio de hermite es: ".format(punto))
        print((polhermite.subs(x,punto)).expand())
    return 0




xn=[1.3,1.6,1.9]
fxn=[0.6200860,0.4554022,0.2818186]
dfxn=[-0.5220232,-0.5698959,-0.5811571]
uwu=hermite(xn,fxn,dfxn,1.5)
print(uwu)















