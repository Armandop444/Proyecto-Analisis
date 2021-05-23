import sympy as sym

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


def newton(listax, listaf):
    listaA = []
    b = 0

    iteracion = len(listax)
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
    return listaA


cont = 0
numero = 0
final = input("Ingrese el grado del polinomio \n")
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
Valores=newton(xi,fi)

variablesB =Valores

x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1,4,1):
    factor = variablesB[j]
    termino = 1
    for k in range(0,j,1):
        termino = termino*(x-xi[k])
    polinomio = polinomio + termino*factor


polisimple = polinomio.expand()




# SALIDA

print('valores de B: ')
print(variablesB)
print('polinomio: ')
print(polinomio)
print('polinomio simplificado: ' )
print(polisimple)
punto_a_evaluar=float(input("ingrese el punto a evaluar"))
evaluar=polisimple.subs(x,punto_a_evaluar)
print ("El valor aproximado de f(",punto_a_evaluar,") es: ", evaluar)


