from Utilidades import limpiar, tablita
from sympy import poly_from_expr
from FormulaEngine import convertir_funcion, reconvertir_funcion,castear
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan, Symbol,factorial, diff, parse_expr, Abs

def mul(b,n):
    m=1.0
    for i in range(n):
        m=m*(b-i)
    return m

def pedir_valores():
    total = 0
    xi = []
    while True:
        limpiar()
        print("Presione 'S' para pasar a ingresar los valores de fi")
        print(f"\tXi ingresados: {xi}")
        dato = castear(f"\tIngrese el valor de x{len(xi)}: ")
        if dato.upper() == "S":
            break
        else:
            try:
                xi.append(float(eval(dato)))
                total=total+1
            except:
                continue
    fi = []
    n=1
    while True:
        limpiar()
        print("Presione 'S' para terminar")
        print(f"\tXi ingresados: {xi}")
        print(f"\tFi ingresados: {fi}")
        dato = castear(f"\tIngrese el valor de f{len(fi)}: ")
        if total==n:
            fi.append(float(eval(dato)))
            break
        else:
            try:
                fi.append(float(eval(dato)))
                n=n+1
            except:
                continue
    valores = {}
    for i in range(len(xi)):
        valores[str(xi[i])] = [fi[i]]
    valores['total'] = len(xi)
    return valores
    
def NewtonDD():
    funcion=""
    punto=""
    iteracion = int(input("Ingrese el grado que desea del polinomio\n"))
    opcion=input("¿Ingresara una funcion para evaluar? 1.Si 2.No")
    if opcion=="1":
        funcion=input("Ingrese la funcion\n")
        punto=float(input("Ingrese el punto a evaluar\n"))
    datos = pedir_valores()
    limpiar()
    #crear tabla
    cabezero = ["Zk","f(Zk)"]
    for _ in range(datos["total"] -1):
        cabezero.append("")
    tabla = tablita(cabezero, show_iteracion=False)
    #cargar matriz principal
    matriz = []

    listax=[]
    for xn, fx in datos.items():
        if not xn == "total":
            listax.append(xn)
            for i in range(len(fx)):
                fila = [float(xn)]
                fila.append(fx[0])
                for _ in range(datos["total"]-1):
                    fila.append(float())
                matriz.append(fila)
    #calcular
    #j,i
    for i in range(2,iteracion+1):
        for j in range(i-1,len(matriz)):
            #print(f"({j},{i})")
            if not (matriz[j][0] - matriz[j-(i-1)][0]) == 0:
                matriz[j][i] = (matriz[j][i-1] - matriz[j-1][i-1]) / (matriz[j][0] - matriz[j-(i-1)][0])
            else:
                matriz[j][i] = datos[str(matriz[j][0])][i-1]
    
    polinomio = f"{matriz[0][1]}"
    temp = ""
    for j in range(1,len(matriz)):
        #print(f"{matriz[j][0]} {matriz[j][j+1]}")
        temp += f"*(x-{matriz[j-1][0]})"
        polinomio += f"+({matriz[j][j+1]}){temp}"
        
    x,_ = poly_from_expr(polinomio)
    
    for fila in matriz:
        tabla.add_fila(fila)
        
    print(f"{'*'*5} Resultado del polinomio de Newton {'*'*5} \n")
    tabla.print_table()
    print(f"\nPolinomio: {str(x.expr).replace('**','^')}")
    print("\n","*"*50)

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
        mayor=0.0
        for i in range(len(listax)):
            if mayor<Abs((listax[i])):
                mayor=float(listax[i])
        fderivada=derivada.subs(x,mayor)
        error=(fderivada/fac)*m
        px=float(eval(convertir_funcion(str(x.expr),var_n="punto")))
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
            px=float(eval(convertir_funcion(str(x.expr),var_n="punto")))
            print(f"Evaluacion en f({punto}):",px)