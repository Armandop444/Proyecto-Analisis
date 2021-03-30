def raiz(radicando, indice):
    return radicando**(1/indice)

def parentesis_iguales(formula: str):
    if formula.count("(") == formula.count(")"):
        return True
    else:
        return False

def cifras(c: float):
    c=0.5*(10**(2-c))
    return c

def convertir_funcion(formula: str):
    if parentesis_iguales(formula):
        #convertir funciones trigonometricas
        if "sen" in formula:
            formula = formula.replace("sen", "sin")
        if "cos" in formula:
            formula = formula.replace("cos", "cos")
        if "tan" in formula:
            formula = formula.replace("tan", "tan")
        if "cot" in formula:
            formula = formula.replace("cot", "1/tan")
        if "sec" in formula:
            formula = formula.replace("sec", "1/cos")
        if "csc" in formula:
            formula = formula.replace("sec", "1/sin")
        
        #convertir logaritmos    
        if "ln" in formula:
            formula = formula.replace("ln", "ln")
        if "log" in formula:
            formula = formula.replace("log", "log")

        #convertir potencias
        if "e^" in formula:
            formula = formula.replace("e^", "exp")
        if "^" in formula:
            formula = formula.replace("^", "**")
        
        #reemplazar las variables por los parametros ejemp: e^(x) -> e**(r)
        return formula
    else:
        return "Error"
