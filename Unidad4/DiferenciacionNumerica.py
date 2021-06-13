from sympy import *
from Utilidades import limpiar
#si desean meter una tabla, pueden interpolar la tabla con un metodo como por ejemplo, lagrange, y la funcion resultante ponerla aqui, si jala xd
#aunque el error depende del grado de la funcion, seguro 

def pedirValores(f,max):
    lista=[]
    total=1
    while True:
        limpiar()
        if max=="":
            print("Presione S para terminar de ingresar los datos en la lista")
        print("Valores \n",lista)
        dato= input(f"Ingrese el valor de {f}({len(lista)}): ")
        if dato.upper()=="S" or (max==total and max!=""):
            if dato.upper()!="S":
                lista.append(float(dato))
            return lista
        else:
            try:
                lista.append(float(dato))
                total+=1
            except:
                continue


x=Symbol("x")
def diffforwardfunc(funcion, xo, h, nivelderivada,shoutput=True):
    #añadir convertir funciones
    error=0.0
    funcion=parse_expr(funcion)
    funcdiff=parse_expr("1")
    dfunc=diff(funcion,x)
    respuesta=0
    if nivelderivada==1:
        funcdiff=((funcion.subs(x,(xo+h)))-(funcion.subs(x,(xo))))/(h)
        respuesta=funcdiff
        error=(Abs(((dfunc.subs(x,xo))-float(respuesta))/(dfunc.subs(x,xo))))*100
        if shoutput==True:
            print("el error de la respuesta es: {0}%".format(error))
            print()
            print("la respuesta es:")
            print(respuesta)
    elif nivelderivada==2:
        funcdiff=(-(funcion.subs(x,(xo+2*h)))+4*(funcion.subs(x,(xo+h)))-3*(funcion.subs(x,xo)))/(2*h)
        respuesta=funcdiff
        error=(Abs(((dfunc.subs(x,xo))-float(respuesta))/(dfunc.subs(x,xo))))*100
        if shoutput==True:
            print("el error de la respuesta es: {0}%".format(error))
            print()
            print("la respuesta es:")
            print(respuesta)
    else:
        print("error en la seleccion de nivel de derivada")
    return float(respuesta)

def diffbackwardfunc(funcion,xo,h,nivelderivada,shoutput=True):
    #añadir convertir funciones
    respuesta=0
    error=0.0
    funcion=parse_expr(funcion)
    funcdiff=parse_expr("1")
    dfunc=diff(funcion,x)
    if nivelderivada==1:
        funcdiff=(-(funcion.subs(x,(xo-h)))+(funcion.subs(x,(xo))))/(h)
        respuesta=funcdiff
        error=(Abs(((dfunc.subs(x,xo))-float(respuesta))/(dfunc.subs(x,xo))))*100
        if shoutput==True:
            print("el error de la respuesta es: {0}%".format(error))
            print()
            print("la respuesta es:")
            print(respuesta)
    elif nivelderivada==2:
        funcdiff=((funcion.subs(x,(xo-2*h)))-4*(funcion.subs(x,(xo-h)))+3*(funcion.subs(x,xo)))/(2*h)
        respuesta=funcdiff
        error=(Abs(((dfunc.subs(x,xo))-float(respuesta))/(dfunc.subs(x,xo))))*100
        if shoutput==True:
            print("el error de la respuesta es: {0}%".format(error))
            print()
            print("la respuesta es:")
            print(respuesta)
    else:
        print("error en la seleccion de nivel de derivada")
    return float(respuesta)


