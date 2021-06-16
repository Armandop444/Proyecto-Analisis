from sympy import *
x=Symbol("x")
#nivelderiavda es si es una derivada de primer(1) o segundo nivel(2), como la diferenciacion normal
#la diferencia es en ordenderivada, que ya no va a ser la primera derivada, sino que (2)segunda, tercera(3) o cuarta(4)
#ahora que lo pienso lo podia hacer de una vez en el codigo de DiferenciacionNumerica.py, pero iba a quedar muy cholo xd

#adelante
def diffnumsupfor(funcion,xo,h,nivelderivada,ordenderivada):
    respuesta=0.0
    error=0.0
    funcion=parse_expr(funcion)
    funcdiff=parse_expr("1")
    dfunc=diff(funcion,x)
    d2func=diff(dfunc,x)
    d3func=diff(d2func,x)
    d4func=diff(d3func,x)
    if nivelderivada==1:
        if ordenderivada==2:
            #derivadaorden2
            funcdiff=((funcion.subs(x,(xo+2*h)))-2*(funcion.subs(x,(xo+h)))+(funcion.subs(x,xo)))/(h**2)
            respuesta=funcdiff
            error=(Abs(((d2func.subs(x,xo))-float(respuesta))/(d2func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==3:
            #derivadaorden3
            funcdiff=(-(funcion.subs(x,xo))+3*(funcion.subs(x,(xo+h)))-3*(funcion.subs(x,(xo+2*h)))+(funcion.subs(x,(xo+3*h))))/(h**3)
            respuesta=funcdiff
            error=(Abs(((d3func.subs(x,xo))-float(respuesta))/(d3func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==4:
            #derivadaorden4
            funcdiff=((funcion.subs(x,(xo)))-4*(funcion.subs(x,(xo+h)))+6*(funcion.subs(x,(xo+2*h)))-4*(funcion.subs(x,(xo+3*h)))+(funcion.subs(x,(xo+4*h))))/(h**4)
            respuesta=funcdiff
            error=(Abs(((d4func.subs(x,xo))-float(respuesta))/(d4func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        else:
            print("Error en la seleccion de un orden de derivada superior (de 2 a 4)")
    elif nivelderivada==2:
        if ordenderivada==2:
            #derivadaorden2
            funcdiff=(2*(funcion.subs(x,(xo)))-5*(funcion.subs(x,(xo+h)))+4*(funcion.subs(x,(xo+2*h)))-(funcion.subs(x,(xo+3*h))))/(h**2)
            respuesta=funcdiff
            error=(Abs(((d2func.subs(x,xo))-float(respuesta))/(d2func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==3:
            #derivadaorden3
            funcdiff=(-5*(funcion.subs(x,(xo)))+18*(funcion.subs(x,(xo+h)))-24*(funcion.subs(x,(xo+2*h)))+14*(funcion.subs(x,(xo+3*h)))-3*(funcion.subs(x,(xo+4*h))))/(2*(h**3))
            respuesta=funcdiff
            error=(Abs(((d3func.subs(x,xo))-float(respuesta))/(d3func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==4:
            #derivadaorden4
            funcdiff=(-2*(funcion.subs(x,(xo+5*h)))+11*(funcion.subs(x,(xo+4*h)))-24*(funcion.subs(x,(xo+3*h)))+26*(funcion.subs(x,(xo+2*h)))-14*(funcion.subs(x,(xo+h)))+3*(funcion.subs(x,(xo))))/(h**4)
            respuesta=funcdiff
            error=(Abs(((d4func.subs(x,xo))-float(respuesta))/(d4func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        else:
            print("Error en la seleccion de un orden de derivada superior (de 2 a 4)")
    else:
        print("Error en el nivel de derivada (1 o 2)")
    return float(respuesta)

#centrales
def diffnumsupcentral(funcion,xo,h,nivelderivada,ordenderivada):
    respuesta=0.0
    error=0.0
    funcion=parse_expr(funcion)
    funcdiff=parse_expr("1")
    dfunc=diff(funcion,x)
    d2func=diff(dfunc,x)
    d3func=diff(d2func,x)
    d4func=diff(d3func,x)
    if nivelderivada==1:
        if ordenderivada==2:
            funcdiff=((funcion.subs(x,(xo-h)))-2*(funcion.subs(x,(xo)))+(funcion.subs(x,(xo+h))))/(h**2)
            respuesta=funcdiff
            error=(Abs(((d2func.subs(x,xo))-float(respuesta))/(d2func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
            #derivadaorden2
        elif ordenderivada==3:
            #derivadaorden3
            funcdiff=(-(funcion.subs(x,(xo-2*h)))+2*(funcion.subs(x,(xo-h)))-2*(funcion.subs(x,(xo+h)))+(funcion.subs(x,(xo+2*h))))/(2*(h**3))
            respuesta=funcdiff
            error=(Abs(((d3func.subs(x,xo))-float(respuesta))/(d3func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==4:
            #derivadaorden4
            funcdiff=((funcion.subs(x,(xo+2*h)))-4*(funcion.subs(x,(xo+h)))+6*(funcion.subs(x,(xo)))-4*(funcion.subs(x,(xo-h)))+(funcion.subs(x,(xo-2*h))))/(h**4)
            respuesta=funcdiff
            error=(Abs(((d4func.subs(x,xo))-float(respuesta))/(d4func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        else:
            print("Error en la seleccion de un orden de derivada superior (de 2 a 4)")
    elif nivelderivada==2:
        if ordenderivada==2:
            #derivadaorden2
            funcdiff=(-(funcion.subs(x,(xo-2*h)))+16*(funcion.subs(x,(xo-h)))-30*(funcion.subs(x,(xo)))+16*(funcion.subs(x,(xo+h)))-(funcion.subs(x,(xo+2*h))))/(12*(h**2))
            respuesta=funcdiff
            error=(Abs(((d2func.subs(x,xo))-float(respuesta))/(d2func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==3:
            #derivadaorden3
            funcdiff=((funcion.subs(x,(xo-3*h)))-8*(funcion.subs(x,(xo-2*h)))+13*(funcion.subs(x,(xo-h)))-13*(funcion.subs(x,(xo+h)))+8*(funcion.subs(x,(xo+2*h)))-(funcion.subs(x,(xo+3*h))))/(8*(h**3))
            respuesta=funcdiff
            error=(Abs(((d3func.subs(x,xo))-float(respuesta))/(d3func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==4:
            #derivadaorden4
            funcdiff=(-(funcion.subs(x,(xo+3*h)))+12*(funcion.subs(x,(xo+2*h)))-39*(funcion.subs(x,(xo+h)))+56*(funcion.subs(x,(xo)))-39*(funcion.subs(x,(xo-h)))+12*(funcion.subs(x,(xo-2*h)))-(funcion.subs(x,(xo-3*h))))/(6*(h**4))
            respuesta=funcdiff
            error=(Abs(((d4func.subs(x,xo))-float(respuesta))/(d4func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        else:
            print("Error en la seleccion de un orden de derivada superior (de 2 a 4)")
    else:
        print("Error en el nivel de derivada (1 o 2)")
    return float(respuesta)

#atras
def diffnumsupback(funcion,xo,h,nivelderivada,ordenderivada):
    respuesta=0.0
    error=0.0
    funcion=parse_expr(funcion)
    funcdiff=parse_expr("1")
    dfunc=diff(funcion,x)
    d2func=diff(dfunc,x)
    d3func=diff(d2func,x)
    d4func=diff(d3func,x)
    if nivelderivada==1:
        if ordenderivada==2:
            #derivadaorden2
            funcdiff=((funcion.subs(x,(xo-2*h)))-2*(funcion.subs(x,(xo-h)))+(funcion.subs(x,(xo))))/(h**2)
            respuesta=funcdiff
            error=(Abs(((d2func.subs(x,xo))-float(respuesta))/(d2func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==3:
            #derivadaorden3
            funcdiff=((funcion.subs(x,(xo)))-3*(funcion.subs(x,(xo-h)))+3*(funcion.subs(x,(xo-2*h)))-(funcion.subs(x,(xo-3*h))))/(h**3)
            respuesta=funcdiff
            error=(Abs(((d3func.subs(x,xo))-float(respuesta))/(d3func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==4:
            #derivadaorden4
            funcdiff=((funcion.subs(x,(xo)))-4*(funcion.subs(x,(xo-h)))+6*(funcion.subs(x,(xo-2*h)))-4*(funcion.subs(x,(xo-3*h)))+(funcion.subs(x,(xo-4*h))))/(h**4)
            respuesta=funcdiff
            error=(Abs(((d4func.subs(x,xo))-float(respuesta))/(d4func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        else:
            print("Error en la seleccion de un orden de derivada superior (de 2 a 4)")
    elif nivelderivada==2:
        if ordenderivada==2:
            #derivadaorden2
            funcdiff=(2*(funcion.subs(x,(xo)))-5*(funcion.subs(x,(xo-h)))+4*(funcion.subs(x,(xo-2*h)))-(funcion.subs(x,(xo-3*h))))/(h**2)
            respuesta=funcdiff
            error=(Abs(((d2func.subs(x,xo))-float(respuesta))/(d2func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==3:
            #derivadaorden3
            funcdiff=(5*(funcion.subs(x,(xo)))-18*(funcion.subs(x,(xo-h)))+24*(funcion.subs(x,(xo-2*h)))-14*(funcion.subs(x,(xo-3*h)))+3*(funcion.subs(x,(xo-4*h))))/(2*(h**3))
            respuesta=funcdiff
            error=(Abs(((d3func.subs(x,xo))-float(respuesta))/(d3func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        elif ordenderivada==4:
            #derivadaorden4
            funcdiff=(3*(funcion.subs(x,(xo)))-14*(funcion.subs(x,(xo-h)))+26*(funcion.subs(x,(xo-2*h)))-24*(funcion.subs(x,(xo-3*h)))+11*(funcion.subs(x,(xo-4*h)))-2*(funcion.subs(x,(xo-5*h))))/(h**4)
            respuesta=funcdiff
            error=(Abs(((d4func.subs(x,xo))-float(respuesta))/(d4func.subs(x,xo))))*100
            error=float(error)
            print("El error de la respuesta es: {0}%".format(error))
            print()
            print("La respuesta es:")
            print(respuesta)
        else:
            print("Error en la seleccion de un orden de derivada superior (de 2 a 4)")
    else:
        print("Error en el nivel de derivada (1 o 2)")
    return float(respuesta)

#fx="cos(x)"
#uwu=diffnumsupcentral(fx,2,0.1,1,4)
#print(uwu)