class ParentesisError(Exception):
    pass

class MathError(Exception):
    pass

def raiz(radicando, indice):
    if indice < 1:
        raise MathError("Solo indices enteros mayor que 1")
    else:
        if indice%2 == 1:
            if radicando < 0:
                return -1 * (abs(radicando) ** (1/indice))
            else:
                return radicando ** (1/indice)
        else:
            if radicando < 0:
                raise MathError("Radicando negativo")
            else:
                return radicando ** (1/indice)

def cifras_significativas(n: int):
    return 0.5*10**(2-n)
