from os import name,system
import Menu

from FormulaEngine import validar_parentesis
from Utilidades import cifras_significativas, ValueError, OperacionDetenida, MathError

from Unidad1.Ejercicio1 import ejercicio1
from Unidad1.Ejercicio2 import ejercicio2
from Unidad1.Ejercicio3 import ejercicio3
from Unidad1.Ejercicio4 import ejercicio4
from Unidad1.Ejercicio5 import ejercicio5
from Unidad2.biseccion import Bisec
from Unidad2.falsaP import FalsaP
from Unidad2.PuntoFijo import PuntoFijo
from Unidad2.newtonRaphson import NewtonRaphson
from Unidad2.secante import Sec
from Unidad2.muller import muller
from Unidad2.bairstow import bairstow


#Permite limpiar la pantalla
def limpiar():
    system('cls' if name=='nt' else 'clear')


def pedir_valores(mensaje: str, historial: list):
    limpiar()
    while True:
        for h in historial:
            print(h)
        print("Escribir 'cancelar' para volver al menu")
        valor = input(mensaje)
        if valor.lower() == "cancelar":
            raise OperacionDetenida("Cancelado")
        else:
            try:
                return float(valor)
            except:
                limpiar()
                print("No es un numero")
                continue

def pedir_grado(mensaje: str, historial: list):
    limpiar()
    while True:
        for h in historial:
            print(h)
        print("Escribir 'cancelar' para volver al menu")
        valor = input(mensaje)
        if valor.lower() == "cancelar":
            raise OperacionDetenida("Cancelado")
        else:
            try:
                return int(valor)
            except:
                limpiar()
                print("No es un numero")
                continue

def pedir_error(historial: list):
    limpiar()
    menu_error = Menu.Menu(
        ['[1] Cifras Significativas',
         '[2] Valor de Error de Tolerancia'],
        titulo= "Error De Tolerancia",
        metodo_seleccion='atajo'
    )
    while True:
        opcion = menu_error.show()
        for h in historial:
            print(h)
        if opcion == 0:
            print("Escribir 'cancelar' para volver al menu")
            cifras = input("Cuantas cifras significativas?  ")
            
            if cifras.lower() == "cancelar":
                raise OperacionDetenida("Cancelado")
            
            if not cifras.isdecimal() :
                limpiar()
                print("No es un numero")
            else:
                return cifras_significativas(int(cifras))
        if opcion == 1:
            print("Escribir 'cancelar' para volver al menu")
            cifras = input("Escriba el error de tolerancia  ")
            
            if cifras.lower() == "cancelar":
                raise OperacionDetenida("Cancelado")
            else:
                return float(cifras)

def pedir_funcion(tema: str):
    limpiar()
    while True:
        print("Escriba 'cancelar' para volver al menu")
        funcion = input("{} Ingrese la funcion:  ".format(tema))
        funcion = funcion.lower()
        if funcion == "cancelar":
            raise OperacionDetenida("Cancelado")
        
        if funcion == "":
            limpiar()
            print("No ha escrito nada")
            continue
        
        if validar_parentesis(funcion):
            return funcion
        else:
            limpiar()
            print("La funcion no esta correctamente escrita")
            continue


def print_final(datos_iniciales: str, tabla):
    print("----Resultados----")
    print(datos_iniciales)
    print(tabla)
    print("\n")

menu_principal = Menu.Menu(
    ['[1] Unidad 1',
     '[2] Unidad 2',
     '[3] Unidad 3',
     '[4] Unidad 4',
     '[5] Unidad 5',
     Menu.Separador(),
     '[a] Ayuda',
     '[s] Salir'],
    titulo= 'Menu Principal',
    metodo_seleccion='atajo'
)


