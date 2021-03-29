from FormulaEngine import *
from biseccion import *
from falsaP import *

menu="Seleccione una Unidad:\n{}\n{}\n{}\n{}\n{}\n{}".format("1-Unidad #1","2-Unidad #2","3-Unidad #3","4-Unidad #4","5-Unidad #5","cualquiera otra tecla para salir")

opcion=int(input("{}".format(menu)))
while (opcion>=1 and opcion<=5):
    tema=0
    formula=""
    if (opcion==1): #Serie de Taylor

        print("Contenido de unidad 1 que aun no hay nada xD")

    if (opcion==2):
        
        tema=int(input("\n\n\nSeleccione Tema\n{}\n{}".format("1-Bisección","2-Falsa Posición")))
        if (tema==1): #Biseccion
            x1=x2=es=bandera= 0
            formula=input("Ingrese la ecuación a evaluar: ")
            
            while bandera==0:
                formula=convertir_funcion(formula)
                if formula !="Error":
                    bandera=1
                    formula=parse_expr(formula)
                else:
                    print("\n  -------------------------------------------------------------------------\n",
                    "|La funcion no esta definida correctamente con la agrupacion de parentesis|\n",
                    " -------------------------------------------------------------------------\n")
                    formula=input("Por favor Ingrese Nuevamente la ecuación:")
            try:
                x1=float(input("Ingrese el valor de X1: "))
                x2=float(input("Ingrese el valor de X2: "))
                es=float(input("Cifras significativas: "))    
                b= Bisec(formula,x1,x2,es)
                print(b,"\n")
            except ValueError as e:
                print("Error: ",e)

        elif(tema==2): #Falsa Posicion
            print("hola")
    opcion=int(input("{}".format(menu))) #Aqui esta la pregunta del menu

