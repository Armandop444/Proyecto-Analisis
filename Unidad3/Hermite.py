from Utilidades import tablita


def hermite(k: int, Xn: list, fx: list, dfx: list):
    #cargar los cabezeros de las columnas
    header = ["K","Zk","f(Zk)","f'(Zk)"]
    for _ in range(k-1):
        header.append("")
        
    tabla = tablita(header)
    return tabla.get_tabla()