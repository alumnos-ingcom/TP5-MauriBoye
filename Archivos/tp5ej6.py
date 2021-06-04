################
# Mauricio Boyé - @MauriBoye
# Ejercicio 6 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°6
"""
import tp5ej1
    
def caracteres_balanceados(cadena, abrir, cerrar):
    """
    Esta funcion indica si una cadena de caracteres esta balanceada
    """
    caracteres_abierto = 0
    caracteres_cerrado = 0
    i = 0
    while i < len(cadena):
        if (cadena[0] == cerrar):
            caracteres_cerrado = caracteres_cerrado + 1
            break
        if (cadena[i] == abrir):
            caracteres_abierto = caracteres_abierto + 1
        if (cadena[i] == cerrar):
            caracteres_cerrado = caracteres_cerrado + 1
        i = i + 1
    if caracteres_abierto == caracteres_cerrado:
        return True
    else:
        return False

def prueba():
    tp5ej1.marco("caracteres_balanceados()")
    cadena = input("Ingrese una cadena de caracteres: ")
    if caracteres_balanceados(cadena, abrir="[", cerrar="]"):
        print(f"Los caracteres '{cadena}' estan balanceados")
    else:
        print(f"Los caracteres '{cadena}' no estan balanceados")

if __name__ == "__main__":
    prueba()