#opcionmetodo
#1=centradasegundoorden
#2=centradacuartoorden
#3=3puntos
#4=5puntos
def diffcentralfunc(funcion,xo,h,opcionmetodo,shoutput=True):
    #añadir convertir funciones
    respuesta=0
    error=0.0
    funcion=parse_expr(funcion)
    dfunc=diff(funcion,x)
    funcdiff=parse_expr("1")
    if opcionmetodo==1:
        #centrado segundo orden
        funcdiff=((funcion.subs(x,(xo+h)))-(funcion.subs(x,(xo-h))))/(2*h)
        respuesta=funcdiff
        error=(Abs(((dfunc.subs(x,xo))-float(respuesta))/(dfunc.subs(x,xo))))*100
        error=float(error)
        if shoutput==True:
            print("el error de la respuesta es: {0}%".format(error))
            print()
            print("la respuesta es:")
            print(respuesta)
    elif opcionmetodo==2:
        #codigo orden 4
        funcdiff=(-(funcion.subs(x,(xo+2*h)))+8*(funcion.subs(x,(xo+h)))-8*(funcion.subs(x,(xo-h)))+(funcion.subs(x,(xo-2*h))))/(12*h)
        respuesta=funcdiff
        error=(Abs(((dfunc.subs(x,xo))-float(respuesta))/(dfunc.subs(x,xo))))*100
        error=float(error)
        if shoutput==True:
            print("el error de la respuesta es: {0}%".format(error))
            print()
            print("la respuesta es:")
            print(respuesta)
    elif opcionmetodo==3:
        #codigo3puntos
        error1=0.0
        error2=0.0
        funcdiff1=parse_expr("1")
        funcdiff2=parse_expr("1")
        funcdiff1=((funcion.subs(x,(xo+h)))-(funcion.subs(x,(xo-h))))/(2*h)
        error1=(Abs(((dfunc.subs(x,xo))-float(funcdiff1))/(dfunc.subs(x,xo))))*100
        funcdiff2=(-(funcion.subs(x,(xo+2*h)))+4*(funcion.subs(x,(xo+h)))-3*(funcion.subs(x,xo)))/(2*h)
        error2=(Abs(((dfunc.subs(x,xo))-float(funcdiff2))/(dfunc.subs(x,xo))))*100
        error1=float(error1)
        error2=float(error2)
        if error1>error2:
            respuesta=funcdiff2
            if shoutput==True:
                print("la mejor aproximacion con error: {0}% es:".format(error2))
                print(respuesta)
        elif error2>error1:
            respuesta=funcdiff1
            if shoutput==True:
                print("la mejor aproximacion con error {0}% es: ".format(error1))
                print(respuesta)
        else:
            respuesta=funcdiff1
            if shoutput==True:
                print("la mejor aproximacion con error {0}% es: ".format(error1))
                print(respuesta)
    elif opcionmetodo==4:
        #codigo5puntos
        contador=0
        valor1=0.0
        posicionenlista=0
        errorlista=[]
        valoreslista=[]
        funcdiff1=(1/(12*h))*(-25*(funcion.subs(x,xo))+48*(funcion.subs(x,(xo+h)))-36*(funcion.subs(x,(xo+2*h)))+16*(funcion.subs(x,(xo+3*h)))-3*(funcion.subs(x,(xo+4*h))))
        valoreslista.append(float(funcdiff1))
        funcdiff1=(1/(12*h))*(-3*(funcion.subs(x,(xo-h)))-10*(funcion.subs(x,xo))+18*(funcion.subs(x,(xo+h)))-6*(funcion.subs(x,(xo+2*h)))+(funcion.subs(x,(xo+3*h))))
        valoreslista.append(float(funcdiff1))
        funcdiff1=(1/(12*h))*((funcion.subs(x,(xo-2*h)))-8*(funcion.subs(x,(xo-h)))+8*(funcion.subs(x,(xo+h)))-(funcion.subs(x,(xo+2*h))))
        valoreslista.append(float(funcdiff1))
        funcdiff1=(1/(12*h))*(4*(funcion.subs(x,(xo-3*h)))+6*(funcion.subs(x,(xo-2*h)))-8*(funcion.subs(x,(xo-h)))+34*(funcion.subs(x,xo))+3*(funcion.subs(x,(xo+h)))+34*(funcion.subs(x,(xo+2*h))))
        valoreslista.append(float(funcdiff1))
        funcdiff1=(1/(12*h))*((funcion.subs(x,(xo-4*h)))-3*(funcion.subs(x,(xo-3*h)))+4*(funcion.subs(x,(xo-2*h)))-36*(funcion.subs(x,(xo-h)))+25*(funcion.subs(x,xo)))
        valoreslista.append(float(funcdiff1))
        for i in range(5):
            error=0.0
            error=(Abs(((dfunc.subs(x,xo))-float(valoreslista[i]))/(dfunc.subs(x,xo))))*100
            errorlista.append(float(error))
            contador=contador+1
        contador=0
        for i in range(5):
            if i==0:
                valor1=errorlista[i]
            else:
                if errorlista[i]<valor1:
                    valor1=errorlista[i]
                    posicionenlista=i
            contador=contador+1

        respuesta=valoreslista[posicionenlista]
        if shoutput==True:
            print(valoreslista)
            print(errorlista)
            print("el valor con mejor aproximacion (error: {0}%) es:".format(valor1))
            print(respuesta)
        
    else:
        print("error en opcion de metodo")
    return float(respuesta)




funcion="-0.0474999999994452*x**4 + 91.346625000011*x**3 - 272.858983333339*x**2 + 287.144158749992*x - 97.4646539166665 "
xo=1.3
h=0.1
uwu=diffcentralfunc(funcion,xo,h,1,True)
print(uwu)

