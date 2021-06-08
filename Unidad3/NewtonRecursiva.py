from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, Symbol,factorial, diff, parse_expr, Abs
from Utilidades import limpiar, tablita
from FormulaEngine import convertir_funcion, reconvertir_funcion

def pedir_valores():
    valores = {}
    total=1
    total_datos = 0
    d = 0
    while True:
        limpiar()
        xn = "xi"
        if xn=="xi" and total_datos!=0:
            xn="fi"
        fila = []
        if xn.upper() == "T":
            valores["total"] = total_datos
            return valores
        else:
            #xn = float(xn)
            n = 0
            while True:
                limpiar()
                if d!=0:
                    print("Valores\nxi:",valores["xi"])
                    if n!=0:
                        print("fi:",fila)
                else:
                    print("Presione 'S' para terminar de ingresar datos de la fila")
                    print("Valores\nxi:",fila)
                valor = input(f"\t Ingrese el valor de X{n} " if d == 0 else f"\t Ingrese el valor de la Fi(x{n})")
                if (n/total)==1 and xn=="fi" :
                    if (n/total)==1:
                        fila.append(float(valor))
                        total_datos += 1
                    valores[str(xn)]=fila
                    valores["total"] = total_datos
                    return valores
                elif valor.upper() == "S":
                    valores[str(xn)]=fila
                    total=total_datos-1
                    d = 1
                    break
                else:
                    fila.append(float(valor))
                    total_datos += 1
                    n += 1




def multiplicacion(b, i, listax):
    mul = 1
    for k in range(i):
        resta = listax[b] - listax[k]
        mul = mul * resta
    return mul


def restaTotal(listaA, b, listax):
    tamanio = len(listaA)
    total = 0
    for i in range(tamanio):
        total = total + (listaA[i] * multiplicacion(b, i, listax))
    return total


def muldiv(b, listax):
    div = 1.0
    for i in range(b):
        div = div * (listax[b] - listax[i])
    return div

def mul(b,n):
    m=1.0
    for i in range(n):
        m=m*(b-i)
    return m

def newton():
    limpiar()
    listaA = []
    b = 0
    funcion=""
    punto=""
    iteracion = int(input("Ingrese el grado que desea del polinomio\n"))
    opcion=input("¿Ingresara una funcion para evaluar? 1.Si 2.No")
    if opcion=="1":
        funcion=input("Ingrese la funcion\n")
        punto=float(input("Ingrese el punto a evaluar\n"))
    dic=pedir_valores()
    limpiar()
    listax=dic["xi"]
    listaf=dic["fi"]
    iteracion=iteracion+1
    for i in range(iteracion):
        if i == 0:
            listaA.append(listaf[b])
        elif i == 1:
            bsub = (listaf[1] - listaf[0]) / (listax[1] - listax[0])
            listaA.append(bsub)
            b = b + 1
        else:
            b = b + 1
            bsub = (listaf[i] - restaTotal(listaA, b, listax)) / muldiv(b, listax)

            listaA.append(bsub)

    variablesB = listaA

    x = Symbol('x')
    polinomio = listaf[0]
    for j in range(1,iteracion,1):
        factor = variablesB[j]
        termino = 1
        for k in range(0,j,1):
                termino = termino*(x-listax[k])
        polinomio = polinomio + termino*factor

    polisimple = polinomio.expand()
    
    # SALIDA
    #Tabla
    listax.insert(0, "xi")
    listaf.insert(0, "fi")
    tabla=tablita("",show_iteracion=False)
    tabla.add_fila(listax)
    tabla.add_fila(listaf)
    tabla.print_table()
    print("\nTabla de valores de b")
    cabezeros=[]
    for i in range(len(variablesB)):
        b="b"+str(i)
        cabezeros.append(b)
    tablaB=tablita(cabezeros,show_iteracion=False)
    tablaB.add_fila(variablesB)
    tablaB.print_table()

    print('\npolinomio simplificado: ' )
    print(reconvertir_funcion(str(polisimple)),"\n")

    if punto !="" and funcion!="":
        n=len(listax)-1
        error=0.0
        fac=factorial(n)
        f=convertir_funcion(funcion)
        derivada=""
        for i in range(n):
            derivada=diff(f)
            f=str(derivada)
        m=mul(punto,n)
        mayor=0
        for i in range(len(listax)):
            if i!=0:
                if mayor<abs(listax[i]):
                    mayor=listax[i]
        fderivada=derivada.subs(x,mayor)
        error=(fderivada/fac)*m
        px=float(eval(convertir_funcion(str(polisimple),var_n="punto")))
        funcion=float(eval(convertir_funcion(funcion,var_n="punto")))
        errorT=Abs((funcion-px)/(funcion))*100
        print(f"Evaluacion en f({punto}):",px)
        print()
        print("Derivada:",reconvertir_funcion(str(derivada)))
        print("Error Porcentual:",errorT)
        print("Error Teorico",error)
    else:
        opcion=input("Desea interpolar en algun punto 1.SI 2.NO")
        if opcion=="1":
            punto=float(input("Ingrese el punto a interpolar"))
            px=float(eval(convertir_funcion(str(polisimple),var_n="punto")))
            print(f"Evaluacion en f({punto}):",px)
newton()