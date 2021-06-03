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


def mul(b,n):
    m=1.0
    for i in range(n):
        m=m*(b-i)
    return m


def grange():
    limpiar()
    x=Symbol("x")
    funcion=""
    punto=""
    grado=int(input("Que grado de polinomio desea encontrar\n"))
    opcion=input("¿Ingresara una funcion para evaluar en un punto? 1.Si 2.No")
    if opcion=="1":
        funcion=input("Ingrese la funcion\n")
        punto=float(input("Ingrese el punto a evaluar\n"))
    dic=pedir_valores()
    limpiar()
    xi=dic["xi"]
    fi=dic["fi"]
    px=0
    for i in range(grado):
        l=fi[i]
        for k in range(grado):
            if k!=i:
                l=l*((x-xi[k])/(xi[i]-xi[k]))
        px=px+l

    #Tabla
    xi.insert(0, "xi")
    fi.insert(0, "fi")
    tabla=tablita("",show_iteracion=False)
    tabla.add_fila(xi)
    tabla.add_fila(fi)
    tabla.print_table()
    px=px.expand()
    print("Polinomio simplificado:",reconvertir_funcion(str(px)),"\n")
    
    if punto !="" and funcion!="":
        n=len(xi)-1
        error=0.0
        fac=factorial(n)
        f=convertir_funcion(funcion)
        derivada=""
        for i in range(n):
            derivada=diff(f)
            f=str(derivada)
        m=mul(punto,n)
        mayor=0
        for i in range(len(xi)):
            if i!=0:
                if mayor<abs(xi[i]):
                    mayor=xi[i]
        fderivada=derivada.subs(x,mayor)
        error=(fderivada/fac)*m
        px=float(eval(convertir_funcion(str(px),var_n="punto")))
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
            px=float(eval(convertir_funcion(str(px),var_n="punto")))
            print(f"Evaluacion en f({punto}):",px)