from os import name,system
from simple_term_menu import TerminalMenu
from FormulaEngine import validar_parentesis, convertir_funcion
from Utilidades import cifras_significativas, ValueError, OperacionDetenida, MathError
from biseccion import Bisec
from sympy import parse_expr

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


def pedir_error(historial: list):
    limpiar()
    menu_error = TerminalMenu(
        ['[1] Cifras Significativas',
         '[2] Valor de Error de Tolerancia'],
        title= "Error De Tolerancia",
        clear_menu_on_exit= True
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
            

def pedir_funcion():
    limpiar()
    while True:
        print("Escriba 'cancelar' para volver al menu")
        funcion = input("Ingrese la funcion:  ")
        
        if funcion == "cancelar":
            raise OperacionDetenida("Cancelado")
        
        if funcion == "":
            limpiar()
            print("No ha escrito nada")
            continue
        
        if validar_parentesis(funcion):
            return convertir_funcion(funcion)
        else:
            limpiar()
            print("La funcion no esta correctamente escrita")
            continue


def print_final(datos_iniciales: str, tabla):
    print("----Resultados----")
    print(datos_iniciales)
    print(tabla)
    print("\n")

menu_principal = TerminalMenu(
    ['[1] Unidad 1',
     '[2] Unidad 2',
     '[3] Unidad 3',
     '[4] Unidad 4',
     '[5] Unidad 5',
     '[a] Ayuda',
     '[s] Salir'],
    title= 'Menu Principal',
    clear_menu_on_exit=True
)


limpiar()
while True:
    opcion = menu_principal.show()
    
    if opcion == 0:
        pass
    
    elif opcion == 1:
        menu_2 = TerminalMenu(
            [
                '[1] Biseccion',
                '[2] Falsa Posicion',
                '[3] Punto Fijo',
                '[4] Secante',
                '[5] Newton Raphson',
                '[a] Ayuda',
                '[s] Volver al menu principal'
            ],
            title= "Metedos de la unidad 2",
            clear_menu_on_exit=True
        )
        """
        Nota mental en el caso de la opcion ayuda y volver al menu principal
        como son los ultimos, si se agregan mas opciones al menu volver a ajustar su posicion
        """
        while True:
            opcion = menu_2.show()
            if opcion == 0:
                try:
                    funcion = pedir_funcion()
                    x1 = pedir_valores("Ingrese el valor del intervalo inferior x1:  ",
                                    [f"Funcion: {funcion}"])
                    x2 = pedir_valores("Ingrese el valor del intervalo inferior x2:  ",
                                    [f"Funcion: {funcion}",
                                        f"X1: {x1}"])
                    es = pedir_error([f"Funcion: {funcion}",
                                        f"X1: {x1}",
                                        f"X2: {x2}"
                                        ])
                    limpiar()
                    print_final(f"Funcion: {funcion},  X1: {x1},  X2: {x2},  ES: {es}",Bisec(parse_expr(funcion),x1,x2,es))
                except OperacionDetenida:
                    limpiar()
                    continue
                
                except MathError as e:
                    print("MathError: " + e)
                    input("Presione cualquier tecla para continuar")
                except Exception as e:
                    print(f"Algo ha salido mal {e}")
                    input("Presione cualquier tecla para continuar")
            elif opcion == 1:
                #pedir funcion
                #pedir error de tolerancia por cifras significativas o el valor
                #los valores del intervalo
                #llamar el metodo de Falsa Posicion
                pass
            elif opcion == 2:
                #pedir funcion
                #pedir error de tolerancia por cifras significativas o el valor
                #los valores del intervalo
                #llamar el metodo de Punto Fijo
                pass
            elif opcion == 3:
                #pedir funcion
                #pedir error de tolerancia por cifras significativas o el valor
                #los valores iniciales
                #llamar el metodo de Secante
                pass
            elif opcion == 4:
                #pedir funcion
                #pedir error de tolerancia por cifras significativas o el valor
                #los valores del intervalo
                #llamar el metodo de Punto Fijo
                pass
            elif opcion == 5:
                limpiar()
                #imprimir ayuda
                print("Aqui va la ayuda :v")
            elif opcion == 6:
                #Opcion terminar
                break
                
        
    elif opcion == 2:
        pass
    
    elif opcion == 3:
        pass
    
    elif opcion == 4:
        pass
    
    elif opcion == 5:
        print("Aqui va la ayuda :v")
        input("Presione cualquier tecla para continuar")
    
    elif opcion == 6:
        if input('Desea terminar? (y/n)').lower() == 'y':
            break
        
    #Se limpia la pantalla
    limpiar()
