from FormulaEngine import *
from Utilidades import *

from biseccion import *
from falsaP import *
from secante import *
from PuntoFijo import *

#Metodo para sacar ES
def ess (es:float):
    banderaError=0
    valor=0
    while banderaError==0:
        if (es==1.0):
            valor=int(input("Ingrese cifras significativas: ")) 
            valor= cifras_significativas(valor)
            banderaError = 1
        if (es==2.0):
            valor=float(input("Ingrese Error de tolerancia: "))
            banderaError = 1
        elif (valor==0):
            print("\n  --------------------------------------------------------------\n",
            "|No ha seleccionado ninguna opcion por favor intente nuevamente|\n",
            " --------------------------------------------------------------\n")
            es=int(input("Seleccione como ingresara el error:\n{}\n{}".format("1-Cifras significativas","2-Error de tolerancia")))
    return valor

#texto de menu
def errorIngreso():
    print("\n  -------------------------------------------------------------------------\n",
        "|La funcion no esta definida correctamente con la agrupacion de parentesis|\n",
        " -------------------------------------------------------------------------\n")
#Menu
menu="Seleccione una Unidad:\n{}\n{}\n{}\n{}\n{}\n{}".format("1-Unidad #1","2-Unidad #2","3-Unidad #3","4-Unidad #4","5-Unidad #5","cualquiera otra tecla para salir")

opcion=int(input("{}".format(menu)))
while (opcion>=1 and opcion<=5):
    tema=0
    formula=""
    if (opcion==1): #Serie de Taylor o Unidad 1

        print("Contenido de unidad 1 que aun no hay nada xD")

    if (opcion==2): #Unidad 2
        tema=int(input("\nSeleccione Tema\n{}\n{}\n{}\n{}".format("1-Bisección","2-Falsa Posición","3-Punto Fijo","5-Secante")))
        bandera=0
        if (tema==1): #Biseccion
            x1=x2=es= 0
            formula=input("[Biseccion] Ingrese la ecuación a evaluar: ")
            
            while bandera==0:
                formula=convertir_funcion(formula)
                if formula !="Error":
                    bandera=1
                    formula=parse_expr(formula)
                else:
                    errorIngreso()
                    formula=input("[Biseccion] Por favor Ingrese Nuevamente la ecuación:")

            try:
                x1=float(input("Ingrese el valor de X1: "))
                x2=float(input("Ingrese el valor de X2: "))
                cualerror=int(input("Seleccione como ingresara el error:\n{}\n{}".format("1-Cifras significativas","2-Error de tolerancia")))
                es=ess(cualerror)
                b= Bisec(formula,x1,x2,es)
                print(b,"\n")
            except ValueError as e:
                print("Error: ",e)

        elif(tema==2): #Falsa Posicion
            formula=input("[Falsa posicion] Ingrese la ecuación a evaluar: ")

            while bandera==0:
                formula=convertir_funcion(formula)
                if formula !="Error":
                    bandera=1
                    formula=parse_expr(formula)
                else:
                    errorIngreso()
                    formula=input("[Falsa Posicion] Por favor Ingrese Nuevamente la ecuación: ")

            try:
                x1=float(input("Ingrese el valor de X1: "))
                x2=float(input("Ingrese el valor de X2: "))
                cualerror=int(input("Seleccione como ingresara el error:\n{}\n{}".format("1-Cifras significativas","2-Error de tolerancia")))
                es=ess(cualerror)
                f=FalsaP(formula,x1,x2,es)
                print(f,"\n")
            except ValueError as e:
                print("Error: ",e)

        elif(tema==3): #Punto Fijo
            formula=input("[Punto Fijo] Ingrese la ecuación a evaluar")

            while bandera==0:
                formula=convertir_funcion(formula)
                if formula !="Error":
                    bandera=1
                else:
                    errorIngreso()
                    formula=input("[Punto Fijo] Por vaor Ingrese Nuevamente la ecuación: ")

            try:
                x=float(input("Ingrese el valor de X: "))
                cualerror=int(input("Seleccione como ingresara el error:\n{}\n{}".format("1-Cifras significativas","2-Error de tolerancia")))
                es=ess(cualerror)
                PuntoFijo(formula,es,x)
            except ValueError as e:
                print("Error: ",e)

        elif(tema==5): #Secante
            formula=input("[Secante] Ingrese la ecuación a evaluar: ")

            while bandera==0:
                formula=convertir_funcion(formula)
                if formula!="Error":
                    bandera=1
                    formula=parse_expr(formula)
                else:
                    errorIngreso()
                    formula=input("[Secante] Por favor Ingrese Nuevamente la ecuación: ")
            try:
                xnmenos=float(input("Ingrese el valor de (xn-1): "))
                xn=float(input("Ingrese el valor de xn: "))
                cualerror=int(input("Seleccione como ingresara el error:\n{}\n{}".format("1-Cifras significativas","2-Error de tolerancia")))
                es=ess(cualerror)
                s=Sec(formula,xnmenos,xn,es)
                print(s,"\n")
            except ValueError as e:
                print("Error: ",e)
        else:
            print("\nOpcion no valida se le enviara al menu principal")

    opcion=int(input("{}".format(menu))) #Aqui esta la pregunta del menu