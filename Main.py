import Menu
from FormulaEngine import validar_parentesis,reconvertir_funcion, convertir_funcion, MathError, ValueError,comprobarpunto
from Utilidades import cifras_significativas, OperacionDetenida, Graficadora, limpiar

#Ayuda
from Ayuda import ayuda
# Unidad 1
from Unidad1.Ejercicio1 import ejercicio1
from Unidad1.Ejercicio2 import ejercicio2
from Unidad1.Ejercicio3 import ejercicio3
from Unidad1.Ejercicio4 import ejercicio4
from Unidad1.Ejercicio5 import ejercicio5
from Unidad1.Ejercicio6 import ejercicio6
from Unidad1.Ejercicio7 import ejercicio7
from Unidad1.Ejercicio8 import ejercicio8
from Unidad1.Ejercicio9 import ejercicio9
from Unidad1.Ejercicio10 import ejercicio10
from Unidad1.Ejercicio11 import ejercicio11
# Unidad 2
from Unidad2.biseccion import Bisec
from Unidad2.falsaP import FalsaP
from Unidad2.PuntoFijo import PuntoFijo
from Unidad2.newtonRaphson import NewtonRaphson
from Unidad2.NewtonTuneado import NewtonTuneado
from Unidad2.secante import Sec
from Unidad2.muller import muller
from Unidad2.bairstow import bairstow
# Unidad 3
from Unidad3.Lagrange import grange
from Unidad3.NewtonRecursiva import newton
from Unidad3.NewtonDiferencias import NewtonDD
from Unidad3.Hermite import hermiteNormal
from Unidad3.HermiteDiferencias import HermiteD
# Unidad 4
from Unidad4.DiferenciacionNumerica import *
from Unidad4.DiferenciacionNumericaSuperior import *
from Unidad4.trapecio import trapecio
from Unidad4.simpson13 import simp
from Unidad4.simpson38 import simp3
from Unidad4.cuadraturaGauss import gauss
from Unidad4.Richardson import Richardson
from Unidad4.rosemberg import Rosemberg
# Unidad 5
from Unidad5.EulerMod import euler
from Unidad5.taylor import taylor
from Unidad5.Kuttaorden4 import Kutta
from Unidad5.Multipasos import main

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
                return float(comprobarpunto(valor))
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
        titulo="Error De Tolerancia",
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

            if not cifras.isdecimal():
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
    titulo='Menu Principal',
    metodo_seleccion='atajo'
)


