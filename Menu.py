from os import name, system
from re import findall

class CreacionMenuError(Exception):
        pass
    
class Menu():
    def limpiar(self):
        system('cls' if name == 'nt' else 'clear')

    def __init__(self, opciones: list, titulo="", metodo_seleccion = "numeracion"):
        """
            Parametros:
                opciones -> las opciones a mostrar en el menu
                titulo -> titulo del menu
                metodo_seleccion(por defecto 'numeracion') -> con esta opcion se puede seleccionar por el numero de la seleccion o por atajo personalizado puesto entre corchetes []
        """
        self.opciones = opciones
        self.titulo = titulo
        if metodo_seleccion == "numeracion":
            self.mostrar = True
            self.validos = []
            n = 1
            for opcion in opciones:
                if type(opcion) == Separador:
                    continue
                self.validos.append(str(n))
                n += 1
        else:
            self.mostrar = False
            self.validos = []
            for opcion in opciones:
                if type(opcion) == Separador:
                    continue
                resultado = findall("\[(.*?)\]", opcion)
                if len(resultado) > 1 :
                    raise CreacionMenuError(f"Una opcion del menu tiene mas de un atajo '{opcion}'")
                else:
                    if resultado[0] in self.validos:
                        raise CreacionMenuError(f"Este atajo ya existe mas de una vez '{resultado[0]}'")
                    else:
                        self.validos.append(resultado[0])
                    

    def show(self):
        """
            Muestra el menu y retorna la posicion de la opcion seleccionada
        """
        while True:
            if not self.titulo == "":
                print(self.titulo)
            n = 1
            for opcion in self.opciones:
                if type(opcion) == Separador:
                    print(opcion)
                else:
                    print(" " * 3 + (f"[{str(n)}]" if self.mostrar else "") + " " + opcion)
                    n += 1
            # pedir opcion
            nopcion = input("Seleccione una opcion ")
            if nopcion in self.validos:
                self.limpiar()
                return self.validos.index(nopcion)
            else:
                self.limpiar()
                continue


class Separador():
    seperador = "-" * 15
    
    def __init__(self, apartado=None):
        """
        Separador entre las opciones del menu, apartado para mostrar el texto en lugar de la linea
        """
        if apartado:
            self.seperador = apartado

    def __str__(self):
        return self.seperador