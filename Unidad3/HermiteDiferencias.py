from Utilidades import limpiar, tablita
from sympy import poly_from_expr,cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
from FormulaEngine import castear
'''
pedir los valores por fila
|   x |   y |   y' |
|-----|-----|------|
|  -2 | -12 |   22 |
|   1 |   9 |   10 |
'''
def pedir_valores():
    valores = {}
    n = 0
    total_datos = 0
    while True:
        limpiar()
        print("Presione 'T' para terminar de ingresar valores")
        xn = castear(f"\t Ingrese el valor de X{n} ")
        fila = []
        if xn.upper() == "T":
            valores["total"] = total_datos
            return valores
        else:
            xn = float(eval(xn))
            d = 0
            while True:
                limpiar()
                
                print("Presione 'T' para terminar de ingresar valores")
                print("Presione 'S' para terminar de ingresar datos de la fila")
                valor = castear(f"\t Ingrese el valor de f(X{n}) " if d == 0 else f"\t Ingrese el valor de la {d}ª derivada para X{n} ")
                if valor.upper() == "T":
                    valores[str(xn)]=fila
                    valores["total"] = total_datos
                    return valores
                elif valor.upper() == "S":
                    n += 1
                    valores[str(xn)]=fila
                    break
                else:
                    fila.append(float(eval(valor)))
                    total_datos += 1
                    d += 1

def HermiteD():
    #cargar datos
    datos = pedir_valores()
    
    #crear tabla
    cabezero = ["Zk","f(Zk)"]
    for _ in range(datos["total"] -1):
        cabezero.append("")
    tabla = tablita(cabezero, show_iteracion=False)
    
    #cargar matriz principal
    matriz = []
    for xn, fx in datos.items():
        if not xn == "total":
            for i in range(len(fx)):
                fila = [float(xn)]
                fila.append(fx[0])
                for _ in range(datos["total"]-1):
                    fila.append(float())
                matriz.append(fila)
    
    #calcular
    #j,i
    for i in range(2,datos["total"]+1):
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
        
    print(f"{'*'*5} Resultado del polinomio de Hermite {'*'*5} \n")
    tabla.print_table()
    print(f"\nPolinomio: {str(x.expr).replace('**','^')}")
    print("\n","*"*50)