from sympy import *
from Utilidades import limpiar, tablita
#el grado de una funcion mediante polinomios de hermite es dado por 2n+1

def pedir_valores(f,max):
    lista=[]
    total=1
    while True:
        limpiar()
        if max=="":
            print("Presione S para terminar de ingresar los datos en la lista")
        print("Valores \n",lista)
        dato= input(f"Ingrese el valor de {f}({len(lista)}): ")
        if dato.upper()=="S" or (max==total and max!=""):
            if dato.upper()!="S":
                lista.append(float(dato))
            return lista
        else:
            try:
                lista.append(float(dato))
                total+=1
            except:
                continue


def hermite():
    xn=pedir_valores("x","")
    fxn=pedir_valores("fi",len((xn)))
    dfxn=pedir_valores("y'",len(fxn))
    limpiar()
    punto=float(input("Ingrese el punto a evaluar: "))
    ls=[]
    lsdiff=[]
    h=[]
    hvar=parse_expr("1")
    hgorritovar=parse_expr("1")
    hgorrito=[]
    x=Symbol("x")
    grado=int(input("Ingrese el grado que quiere encontrar"))
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

    tabla=tablita("",show_iteracion=False)
    xn.insert(0, "Xi")
    fxn.insert(0, "Fi")
    dfxn.insert(0, "y'")
    tabla.add_fila(xn)
    tabla.add_fila(fxn)
    tabla.add_fila(dfxn)
    limpiar()
    tabla.print_table()
    print("\nEl polinomio es: ")
    print(polhermite)
    print("")
    if punto!="":
        print("el valor del punto dado ({0}) en el polinomio de hermite es: ".format(punto))
        print((polhermite.subs(x,punto)).expand())

xn=[1.3,1.6,1.9]
fxn=[0.6200860,0.4554022,0.2818186]
dfxn=[-0.5220232,-0.5698959,-0.5811571]
hermite()