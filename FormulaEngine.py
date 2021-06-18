import re

class MathError(Exception):
    pass


class ValueError(Exception):
    pass

def castear(mensaje = ""):
    valor = input(mensaje + " ")
    return convertir_funcion(valor)

def separarRaiz(valor):
    valor = valor.lower()
    parentesisA = 0
    bandera = 0
    salida = ""
    cuantasRaices = valor.count("raiz")
    inicioBuscar = 0
    if cuantasRaices > 0:
        while cuantasRaices > 0:
            if inicioBuscar == 0:
                posicion = valor.find("raiz")+4
                posicionInicio = valor.find("raiz")
            else:
                posicion = valor.find("raiz", inicioBuscar)+4
                posicionInicio = valor.find("raiz", inicioBuscar)
            while bandera == 0:

                if valor[posicion] == "(":
                    parentesisA = parentesisA+1
                elif valor[posicion] == ")":
                    parentesisA = parentesisA-1

                if parentesisA == 0:
                    salida = salida + \
                        valor[inicioBuscar:posicionInicio]+" " + \
                        valor[posicionInicio:(posicion+1)]+" "
                    bandera = 1
                    inicioBuscar = posicion+1

                posicion = posicion+1
            cuantasRaices = cuantasRaices-1
            bandera = 0
        return salida
    else:
        return valor


def unirRaiz(original, convertido=[]):
    parentesis = 0
    bandera = 0
    salida = ""
    cuantasRaices = original.count("raiz")
    inicioBuscar = 0
    posicionConvertido = 0
    while cuantasRaices > 0:
        if inicioBuscar == 0:
            posicion = original.find("raiz")+4
            posicionInicio = original.find("raiz")
        else:
            posicion = original.find("raiz", inicioBuscar)+4
            posicionInicio = original.find("raiz", inicioBuscar)
        while bandera == 0:

            if original[posicion] == "(":
                parentesis = parentesis+1
            elif original[posicion] == ")":
                parentesis = parentesis-1

            if parentesis == 0:
                if inicioBuscar == posicionInicio and original.count("raiz") <= 1:
                    salida = salida + \
                        convertido[posicionConvertido]+original[(posicion+1):]
                else:
                    salida = salida + \
                        original[inicioBuscar:posicionInicio] + \
                        convertido[posicionConvertido]
                bandera = 1
                if  bandera==1 and original.count("raiz") <= 1:
                    salida = salida + \
                            original[(posicion+1):]
                
                inicioBuscar = posicion+1
                posicionConvertido = posicionConvertido+1
                
            posicion = posicion+1
        cuantasRaices = cuantasRaices-1
        falta=0
        for i in range(len(salida)):
            if salida[i]=="(":
                falta+=1
            elif salida[i]==")":
                falta-=1
        if bandera==1 and original.count("raiz") > 1 and cuantasRaices==0 and falta!=0:
                    salida = salida + ")"
        bandera = 0
    return salida


def raiz(radicando):
    separado = separarRaiz(radicando)
    lista = re.findall(r"raiz(\([\w,\(\^)+*\/-]+\))", separado)
    cuantosDatos = len(lista)
    if cuantosDatos > 0:
        listaConvertida = []
        for i in range(cuantosDatos):
            dato = lista[i]
            if dato.count(",") == 1:
                separarIndice = dato.split(",")

                conversion = separarIndice[0]+")"
                indice = separarIndice[1]

                for k in range(len(indice)):
                    if indice[k] != ")":
                        if indice[k].isdigit() == True:
                            conversion = conversion+"^(1/"+indice[k]+")"
                        elif (indice[k] == "+" or indice[k] == "-" or indice[k] == "/" or indice[k] == "*") and k == (len(indice)-1):
                            conversion = conversion+indice[k]
                        else:
                            raise MathError(
                                f"Error en funcion raiz({dato}) Solo indices naturales mayor o igual a 1")
                listaConvertida.append(conversion)
            elif dato.count(",") >= 1:
                raise MathError(
                    f"Error en funcion raiz({dato}) Solo indices naturales mayor o igual a 1")
            else:
                for k in range(len(dato)):
                    conversion = dato+"^(1/2)"
                listaConvertida.append(conversion)

        salida = unirRaiz(radicando, listaConvertida)
        return salida
    else:
        return radicando

def validar_parentesis(funcion: str):
    if funcion.count("(") == funcion.count(")"):
        return True
    else:
        return False
    
def convertir_funcion(formula: str, var_o = "x", var_n = "x", graficar = False):
    if validar_parentesis(formula):
        #Cambiamos la variable original por la que se va a evaluar
        formula = formula.replace(var_o, var_n)

        #ver si hay raiz y convertila a lenguaje entendible
        if "raiz" in formula:
            formula = raiz(formula)
        
        #Convertir funciones trigonometricas
        if "sen" in formula:
            formula = formula.replace("sen", "sin")
        if "asen" in formula:
            if graficar:
                formula = formula.replace("asen", "asin")
            else:
                formula = formula.replace("asen", "arcsin")
        if "acos" in formula:
            if not graficar:
                formula = formula.replace("acos", "arcsin")
        if "atan" in formula:
            if not graficar:
                formula = formula.replace("atan", "arctan")
        #convertir potencias
        if "e^" in formula:
            formula = formula.replace("e^", "exp")
        if "^" in formula:
            formula = formula.replace("^", "**")
        
        if "pi" in formula:
            formula = formula.replace("pi","3.141592")

        if graficar:
            formula = formula.replace("ln", "log")
        
        return formula
    else:
        return "Error"

def reconvertir_funcion(formula: str):
    if validar_parentesis(formula):            
        #convertir potencias
        if "exp" in formula:
            formula = formula.replace("exp", "e^")
        if "**" in formula:
            formula = formula.replace("**", "^")
        
        return formula
    else:
        return "Error"