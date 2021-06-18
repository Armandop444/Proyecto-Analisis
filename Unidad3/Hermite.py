from sympy import parse_expr,Symbol,cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
from sympy import *
from Utilidades import limpiar, tablita
from FormulaEngine import castear, convertir_funcion, reconvertir_funcion
#el grado de una funcion mediante polinomios de hermite es dado por 2n+1

def pedir_valores(f,max):
    lista=[]
    total=1
    while True:
        limpiar()
        if max=="":
            print("Presione S para terminar de ingresar los datos en la lista")
        print("Valores \n",lista)
        dato= castear(f"Ingrese el valor de {f}({len(lista)}): ")
        if dato.upper()=="S" or (max==total and max!=""):
            if dato.upper()!="S":
                lista.append(float(eval(dato)))
            return lista
        else:
            try:
                lista.append(float(eval(dato)))
                total+=1
            except:
                continue


def hermiteNormal():
    x=symbols("x")
    xn=pedir_valores("x","")
    limpiar()
    opcionfuncion=int(input("desea ingresar una función para f(x) (1.Si  2.No)\n"))
    limpiar()
    if opcionfuncion==1:
        funcionpedida=input("ingrese la funcion:")
        limpiar()
        print(reconvertir_funcion(funcionpedida))
        funcionpedida=convertir_funcion(funcionpedida)
        funcionpedida=parse_expr(funcionpedida)
        fxn=[]
        for i in range(len(xn)):
            fxn.append(float(funcionpedida.subs(x,(xn[i]))))
        #print(fxn)
    else:
        fxn=pedir_valores("fi",len((xn)))
    #fxn=pedir_valores("fi",len((xn)))
    if opcionfuncion==1:
        opcionfuncion2=int(input("desea usar la misma funcion para df(x) (1.Si, hazlo  2.No, quiero ingresar valores)\n"))
    else:
        opcionfuncion2=2
    
    if opcionfuncion2==1:
        limpiar()
        funcionpedidaderivada=diff(funcionpedida,x)
        print(reconvertir_funcion(str(funcionpedidaderivada)))
        dfxn=[]
        for i in range(len(xn)):
            dfxn.append(float(funcionpedidaderivada.subs(x,(xn[i]))))
    else:
        dfxn=pedir_valores("y'",len(fxn))
    #dfxn=pedir_valores("y'",len(fxn))
    input("Presione cualquier tecla para continuar")
    limpiar()
    punto=""
    preguntapunto=int(input("Ingresará un punto? (1.Si  2.No)\n"))
    if preguntapunto==1:
        punto=input("Ingrese el punto a evaluar: ")
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
        punto=float(punto)
        print("el valor del punto dado ({0}) en el polinomio de hermite es: ".format(punto))
        print((polhermite.subs(x,punto)).expand())
