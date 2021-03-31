class ParentesisError(Exception):
    pass

def raiz(radicando, indice):
    return radicando**(1/indice)

def cifras_significativas(n: int):
    return 0.5*10**(2-n)