from os import name, system
from FormulaEngine import convertir_funcion, MathError
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, tan, log, exp, arcsin, arccos, arctan


# Excepciones necesarias para mostrar el tipo de error
class OperacionDetenida(Exception):
    pass

# clase para generar tablas chivas
class tablita:
    def __init__(self, cabeceros, show_iteracion=True):
        self.contenido = []
        self.show_iteracion = show_iteracion
        if show_iteracion:
            cabeceros.insert(0, "Iteracion")
            self.iterador = 1
        self.cabeceros = cabeceros

    def add_fila(self, fila: list):
        if self.show_iteracion:
            fila.insert(0, self.iterador)
            self.iterador += 1
        self.contenido.append(str(elemento) for elemento in fila)

    def print_table(self, estilo="github"):
        print(tabulate(self.contenido, headers=self.cabeceros, tablefmt=estilo))

    def get_tabla(self, estilo="github"):
        return tabulate(self.contenido, headers=self.cabeceros, tablefmt=estilo)

# Para graficar
class Graficadora:

    def __init__(self) -> None:
        pass

    def render(self, funcion : str, titulo = "", inicio = -50.0, final = 50.0, paso = 0.01):
        #preparar datos
        x = np.arange(inicio,final,paso)
        y = eval(convertir_funcion(funcion, graficar=True))


        fig, ax = plt.subplots()

        ax.plot(x,y, label = f"y = {funcion}")
        ax.set(xlabel = "Eje X", ylabel="Eje Y", title = titulo)
        ax.grid(True, linestyle="-.")
        plt.axhline(y = 0, color="black")
        plt.axvline(x = 0, color="black")
        plt.ylim((-10,10))
        plt.xlim((-10,10))
        plt.legend()
        plt.show()


# Permite limpiar la pantalla
def limpiar():
    system('cls' if name == 'nt' else 'clear')

# funciones utiles
def cifras_significativas(n: int):
    return 0.5*10**(2-n)




# Recuerdame
def raizA(radicando, indice=2):
    if not type(indice) == int:
        raise MathError(
            f"Error en funcion raiz({radicando},{indice}) Solo indices naturales mayor o igual a 1")
    if indice < 1:
        raise MathError(
            f"Error en funcion raiz({radicando},{indice}) Solo indices naturales mayor o igual a 1")
    else:
        if indice % 2 == 1:
            if radicando < 0:
                return -1 * (abs(radicando) ** (1/indice))
            else:
                return radicando ** (1/indice)
        else:
            if radicando < 0:
                raise MathError(
                    f"Error en funcion raiz({radicando},{indice}) Radicando negativo en un raiz con indice par")
            else:
                return radicando ** (1/indice)
