from tabulate import tabulate

class tablita:
    def __init__(self, cabeceros):
        self.contenido = []
        cabeceros.insert(0,"Iteracion")
        self.cabeceros = cabeceros
        self.iterador = 1
        
    def add_fila(self, fila: list):
        fila.insert(0,self.iterador)
        self.iterador += 1
        self.contenido.append(fila)
        
    def print_table(self, estilo = "github"):
        print(tabulate(self.contenido, headers=self.cabeceros,tablefmt=estilo))
        
    def get_tabla(self, estilo = "github"):
        return tabulate(self.contenido, headers=self.cabeceros,tablefmt=estilo)
        
class MathError(Exception):
    pass

class ParentesisError(Exception):
    pass

def raiz(radicando, indice = 2):
    if not type(indice) == int:
        raise MathError(f"Error en funcion raiz({radicando},{indice}) Solo indices naturales mayor o igual a 1")
    if indice < 1:
        raise MathError(f"Error en funcion raiz({radicando},{indice}) Solo indices naturales mayor o igual a 1")
    else:
        if indice%2 == 1:
            if radicando < 0:
                return -1 * (abs(radicando) ** (1/indice))
            else:
                return radicando ** (1/indice)
        else:
            if radicando < 0:
                raise MathError(f"Error en funcion raiz({radicando},{indice}) Radicando negativo en un raiz con indice par")
            else:
                return radicando ** (1/indice)
            
def cifras_significativas(n: int):
    return 0.5*10**(2-n)
