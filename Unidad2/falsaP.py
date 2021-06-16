from FormulaEngine import convertir_funcion, raiz
from Utilidades import tablita
from sympy import cos, sin, tan, log, ln, exp, cot, sec, csc, asin, acos, atan

#ecuacion=input("ingrese la funcion\n")
# funcion que se evaluara

#esto es del ccodigo de alejandro
#if"^"in ecuacion:
#    ecuacion=ecuacion.replace("^","**")
#aqui termina el codigo del ale

#func = parse_expr(ecuacion)# funcion que evaluaremos


# metodo de la biseccion
def FalsaP(func, x1, x2, es):
    tabla = tablita(["X1","X2","Xr","EA"])
    
    xr = 0
    ea = 100

    # incio del bucle
    while ea > es:
        
        f1 = eval(convertir_funcion(func, var_n="x1"))  # reamplazmos x por x1 y evaluamos la funcion
        f2 = eval(convertir_funcion(func, var_n="x2"))
        
        xanterior = xr
        
        xr = (x1-((f1*(x1-x2))/(f1-f2)))
        fr = eval(convertir_funcion(func, var_n="xr"))
        if xr != 0:
            ea = abs((xr - xanterior) / xr) * 100
        test = f1 * fr
        
        # agregamos valores a la fila de la iteracion
        tabla.add_fila([x1,x2,xr,ea])

        if test < 0:
            x2 = xr
        elif test > 0:
            x1 = xr
        else:
            ea = 0

    return tabla.get_tabla()

#x1=float(input("ingrese el valor de x1\n"))
#x2=float(input("ingrese el valor de x2\n"))
#a = FalsaP(func, x1, x2, 0.00001)
#print(a)