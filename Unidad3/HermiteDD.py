import sympy as sp
from Utilidades import tablita

#x=sp.Symbol(x)

def hermiteDD(n):
    listalista=[]
    nmas1=n+1
    avancehorizontal=1
    # for i in range(n):
    #     xn=float(input("ingrese el valor n {0} de xn".format(i)))
    #     a=float(input("ingrese el valor de n {0} para fx".format(i)))
    #     lista=[]
    #     lista.append(i)
    #     lista.append(xn)
    #     lista.append(a)
    #     listalista.append(lista)
    # for i in range(1,n,2):
    #     dxn=float(input("ingrese el valor de {0} para dfx: ".format(listalista[i][0])))
    #     lista=listalista[i]
    #     lista.append(dxn)
    #     listalista[i]=lista
    # for i in range(2,n,2):
    #     dfxn=((listalista[i][2])-(listalista[i-1][2]))/((listalista[i][1])-(listalista[i-1][1]))
    #     lista=listalista[i]
    #     lista.append(dfxn)
    #     listalista[i]=lista
    # z=2
    # for i in range(4,(nmas1+1),1):
    #     for j in range(z,n,1):
    #         h=((listalista[j][i-1])-(listalista[j-1][i-1]))/((listalista[j][1])-(listalista[j-2][1]))
    #         lista=listalista[j]
    #         lista.append(h)
    #         listalista[j]=lista
    #     z=z+1
    xdatos=int(input("ingrese la cantidad de puntos (x0, x1, xn)"))

    for i in range(0,xdatos,1):
        xn=float(input())

    for i in range(0,n,1):
        print(listalista[i])
    polinomio=""
    

    


n=int(input("inserte el valor de n: "))
uwu=hermiteDD(n)
print(uwu)















