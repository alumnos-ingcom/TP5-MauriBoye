################
# Mauricio Boyé - @MauriBoye
# Ejercicio 6 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°6
"""
import tp5ej1

def ingreso_tipo_caracter(mensaje):
    """
    Esta funcion pide el ingreso de una pareja(2) de caracteres
    """
    caracter = input(mensaje)
    if len(caracter) == 2:
        return caracter
    else:
        raise tp5ej1.IngresoIncorrecto(f"'{caracter}' no es un "
                                       "par de caracateres!")
    
def caracteres_balanceados(cadena, caracter):
    """
    Esta funcion indica si una cadena de caracteres esta balanceada
    """
    caracteres_abierto = 0
    caracteres_cerrado = 0
    i = 0
    while i < len(cadena):
        if (cadena[0] == caracter[1]):
            caracteres_cerrado = caracteres_cerrado + 1
            break
        if (cadena[i] == caracter[0]):
            caracteres_abierto = caracteres_abierto + 1
        if (cadena[i] == caracter[1]):
            caracteres_cerrado = caracteres_cerrado + 1
        i = i + 1
    if caracteres_abierto == caracteres_cerrado:
        return True
    else:
        return False

def prueba():
    tp5ej1.marco("caracteres_balanceados()")
    caracter = ingreso_tipo_caracter("Ingrese el tipo de "
                                     "pares de caracteres: ")
    cadena = input("Ingrese una cadena de caracteres: ")
    if caracteres_balanceados(cadena, caracter):
        print(f"Los caracteres '{cadena}' estan balanceados")
    else:
        print(f"Los caracteres '{cadena}' no estan balanceados")

if __name__ == "__main__":
    prueba()