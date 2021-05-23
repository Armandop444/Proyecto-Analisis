from sympy import *

def hermiteDD(xn,fxn,dfxn,grado,punto):
    ls=[]
    lsdiff=[]
    h=[]
    hvar=parse_expr("1")
    hgorritovar=parse_expr("1")
    hgorrito=[]
    x=Symbol("x")
    grado=grado+1
    polhermite=0
    l=parse_expr("1")
    for i in range(grado):
        for k in range(grado):
            if k!=i:
                l=l*((x-xn[k])/(xn[i]-xn[k]))
        l=l.expand()
        ls.append(l)
        lsdiff.append(l.diff(x))
        print(l)
        l=parse_expr("1")
    print(ls)
    print(lsdiff)
    for i in range(grado):
        hvar=(1-2*(x-xn[i])*((lsdiff[i]).subs(x,xn[i])))*((ls[i])**2)
        hgorritovar=(x-xn[i])*((ls[i])**2)
        hvar=hvar.expand()
        hgorritovar=hgorritovar.expand()
        h.append(hvar)
        hgorrito.append(hgorritovar)
    print(h)
    print(hgorrito)
    for i in range(grado):
        polhermite=polhermite+((fxn[i])*(h[i]))+((dfxn[i])*(hgorrito[i]))
    polhermite=polhermite.expand()
    print(polhermite)
    if punto!="":
        print((polhermite.subs(x,punto)).expand())
    return 0




xn=[1.3,1.6,1.9]
fxn=[0.6200860,0.4554022,0.2818186]
dfxn=[-0.5220232,-0.5698959,-0.5811571]
uwu=hermiteDD(xn,fxn,dfxn,2,1.5)
print(uwu)















