from biseccion import *

menu="Seleccione una Unidad:\n{}\n{}\n{}\n{}\n{}\{}".format("1-Unidad #1","2-Unidad #2","3-Unidad #3","4-Unidad #4","5-Unidad #5","cualquiera otra tecla para salir")

opcion=int(input("{}".format(menu)))
while (opcion>=1 and opcion<=5):
    tema=0
    formula=""
    if (opcion==1):
        print("Contenido de unidad 1 que aun no hay nada xD")
    if (opcion==2):
        x1=x2=es= 0
        tema=int(input("\n\n\nSeleccione Tema\n{}".format("1-Biseccion")))
        if (tema==1):
            formula=parse_expr(input("Ingrese la ecuacion a evaluar: "))
            try:
                x1=float(input("Ingrese el valor de X1: "))
                x2=float(input("Ingrese el valor de X2: "))
                es=float(input("Cifras significativas (actualmente valor ya aplicado a la formula): "))    
                b= Bisec(formula,x1,x2,es)
                print(b,"\n")
            except ValueError as e:
                print("Me dio amsiedad: ",e)
            
    opcion=int(input("{}".format(menu))) #Aqui esta la pregunta del menu

