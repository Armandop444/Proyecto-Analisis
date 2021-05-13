
import math
import cmath
import numpy as np
import sys
from Utilidades import tablita


def cuadratica(r, s):  # hallar 2 raices en grados mayores a 2
    discrim = math.pow(r, 2) + (4 * s)
    raices = []
    if discrim > 0:  # raiz real
        raices.append((r + math.sqrt(discrim)) / (2))
        raices.append((r - math.sqrt(discrim)) / (2))
    else:  # raiz compleja
        raices.append((r - cmath.sqrt(discrim)) / 2)
        raices.append((r + cmath.sqrt(discrim)) / 2)
    return raices


def cuadratica2(a, b, c):  # hallar últimas 2 raices
    discrim = math.pow(b, 2) - (4 * a * c)
    raices = []
    if discrim > 0:  # raiz real
        raices.append((-b + math.sqrt(discrim)) / (2 * a))
        raices.append((-b - math.sqrt(discrim)) / (2 * a))
    else:  # raiz compleja
        raices.append((-b - cmath.sqrt(discrim)) / (2 * a))
        raices.append((-b + cmath.sqrt(discrim)) / (2 * a))
    return raices


def generateb(a, r, s):  # implementacion de relación de concurrencia para hallar residuos de división sintética
    b = []
    b.append(a[0])
    b.append(a[1] + (r * b[-1]))
    for i in a[2:]:
        b.append(i + (r * b[-1]) + (s * b[-2]))
    return b


def generatec(b, r, s):  # implementacion de relación de concurrencia para hallar derivadas parciales
    c = []
    c.append(b[0])
    c.append(b[1] + (r * c[-1]))
    for i in b[2:-1]:
        c.append(i + (r * c[-1]) + (s * c[-2]))
    return c


def bairstow(r, s, a, errorA):
    tabla = tablita(["r", "s", "EA-R","EA-S","RAIZ-R","RAIZ-S"])
    tablaD = tablita(["Formula Cuadratica"])
    grado = len(a) - 1
    noIter = 1
    listaRaices = []
    b = []
    i=0
    while grado > 0:
        noIter = 0
        rerror = 100
        serror = 100
        if grado == 1:

            if len(b) != 0:
                listaRaices.append(-b[1] / b[0])
                tablaD.add_fila([str(listaRaices[i])])
            else:
                listaRaices.extend(cuadratica2(a[0], a[1], a[2]))
                tablaD.add_fila([str(listaRaices[i])])
            grado -= 1
            i+=1
        elif grado == 2:

            if len(b) != 0:
                listaRaices.extend(cuadratica2(b[0], b[1], b[2]))
                tablaD.add_fila([str(listaRaices[i])])
                tablaD.add_fila([str(listaRaices[i+1])])
            else:
                listaRaices.extend(cuadratica2(a[0], a[1], a[2]))
                tablaD.add_fila([str(listaRaices[i])])
                tablaD.add_fila([str(listaRaices[i+1])])
            grado -= 2
            i+=2
        else:

            while rerror > errorA or serror > errorA:
                b = generateb(a, r, s)  # b4, b3, b2, b1, b0 ...
                c = generatec(b, r, s)  # c4, c3, c2, c1
                eq1 = np.array([[c[-2], c[-3]], [c[-1], c[-2]]])
                eq2 = np.array([-b[-2], -b[-1]])
                solEq = np.linalg.solve(eq1, eq2)  # resolver sistema de ecuaciones usando matrices
                rdelta = solEq[0]
                sdelta = solEq[1]
                r += rdelta 
                s += sdelta 
                rerror = abs(rdelta / r) * 100  # calcula errores relativos de r y s añadir a tablita
                serror = abs(sdelta / s) * 100  #añadir a tablita
                noIter += 1

            listaRaices.extend(cuadratica(r, s))
            i=i+2
            tabla.add_fila([r,s,rerror,serror,str(listaRaices[i-2]),str(listaRaices[i-1])])
            
            a = b[:-2]
            grado -= 2
    salida=tabla.get_tabla()+"\n\n"+tablaD.get_tabla()
    
    return salida


"""def main(argv):
    r = float(input('ingrese un valor para R: '))
    s = float(input('Ingrese un valor para S: '))
    errorA = float(input('cifras significativas: '))
    grado = int(input('Ingrese el grado del polinomio al cual desea calcularle las raices: '))
    a = []
    print('A continuación por favor ingrese los coeficientes de los términos del polinomio de mayor a menor grado:')
    coef = range(0, grado + 1)

    for i in coef:
        a.append(float(input('Coeficiente x' + str(i) + ': ')))

    cont = 1
    raices = bairstow(r, s, a, math.pow(10, -errorA))
    print("\n")

    print('---------------Raices---------------------')

    #for i in raices:
    #    print('Raíz no.' + str(cont) + ' : ' + str(i))
    #    cont += 1
    print(raices)


if __name__ == "__main__":
    main(sys.argv)"""