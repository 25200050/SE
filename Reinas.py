"""
Created on Sun Sep 11 20:01:22 2023

@author: isisa
"""

def tablero_seguro(tablero, fila, columna):
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
    
    
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
   
    for i, j in zip(range(fila, -1, -1), range(columna, len(tablero))):
        if tablero[i][j] == 1:
            return False
    
    return True

def resolver_cuatro_reinas(tablero, fila):
    if fila >= len(tablero):
        return True
    
    for columna in range(len(tablero)):
        if tablero_seguro(tablero, fila, columna):
            tablero[fila][columna] = 1

            if resolver_cuatro_reinas(tablero, fila + 1):
                return True
            
            tablero[fila][columna] = 0
    
    return False

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(['Q' if x == 1 else '.' for x in fila]))

def cuatro_reinas():
    n = 4
    tablero = [[0 for _ in range(n)] for _ in range(n)]

    if resolver_cuatro_reinas(tablero, 0):
        imprimir_tablero(tablero)
    else:
        print("No se encontró una solución.")

cuatro_reinas()