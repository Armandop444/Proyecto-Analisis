from Utilidades import limpiar, tablita
from sympy import poly_from_expr

def pedir_valores():
    total = 0
    xi = []
    while True:
        limpiar()
        print("Presione 'S' para pasar a ingresar los valores de fi")
        print(f"\tXi ingresados: {xi}")
        dato = input(f"\tIngrese el valor de x{len(xi)}: ")
        if dato.upper() == "S":
            break
        else:
            try:
                xi.append(str(float(dato)))
            except:
                continue
    fi = []
    while True:
        limpiar()
        print("Presione 'S' para terminar")
        print(f"\tXi ingresados: {xi}")
        print(f"\tXi ingresados: {fi}")
        dato = input(f"\tIngrese el valor de f{len(fi)}: ")
        if dato.upper() == "S":
            break
        else:
            try:
                fi.append(float(dato))
            except:
                continue
    valores = {}
    for i in range(len(xi)):
        valores[str(xi[i])] = [fi[i]]
    valores['total'] = len(xi)
    return valores
    
def NewtonDD():
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
    return str(x.expr) 