limpiar()
while True:
    opcion = menu_principal.show()

    if opcion == 0:  # UNIDAD 1
        menu_1 = Menu.Menu(
            [
                '[1] Ln(e+x)',
                '[2] e^(x^2)',
                '[3] Sen(x)',
                '[4] Cos(x)',
                '[5] e^x',
                '[6] sh x ',
                '[7] ch x',
                '[8] arcsen(x)',
                '[9] ln(1+x)',
                '[10] 1/(1+x^2)',
                '[11] arctan(x)',
                Menu.Separador(),
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            titulo="Ejercicios de la unidad 1 por metodo de taylor",
            metodo_seleccion='atajo'
        )
        while True:
            opcion = menu_1.show()
            if opcion == 0:  # Ln(e+x)
                try:
                    xn = pedir_valores("[Ln(e+x)] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    es = pedir_error(["Funcion: Ln(e+x)", xn])
                    limpiar()
                    print_final(f"Funcion: Ln(e+x), XN: {xn}, ES: {es}",
                                ejercicio1(xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif (opcion == 1):  # e^x^2
                try:
                    xn = pedir_valores("[e^(x^2)] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    es = pedir_error(["Funcion: e^(x^2)", xn])
                    limpiar()
                    print_final(f"Funcion: e^(x^2), XN: {xn}, ES: {es}",
                                ejercicio2(xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 2:  # Sen(x)
                try:
                    xn = pedir_valores("[Sen(x)] Ingrese el valor del intervalo x en grados:  ",
                                       [f""])
                    es = pedir_error(["Funcion: Sen(x)", xn])
                    limpiar()
                    print_final(f"Funcion: Sen(x), XN: {xn}, ES: {es}",
                                ejercicio3(xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 3:  # Cos(x)
                try:
                    xn = pedir_valores("[Cos(x)] Ingrese el valor del intervalo x en grados:  ",
                                       [f""])
                    es = pedir_error(["Funcion: Cos(x)", xn])
                    limpiar()
                    print_final(f"Funcion: Cos(x), XN: {xn}, ES: {es}",
                                ejercicio4(xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 4:  # e^x
                try:
                    xn = pedir_valores("[e^x] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    es = pedir_error(["Funcion: e^x", xn])
                    limpiar()
                    print_final(f"Funcion: e^x, XN: {xn}, ES: {es}",
                                ejercicio5(xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 5:  # sh x
                try:
                    xn = pedir_valores("[sh x] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    es = pedir_error(["Funcion: sh x", xn])
                    limpiar()
                    print_final(f"Funcion: sh x, XN: {xn}, ES: {es}",
                                ejercicio6(xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 6:  # ch x
                try:
                    xn = pedir_valores("[ch x] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    es = pedir_error(["Funcion: ch x", xn])
                    limpiar()
                    print_final(f"Funcion: ch x, XN: {xn}, ES: {es}",
                                ejercicio7(xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 7:  # arcsen(x)
                try:
                    xn = pedir_valores("[arcsen(x)] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    if xn>=-1 and xn<1:
                        es = pedir_error(["Funcion: arcsen(x)", xn])
                        limpiar()
                        print_final(f"Funcion: arcsen(x), XN: {xn}, ES: {es}",
                                    ejercicio8(xn, es))
                    else:
                        print("El rango de xn no es el correcto para el ejercicio")
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 8:  # ln(1+x)
                try:
                    xn = pedir_valores("[ln(1+x)] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    if xn>-1 and xn<1:
                        es = pedir_error(["Funcion: lnx(1+x)", xn])
                        limpiar()
                        print_final(f"Funcion: ln(1+x), XN: {xn}, ES: {es}",
                                    ejercicio9(xn, es))
                    else:
                        print("El rango de xn no es el correcto para el ejercicio")
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 9:  # 1/(1+x^2)
                try:
                    xn = pedir_valores("1/(1+x^2)] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    if xn>-1 and xn<1:
                        es = pedir_error(["Funcion: 1/(1+x^2)", xn])
                        limpiar()
                        print_final(f"Funcion: 1/(1+x^2), XN: {xn}, ES: {es}",
                                    ejercicio10(xn, es))
                    else:
                        print("El rango de xn no es el correcto para el ejercicio")

                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 10:  # arctan(x)
                try:
                    xn = pedir_valores("[arctan(x)] Ingrese el valor del intervalo x:  ",
                                       [f""])
                    if xn>=-1 and xn<=1:
                        es = pedir_error(["Funcion: arctan(x)", xn])
                        limpiar()
                        print_final(f"Funcion: arctan(x), XN: {xn}, ES: {es}",
                                    ejercicio11(xn, es))
                    else:
                        print("El rango de xn no es el correcto para el ejercicio")
                except OperacionDetenida:
                    limpiar()
                    continue
            elif opcion == 11:
                limpiar()
                ayuda()
                input("Presione cualquier tecla para continuar")
                limpiar()
            elif opcion == 12:
                # Opcion terminar
                break

    elif opcion == 1:  # UNIDAD 2
        menu_2 = Menu.Menu(
            [
                '[1] Biseccion',
                '[2] Falsa Posicion',
                '[3] Punto Fijo',
                '[4] Newton Raphson',
                '[5] Newton Raphson Modificado',
                '[6] Secante',
                '[7] Muller',
                '[8] Bairstow',
                Menu.Separador(),
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            titulo="Metodos de la unidad 2",
            metodo_seleccion='atajo'
        )
        """
        Nota mental en el caso de la opcion ayuda y volver al menu principal
        como son los ultimos, si se agregan mas opciones al menu volver a ajustar su posicion
        """
        while True:
            opcion = menu_2.show()
            if opcion == 0:  # Biseccion
                try:
                    funcion = pedir_funcion("[Biseccion]")
                    grafica = Graficadora()
                    grafica.render(funcion,"Biseccion")
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
                                Bisec(funcion, x1, x2, es))
                except OperacionDetenida:
                    limpiar()
                    continue

                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 1:  # Falsa Posicion
                try:
                    funcion = pedir_funcion("[Falsa Posicion]")
                    grafica = Graficadora()
                    grafica.render(funcion,"Falsa Posicion")
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
                                FalsaP(funcion, x1, x2, es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 2:  # Punto Fijo
                try:
                    funcion = pedir_funcion("[Punto Fijo]")
                    x = pedir_valores("[Punto Fijo] Ingrese el valor de x: ",
                                        [f"Funcion: {funcion}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                        f"X: {x}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, X: {x} ES: {es}", 
                                PuntoFijo(funcion, es, x))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 3:  # Newton Raphson
                try:
                    funcion = pedir_funcion("[Newton Raphson]")
                    grafica = Graficadora()
                    grafica.render(funcion,"Newton Raphson")
                    xi = pedir_valores("[Newton Raphson] Ingrese el valor de xi: ",
                                       [f"Funcion: {funcion}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                      f"X: {xi}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, XI: {xi} ES: {es}",
                                NewtonRaphson(funcion, xi, es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 4:  # Newton Raphson Modificado
                try:
                    funcion = pedir_funcion("[Newton Raphson M]")
                    grafica = Graficadora()
                    grafica.render(funcion,"Newton Raphson Modificado")
                    xi = pedir_valores("[Newton Raphson M] Ingrese el valor de xi: ",
                                       [f"Funcion: {funcion}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                      f"X: {xi}"])
                    limpiar()
                    print_final(f"Funcion: {funcion}, XI: {xi} ES: {es}",
                                NewtonTuneado(funcion, xi, es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 5:  # Secante
                try:
                    funcion = pedir_funcion("[Secante]")
                    grafica = Graficadora()
                    grafica.render(funcion,"Secante")
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
                                Sec(funcion, xnmenos, xn, es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 6:  # Muller
                try:
                    funcion = pedir_funcion("[Muller]")
                    grafica = Graficadora()
                    grafica.render(funcion,"Muller")
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
                                muller(funcion, x0, x1, x2, es))
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")

            elif opcion == 7:  # Bairstow
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
                        coe.append(float(pedir_valores("[Bairstow] Ingrese el coeficiente x" + str(i)+": ", [f"r= {r}",
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
            elif opcion == 8:
                limpiar()
                ayuda()
                input("Presione cualquier tecla para continuar")
                limpiar()
            elif opcion == 9:
                # Opcion terminar
                break

    elif opcion == 2:  # UNIDAD 3
        menu_3 = Menu.Menu(
            [
                '[1] Lagrange',
                '[2] Interpolacion de Newton',
                '[3] Diferencias Divididas',
                '[4] Polinomio de Hermite',
                Menu.Separador(),
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            titulo="Metodos de la unidad 3",
            metodo_seleccion='atajo'
        )

        while True:
            opcion = menu_3.show()
            if opcion == 0:  # Lagrange
                try:
                    grange()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 1:  # Newton Recursivo
                try:
                    newton()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 2:  # Diferencias Divididas
                menu_mini = Menu.Menu(
                    [
                        '[1] Interpolacion de Newton',
                        '[2] Polinomio de Hermite',
                        Menu.Separador(),
                        '[s] Volver al menu principal'
                    ],
                    titulo="Metodos por Diferencias Divididas",
                    metodo_seleccion='atajo'
                )
                opcion2 = menu_mini.show()
                if opcion2 == 0:  # Newton Diferencias
                    try:
                        NewtonDD()
                    except OperacionDetenida:
                        limpiar()
                        continue
                    except MathError as e:
                        print("MathError: " + e)
                        input("Presione cualquier tecla para continuar")
                    except Exception as e:
                        print(f"Algo ha salido mal {e}")
                        input("Presione cualquier tecla para continuar")
                elif opcion2 == 1:  # Hermite Diferencias
                    try:
                        HermiteD()
                    except OperacionDetenida:
                        limpiar()
                        continue
                    except MathError as e:
                        print("MathError: " + e)
                        input("Presione cualquier tecla para continuar")
                    except Exception as e:
                        print(f"Algo ha salido mal {e}")
                        input("Presione cualquier tecla para continuar")

                elif opcion2 == 2:
                    # Opcion terminar
                    break
            elif opcion == 3:  # Hermite normal
                try:
                    hermiteNormal()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 4:
                limpiar()
                ayuda()
                input("Presione cualquier tecla para continuar")
                limpiar()
            elif opcion == 5:
                # Opcion terminar
                break

    elif opcion == 3:  # UNIDAD 4
        menu_4 = Menu.Menu(
            [
                '[1] Derivacion Numerica',
                '[2] Derivacion Numerica Superior',
                '[3] Integracion Numerica',
                '[4] Richardson',
                '[5] Rosemberg',
                Menu.Separador(),
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            titulo="Metodos de la unidad 4",
            metodo_seleccion='atajo'
        )
        while True:
            opcion = menu_4.show()
            if opcion == 0:  # Derivacion
                menu_mini = Menu.Menu(
                    [
                        '[1] Adelante',
                        '[2] Atras',
                        '[3] Centrada',
                        Menu.Separador(),
                        '[s] Volver al menu principal'
                    ],
                    titulo="Metodos para Derivacion Numerica",
                    metodo_seleccion='atajo')
                opcion2 = menu_mini.show()
                if opcion2 == 0 or opcion2 == 1:  # Adelante o Atras
                    menu_mini2 = Menu.Menu(
                        [
                            '[1] Primera Diferencia',
                            '[2] Segunda Diferencia',
                            Menu.Separador(),
                            '[s] Volver al menu principal'
                        ],
                        titulo="Tipo de Diferencia",
                        metodo_seleccion='atajo')
                    opcion3 = menu_mini2.show()
                    if opcion2 == 0:  # Adelante
                        try:
                            # Pedir los valores
                            funcion=""
                            tipo=input("Ingresara:\n1.Funcion\n2.Tabla")
                            if tipo=="2":
                                px=0
                                xi = pedirValores("xi", "")
                                yi = pedirValores("fi", len(xi))
                                for i in range(len(xi)):
                                    l = yi[i]
                                    for k in range(len(xi)):
                                        if k != i:
                                            l = l*((x-xi[k])/(xi[i]-xi[k]))
                                            px = px+l
                                funcion = str(px.expand())
                            else:
                                funcion=pedir_funcion("[Diferencia Hacia Adelante]")
                                funcion=convertir_funcion(funcion)
                            xo=pedir_valores("Ingrese el valor de x", [f"Funcion {reconvertir_funcion(funcion)}"])
                            h=pedir_valores("Ingrese el valor de h", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}"])
                            if opcion3 == 0:  # primera
                                diffforwardfunc(funcion, xo, h, 1)
                            else:  # segunda
                                diffforwardfunc(funcion, xo, h, 2)
                        except OperacionDetenida:
                            limpiar()
                            continue
                        except MathError as e:
                            print("MathError: " + e)
                            input("Presione cualquier tecla para continuar")
                        except Exception as e:
                            print(f"Algo ha salido mal {e}")
                            input("Presione cualquier tecla para continuar")
                    elif opcion2 == 1:  # Atras
                        try:
                            # Pedir los valores
                            funcion=""
                            tipo=input("Ingresara:\n1.Funcion\n2.Tabla")
                            if tipo=="2":
                                px=0
                                xi = pedirValores("xi", "")
                                yi = pedirValores("fi", len(xi))
                                for i in range(len(xi)):
                                    l = yi[i]
                                    for k in range(len(xi)):
                                        if k != i:
                                            l = l*((x-xi[k])/(xi[i]-xi[k]))
                                            px = px+l
                                funcion = str(px.expand())
                            else:
                                funcion=pedir_funcion("[Diferencia Hacia Atras]")
                                funcion=convertir_funcion(funcion)
                            xo=pedir_valores("Ingrese el valor de x", [f"Funcion {reconvertir_funcion(funcion)}"])
                            h=pedir_valores("Ingrese el valor de h", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}"])
                            if opcion3 == 0:  # primera
                                diffbackwardfunc(funcion, xo, h, 1)
                            else:  # segunda
                                diffbackwardfunc(funcion, xo, h, 2)
                        except OperacionDetenida:
                            limpiar()
                            continue
                        except MathError as e:
                            print("MathError: " + e)
                            input("Presione cualquier tecla para continuar")
                        except Exception as e:
                            print(f"Algo ha salido mal {e}")
                            input("Presione cualquier tecla para continuar")

                elif opcion2 == 2:  # Centrada
                    menu_mini2 = Menu.Menu(
                        [
                            '[1] Orden 2',
                            '[2] Orden 4',
                            '[3] Con 3 puntos',
                            '[4] Con 5 puntos',
                            Menu.Separador(),
                            '[s] Volver al menu principal'
                        ],
                        titulo="Tipo de Diferencia",
                        metodo_seleccion='atajo')
                    opcion3 = menu_mini2.show()
                    if opcion3 >= 0 or opcion3 <= 3:  # todo el menu de orden2 a 5 puntos
                        try:
                            # Pedir los valores
                            funcion=""
                            tipo=input("Ingresara:\n1.Funcion\n2.Tabla")
                            if tipo=="2":
                                px=0
                                xi = pedirValores("xi", "")
                                yi = pedirValores("fi", len(xi))
                                for i in range(len(xi)):
                                    l = yi[i]
                                    for k in range(len(xi)):
                                        if k != i:
                                            l = l*((x-xi[k])/(xi[i]-xi[k]))
                                            px = px+l
                                funcion = str(px.expand())
                            else:
                                funcion=pedir_funcion("[Diferencia Centrada]")
                                funcion=convertir_funcion(funcion)
                            xo=pedir_valores("Ingrese el valor de x", [f"Funcion {reconvertir_funcion(funcion)}"])
                            h=pedir_valores("Ingrese el valor de h", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}"])
                            if opcion3 == 0:  # orden2
                                diffcentralfunc(funcion, xo, h, 1)
                            elif opcion3 == 1:  # orden4
                                diffcentralfunc(funcion, xo, h, 2)
                            elif opcion3 == 2:  # 3 puntos
                                diffcentralfunc(funcion, xo, h, 3)
                            elif opcion3 == 3:  # 5 puntos
                                diffcentralfunc(funcion, xo, h, 4)
                        except OperacionDetenida:
                            limpiar()
                            continue
                        except MathError as e:
                            print("MathError: " + e)
                            input("Presione cualquier tecla para continuar")
                        except Exception as e:
                            print(f"Algo ha salido mal {e}")
                            input("Presione cualquier tecla para continuar")

            if opcion == 1:  # Orden Superior
                menu_mini = Menu.Menu(
                    [
                        '[1] Adelante',
                        '[2] Atras',
                        '[3] Centrada',
                        Menu.Separador(),
                        '[s] Volver al menu principal'
                    ],
                    titulo="Metodos para Derivacion Numerica Superior",
                    metodo_seleccion='atajo')
                opcion2 = menu_mini.show()
                if opcion2 == 0 or opcion2 == 1 or opcion2==2:  # Adelante o Atras
                    menu_mini2 = Menu.Menu(
                        [
                            '[1] Primera Diferencia',
                            '[2] Segunda Diferencia',
                            Menu.Separador(),
                            '[s] Volver al menu principal'
                        ],
                        titulo="Tipo de Diferencia",
                        metodo_seleccion='atajo')
                    opcion3 = menu_mini2.show()
                    if opcion2 == 0:  # Adelante
                        try:
                            # Pedir los valores
                            funcion=""
                            tipo=input("Ingresara:\n1.Funcion\n2.Tabla")
                            if tipo=="2":
                                px=0
                                xi = pedirValores("xi", "")
                                yi = pedirValores("fi", len(xi))
                                for i in range(len(xi)):
                                    l = yi[i]
                                    for k in range(len(xi)):
                                        if k != i:
                                            l = l*((x-xi[k])/(xi[i]-xi[k]))
                                            px = px+l
                                funcion = str(px.expand())
                            else:
                                funcion=pedir_funcion("[Diferencia Hacia Adelante]")
                                funcion=convertir_funcion(funcion)
                            xo=pedir_valores("Ingrese el valor de x", [f"Funcion {reconvertir_funcion(funcion)}"])
                            h=pedir_valores("Ingrese el valor de h", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}"])
                            orden=pedir_valores("Ingrese el orden de derivada (orden 2 a 4)", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}",
                                            f"H: {h}"])
                            if opcion3 == 0:  # primera
                                diffnumsupfor(funcion, xo, h, 1, orden)
                            else:  # segunda
                                diffnumsupfor(funcion, xo, h, 2, orden)
                        except OperacionDetenida:
                            limpiar()
                            continue
                        except MathError as e:
                            print("MathError: " + e)
                            input("Presione cualquier tecla para continuar")
                        except Exception as e:
                            print(f"Algo ha salido mal {e}")
                            input("Presione cualquier tecla para continuar")
                    elif opcion2 == 1:  # Atras
                        try:
                            # Pedir los valores
                            funcion=""
                            tipo=input("Ingresara:\n1.Funcion\n2.Tabla")
                            if tipo=="2":
                                px=0
                                xi = pedirValores("xi", "")
                                yi = pedirValores("fi", len(xi))
                                for i in range(len(xi)):
                                    l = yi[i]
                                    for k in range(len(xi)):
                                        if k != i:
                                            l = l*((x-xi[k])/(xi[i]-xi[k]))
                                            px = px+l
                                funcion = str(px.expand())
                            else:
                                funcion=pedir_funcion("[Diferencia Hacia Atras]")
                                funcion=convertir_funcion(funcion)
                            xo=pedir_valores("Ingrese el valor de x", [f"Funcion {reconvertir_funcion(funcion)}"])
                            h=pedir_valores("Ingrese el valor de h", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}"])
                            orden=pedir_valores("Ingrese el orden de derivada (orden 2 a 4)", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}",
                                            f"H: {h}"])
                            if opcion3 == 0:  # primera
                                diffnumsupback(funcion, xo, h, 1, orden)
                            else:  # segunda
                                diffnumsupback(funcion, xo, h, 2, orden)
                        except OperacionDetenida:
                            limpiar()
                            continue
                        except MathError as e:
                            print("MathError: " + e)
                            input("Presione cualquier tecla para continuar")
                        except Exception as e:
                            print(f"Algo ha salido mal {e}")
                            input("Presione cualquier tecla para continuar")

                    elif opcion2 == 2:  # centrada
                        try:
                            # Pedir los valores
                            funcion=""
                            tipo=input("Ingresara:\n1.Funcion\n2.Tabla")
                            if tipo=="2":
                                px=0
                                xi = pedirValores("xi", "")
                                yi = pedirValores("fi", len(xi))
                                for i in range(len(xi)):
                                    l = yi[i]
                                    for k in range(len(xi)):
                                        if k != i:
                                            l = l*((x-xi[k])/(xi[i]-xi[k]))
                                            px = px+l
                                funcion = str(px.expand())
                            else:
                                funcion=pedir_funcion("[Diferencia Centrada]")
                                funcion=convertir_funcion(funcion)
                            xo=pedir_valores("Ingrese el valor de x", [f"Funcion {reconvertir_funcion(funcion)}"])
                            h=pedir_valores("Ingrese el valor de h", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}"])
                            orden=pedir_valores("Ingrese el orden de derivada (orden 2 a 4)", [f"Funcion {reconvertir_funcion(funcion)}",
                                            f"X0: {xo}",
                                            f"H: {h}"])
                            if opcion3 == 0:  # primera
                                diffnumsupcentral(funcion, xo, h, 1, orden)
                            else:  # segunda
                                diffnumsupcentral(funcion, xo, h, 2, orden)
                        except OperacionDetenida:
                            limpiar()
                            continue
                        except MathError as e:
                            print("MathError: " + e)
                            input("Presione cualquier tecla para continuar")
                        except Exception as e:
                            print(f"Algo ha salido mal {e}")
                            input("Presione cualquier tecla para continuar")


            elif opcion == 2:  # Integracion
                menu_mini = Menu.Menu(
                    [
                        '[1] Trapecio',
                        '[2] Simpson 1/3',
                        '[3] Simpson 3/8',
                        '[4] Cuadratura Gauss',
                        Menu.Separador(),
                        '[s] Volver al menu principal'
                    ],
                    titulo="Metodos para Integracion Numerica",
                    metodo_seleccion='atajo')
                opcion2 = menu_mini.show()
                if opcion2 == 0: #Trapecio
                    try:
                        trapecio()
                    except OperacionDetenida:
                        limpiar()
                        continue
                    except MathError as e:
                        print("MathError: " + e)
                        input("Presione cualquier tecla para continuar")
                    except Exception as e:
                        print(f"Algo ha salido mal {e}")
                        input("Presione cualquier tecla para continuar")
                elif opcion2 == 1 :#Simpson 1/3
                    try:
                        simp()
                    except OperacionDetenida:
                        limpiar()
                        continue
                    except MathError as e:
                        print("MathError: " + e)
                        input("Presione cualquier tecla para continuar")
                    except Exception as e:
                        print(f"Algo ha salido mal {e}")
                        input("Presione cualquier tecla para continuar")
                elif opcion2 == 2 :#Simpson 3/8
                    try:
                        simp3()
                    except OperacionDetenida:
                        limpiar()
                        continue
                    except MathError as e:
                        print("MathError: " + e)
                        input("Presione cualquier tecla para continuar")
                    except Exception as e:
                        print(f"Algo ha salido mal {e}")
                        input("Presione cualquier tecla para continuar")
                elif opcion2 == 3 :#Cuadratura Gauss
                    try:
                        gauss()
                    except OperacionDetenida:
                        limpiar()
                        continue
                    except MathError as e:
                        print("MathError: " + e)
                        input("Presione cualquier tecla para continuar")
                    except Exception as e:
                        print(f"Algo ha salido mal {e}")
                        input("Presione cualquier tecla para continuar")
            elif opcion==3:#Richarson
                try:
                    Richardson()
                    input()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion==4:#Rosemberg
                try:
                    print(Rosemberg())
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion==5:#aiuda
                limpiar()
                ayuda()
                input("Presione cualquier tecla para continuar")
                limpiar()
            elif opcion==6:
                break

    elif opcion == 4:  # UNIDAD 5
        menu_5 = Menu.Menu(
            [
                '[1] Euler Modificado',
                '[2] Metodo de Taylor',
                '[3] Runge Kutta 4 orden',
                '[4] Multipasos',
                Menu.Separador(),
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            titulo="Metodos de la Unidad 5",
            metodo_seleccion='atajo'
        )
        while True:
            opcion=menu_5.show()
            if opcion==0:#Euler Mod
                try:
                    euler()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion==1:#Taylor
                try:
                    taylor()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion==2:#kutta
                try:
                    Kutta()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion==3:#Multipasos
                try:
                    main()
                except OperacionDetenida:
                    limpiar()
                    continue
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 4:
                limpiar()
                ayuda()
                input("Presione cualquier tecla para continuar")
                limpiar()
            elif opcion ==5:
                break

    elif opcion == 5:
        limpiar()
        ayuda()
        input("Presione cualquier tecla para continuar")

    elif opcion == 6:
        if input('Desea terminar? (y/n)').lower() == 'y':
            break

    # Se limpia la pantalla
    limpiar()
