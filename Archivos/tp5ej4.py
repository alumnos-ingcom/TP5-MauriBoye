################
# Mauricio Boyé - @MauriBoye
# Ejercicio 4 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°4
"""
import tp5ej1, tp5ej2

def numero_perfecto(numero):
    """
    Esta funcion indica si un numero ingresado es un numero perfecto.
    """
    i = 1
    suma_divisores = 0
    while (i < numero):
        if (numero % i == 0):
            suma_divisores = suma_divisores + i
        i = i + 1
    return suma_divisores == numero
    
def prueba():
    tp5ej1.marco("numero_perfecto()")
    numero = tp5ej2.ingreso_numero_entero_positivo("Ingrese un numero: ",0)
    if (numero_perfecto(numero)):
        print(f"{numero} si es un numero perfecto")
    else:
        print(f"{numero} no es un numero perfecto")

if __name__ == "__main__":
    prueba()