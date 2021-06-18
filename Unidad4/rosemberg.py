from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan
from sympy import symbols, parse_expr
from FormulaEngine import convertir_funcion,castear,raiz,comprobarpunto
from Utilidades import limpiar

def Rosemberg():
    # pedir datos
    try:
        x = symbols("x")
        funcion = input("Ingrese la funcion ")
        funcion = parse_expr(convertir_funcion(funcion))
        nivel = int(input("Ingrese el nivel "))
        lim_inf =comprobarpunto(input("Ingrese el limite inferior "))

        lim_sup = comprobarpunto(input("Ingrese el limite superior "))
    except Exception as error:
        print("No has introducio correctamente los datos, vuelve a intentar")
        print(error)

    # generar los valores hn
    hn = [
        [lim_inf, lim_sup]
    ]
    suc = 1
    for i in range(2, nivel+1):
        hsn = []
        cual = 0
        for j in range(1, 1 + suc + len(hn[i-2])):
            if j % 2 == 0:
                # se calcula el punto medio
                v1 = hn[i-2][cual-1]
                v2 = hn[i-2][cual]
                valor = (v1 + v2) / 2
                hsn.append(valor)
            else:
                hsn.append(hn[i-2][cual])
                cual += 1
        hn.append(hsn)
        suc = suc * 2 # este se usa para calcular la cantidad elementos del siguiente fila

    # se calcula el nivel 1
    niveles = []
    valor = 0
    n = 2
    subnivel = []
    for i in hn:
        if len(i) == 2:
            xa = lim_inf
            fls = funcion.subs(x,xa)
            xa = lim_sup
            fli = funcion.subs(x,xa)
            valor = fls + fli
            subnivel.append(((lim_sup-lim_inf)/2) * (fls + fli))
        else:
            i.pop(0)
            i.pop(len(i)-1)
            suma = 0
            for xa in i:
                suma += funcion.subs(x,xa)
            suma = suma * 2
            suma = suma + valor
            suma = suma * ((lim_sup-lim_inf)/2**n)
            n += 1
            subnivel.append(suma)
    niveles.append(subnivel)
    
    #generar el resto de niveles 
    for i in range(1, nivel):
        subnivel = []
        for j in range(len(niveles[i-1]) - 1):
            multi = 4**(i)
            p1 = niveles[i-1][j]
            p2 = niveles[i-1][j+1]
            div = 4**(i) -1
            suma = ((multi * p2) / div) - ((p1) / div)
            subnivel.append(suma)
        niveles.append(subnivel)
    
    limpiar()
    print(f"{'*' * 10} Resultados { '*' * 10}")
    for i in range(1,nivel + 1 ):
        print(f"Nivel {i}")
        for j in niveles[i-1]:
            print(f"\t{j}")
    print("*"*35)