limpiar()
while True:
    opcion = menu_principal.show()
    
    if opcion == 0: #UNIDAD 1
        menu_1 = Menu.Menu(
            [
                '[1] Ln(e+x)',
                '[2] e^(x^2)',
                '[3] Sen(x)',
                '[4] Cos(x)',
                '[5] e^x',
                Menu.Separador(),
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            titulo= "Ejercicios de la unidad 1 por metodo de taylor",
            metodo_seleccion='atajo'
        )
        while True:
            opcion=menu_1.show()
            if opcion==0:#Ln(e+x)
                try:
                    xn = pedir_valores("[Ln(e+x)] Ingrese el valor del intervalo x:  ",
                                    [f""])
                    es = pedir_error(["Funcion: Ln(e+x)",xn])
                    limpiar()
                    print_final(f"Funcion: Ln(e+x), XN: {xn}, ES: {es}",
                                ejercicio1(xn,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif (opcion==1): #e^x^2
                try:
                    xn = pedir_valores("[e^(x^2)] Ingrese el valor del intervalo x:  ",
                                    [f""])
                    es = pedir_error(["Funcion: e^(x^2)",xn])
                    limpiar()
                    print_final(f"Funcion: e^(x^2), XN: {xn}, ES: {es}",
                                ejercicio2(xn,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 2: #Sen(x)
                try:
                    xn = pedir_valores("[Sen(x)] Ingrese el valor del intervalo x en grados:  ",
                                    [f""])
                    es = pedir_error(["Funcion: Sen(x)",xn])
                    limpiar()
                    print_final(f"Funcion: Sen(x), XN: {xn}, ES: {es}",
                                ejercicio3(xn,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 3: #Cos(x)
                try:
                    xn = pedir_valores("[Cos(x)] Ingrese el valor del intervalo x en grados:  ",
                                    [f""])
                    es = pedir_error(["Funcion: Cos(x)",xn])
                    limpiar()
                    print_final(f"Funcion: Cos(x), XN: {xn}, ES: {es}",
                                ejercicio4(xn,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 4: #e^x
                try:
                    xn = pedir_valores("[e^x] Ingrese el valor del intervalo x:  ",
                                    [f""])
                    es = pedir_error(["Funcion: e^x",xn])
                    limpiar()
                    print_final(f"Funcion: e^x, XN: {xn}, ES: {es}",
                                ejercicio5(xn,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 5:
                limpiar()
                #imprimir ayuda
                print("Aqui va la ayuda :v")
            elif opcion == 6:
                #Opcion terminar
                break


    
    elif opcion == 1: #UNIDAD 2
        menu_2 = Menu.Menu(
            [
                '[1] Biseccion',
                '[2] Falsa Posicion',
                '[3] Punto Fijo',
                '[4] Newton Raphson',
                '[5] Secante',
                '[6] Muller',
                '[7] Bairstow',
                Menu.Separador(),
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            titulo= "Metodos de la unidad 2",
            metodo_seleccion='atajo'
        )
        """
        Nota mental en el caso de la opcion ayuda y volver al menu principal
        como son los ultimos, si se agregan mas opciones al menu volver a ajustar su posicion
        """
        while True:
            opcion = menu_2.show()
            if opcion == 0: #Biseccion
                try:
                    funcion = pedir_funcion("[Biseccion]")
                    x1 = pedir_valores("[Biseccion] Ingrese el valor del intervalo inferior x1:  ",
                                    [f"Funcion: {funcion}"])
                    x2 = pedir_valores("[Biseccion] Ingrese el valor del intervalo superior x2:  ",
                                    [f"Funcion: {funcion}",
                                        f"X1: {x1}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                        f"X1: {x1}",
                                        f"X2: {x2}"
                                        ])
                    limpiar()
                    print_final(f"Funcion: {funcion},  X1: {x1},  X2: {x2},  ES: {es}",
                                Bisec(funcion,x1,x2,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 1: #Falsa Posicion
                try:
                    funcion = pedir_funcion("[Falsa Posicion]")
                    x1 = pedir_valores("[Falsa Posicion] Ingrese el valor del intervalo inferior x1:  ",
                                        [f"Funcion:{funcion}"])
                    x2 = pedir_valores("[Falsa Posicion] Ingrese el valor del intervalo superior x2:  ",
                                        [f"Funcion:{funcion}",
                                        f"X1: {x1}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                        f"X1: {x1}",
                                        f"X2: {x2}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, X1: {x1}, X2: {x2}, ES: {es}",
                                FalsaP(funcion,x1,x2,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 2: #Punto Fijo
                try:
                    funcion= pedir_funcion("[Punto Fijo]")
                    x = pedir_valores("[Punto Fijo] Ingrese el valor de x: ",
                                    [f"Funcion: {funcion}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                    f"X: {x}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, X: {x} ES: {es}",PuntoFijo(funcion,es,x))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
                
            elif opcion == 3: #Newton Raphson
                try:
                    funcion = pedir_funcion("[Newton Raphson]")
                    xi = pedir_valores("[Newton Raphson] Ingrese el valor de xi: ",
                                    [f"Funcion: {funcion}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                    f"X: {xi}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, XI: {xi} ES: {es}",
                                NewtonRaphson(funcion,xi,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 4: #Secante
                try:
                    funcion = pedir_funcion("[Secante]")
                    xnmenos = pedir_valores("[Secante] Ingrese el valor de xn-1: ",
                                            [f"Funcion: {funcion}"])
                    xn = pedir_valores("[Secante] Ingrese el valor de xn: ",
                                            [f"Funcion: {funcion}",
                                            f"Xn-1:{xnmenos}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                    f"Xn-1:{xnmenos}",
                                    f"Xn:{xn}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, Xn-1: {xnmenos}, Xn: {xn}, ES: {es}",
                                Sec(funcion,xnmenos,xn,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
                
            elif opcion == 5: #Muller
                try:
                    funcion = pedir_funcion("[Muller]")
                    x0 = pedir_valores("[Muller] Ingrese el valor de x0: ",
                                        [f"Funcion: {funcion}"])
                    x1 = pedir_valores("[Muller] Ingrese el valor de x1: ",
                                            [f"Funcion: {funcion}",
                                            f"X0= {x0}"])
                    x2 = pedir_valores("[Muller] Ingrese el valor de x2: ",
                                            [f"Funcion: {funcion}",
                                            f"X0 = {x0}",
                                            f"X! = {x1}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                        f"X0 = {x0}",
                                        f"X1 = {x1}",
                                        f"X2 = {x2}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, X0: {x0}, X1: {x1}, X2: {x2}, ES: {es}",
                                muller(funcion,x0,x1,x2,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 6: #Bairstow
                try:
                    r = pedir_valores("[Bairstow] Ingrese el valor de r: ", "")
                    s = pedir_valores("[Bairstow] Ingrese el valor de s:", 
                                        [f"r= {r}"])
                    es = pedir_error([f"r= {r}",
                                        f"s= {s}"])
                    grado = pedir_grado("[Bairstow] Ingrese el grado del polinomio al cual desea calcularle las raices: ", 
                                        [f"r= {r}",
                                        f"s= {s}",
                                        f"es= {es}"])
                    coe = []
                    rango = range(0, grado + 1)
                    for i in rango:
                        coe.append(float(pedir_valores("[Bairstow] Ingrese el coeficiente x"+ str(i)+": ",[f"r= {r}",
                                        f"s= {s}",
                                        f"Coeficientes (Mayor a menor): {coe}"])))
                    limpiar()
                    print_final(f"r: {r}, s: {s}, Coeficientes: {coe}", 
                                bairstow(r, s, coe, es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 7:
                limpiar()
                #imprimir ayuda
                print("Aqui va la ayuda :v")
            elif opcion == 8:
                #Opcion terminar
                break
                
        
    elif opcion == 2: #UNIDAD 3
        pass
    
    elif opcion == 3: #UNIDAD 4
        pass
    
    elif opcion == 4: #UNIDAD 5
        pass
    
    elif opcion == 5:
        print("Aqui va la ayuda :v")
        input("Presione cualquier tecla para continuar")
    
    elif opcion == 6:
        if input('Desea terminar? (y/n)').lower() == 'y':
            break
        
    #Se limpia la pantalla
    limpiar()
