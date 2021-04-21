def validar_parentesis(funcion: str):
    if funcion.count("(") == funcion.count(")"):
        return True
    else:
        return False
    
def convertir_funcion(formula: str, var_o = "x", var_n = "x"):
    if validar_parentesis(formula):
        #Cambiamos la variable original por la que se va a evaluar
        formula = formula.replace(var_o, var_n)
        
        #Convertir funciones trigonometricas
        if "sen" in formula:
            formula = formula.replace("sen", "sin")
        if "asen" in formula:
            formula = formula.replace("asen", "asin")
            
        #convertir potencias
        if "e^" in formula:
            formula = formula.replace("e^", "exp")
        if "^" in formula:
            formula = formula.replace("^", "**")
            
        return formula
    else:
        return "Error"