class ParentesisError(Exception):
    pass

def raiz(radicando, indice):
    if radicando <= 0:
        return -1 * (abs(radicando) ** (1/indice))
    else:
        return radicando ** (1/indice)

def cifras_significativas(n: int):
    return 0.5*10**(2-n)
