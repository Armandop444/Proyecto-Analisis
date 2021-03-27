def raiz(radicando, indice):
    return radicando**(1/indice)

def parentesis_iguales(formula: str):
    if formula.count("(") == formula.count(")"):
        return True
    else:
        return False


def convertir_funcion(formula: str):
    if parentesis_iguales(formula):
        #convertir funciones trigonometricas
        if "sen" in formula:
            formula = formula.replace("sen", "np.sin")
        if "cos" in formula:
            formula = formula.replace("cos", "np.cos")
        if "tan" in formula:
            formula = formula.replace("tan", "np.tan")
        if "cot" in formula:
            formula = formula.replace("cot", "1/np.tan")
        if "sec" in formula:
            formula = formula.replace("sec", "1/np.cos")
        if "csc" in formula:
            formula = formula.replace("sec", "1/np.sin")
        
        #convertir logaritmos    
        if "ln" in formula:
            formula = formula.replace("ln", "np.log")
                
        #convertir potencias
        if "e^" in formula:
            formula = formula.replace("e^", "np.exp")
        if "^" in formula:
            formula = formula.replace("^", "**")
        
        #reemplazar las variables por los parametros ejemp: e^(x) -> e**(r)
        return formula
    else:
        raise NameError("La funcion no esta definida correctamente la agrupacion")
