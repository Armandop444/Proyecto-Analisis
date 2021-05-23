from tabulate import tabulate
import re
from os import name, system


# Excepciones necesarias para mostrar el tipo de error
class MathError(Exception):
    pass


class ValueError(Exception):
    pass


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


# Permite limpiar la pantalla
def limpiar():
    system('cls' if name == 'nt' else 'clear')

# funciones utiles


def cifras_significativas(n: int):
    return 0.5*10**(2-n)


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
                inicioBuscar = posicion+1
                posicionConvertido = posicionConvertido+1

            posicion = posicion+1
        cuantasRaices = cuantasRaices-1
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
