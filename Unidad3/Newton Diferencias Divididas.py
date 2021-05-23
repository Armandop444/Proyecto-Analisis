import numpy as np
import sympy as sym

# INGRESO , Datos de prueba
#xi = np.array([4, -4, 7,6,2])
#fi = np.array([278, -242, 1430, 908,40])
def InterpolacionNewtondDivididas(grado):
    cont = 0
    numero = 0
    final = grado
    final = int(final)
    xi = [""]*(final+1)
    while cont < final+1:
        mensaje = "Ingrese el valor de Xi para la posicion: {0} \n".format(cont+1)
        numero = float(input(mensaje))
        xi[cont] = numero
        cont = cont+1
    print(xi)
    cont = 0
    fi = [""]*(final+1)
    while cont < final+1:
        #print("estoy en segundo bucle con el contador en {0}".format(cont))
        mensaje = "Ingrese el valor de fi para la posicion: {0} \n".format(cont+1)
        numero = float(input(mensaje))
        fi[cont] = numero
        cont = cont+1
    print(fi)


    titulo = ['i   ', 'xi  ', 'fi  ']
    n = len(xi)
    ki = np.arange(0, n, 1)
    tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
    tabla = np.transpose(tabla)


    dfinita = np.zeros(shape=(n, n), dtype=float)
    tabla = np.concatenate((tabla, dfinita), axis=1)


    [n, m] = np.shape(tabla)
    diagonal = n-1
    j = 3
    while (j < m):

        titulo.append('F['+str(j-2)+']')

        i = 0
        paso = j-2
        while (i < diagonal):
            denominador = (xi[i+paso]-xi[i])
            numerador = tabla[i+1, j-1]-tabla[i, j-1]
            tabla[i, j] = numerador/denominador
            i = i+1
        diagonal = diagonal - 1
        j = j+1


    dDividida = tabla[0, 3:]
    n = len(dfinita)


    x = sym.Symbol('x')
    polinomio = fi[0]
    for j in range(1, n, 1):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0, j, 1):
            termino = termino*(x-xi[k])
        polinomio = polinomio + termino*factor


    polisimple = polinomio.expand()


    # SALIDA

    print('dDividida: ')
    print(dDividida)
    print('polinomio: ')
    print(polinomio)
    print('polinomio simplificado: ')
    print(polisimple)
    punto = float(input("Ingrese el punto a evaluar \n"))
    evaluar = polisimple.subs(x, punto)
    print(evaluar)
    print(tabla)

#Prueba de funcion
#InterpolacionNewtondDivididas(2)
