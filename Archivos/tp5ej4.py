################
# Mauricio Boyé - @MauriBoye
# Ejercicio 4 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°4
"""
import tp5ej1

def ingreso_numero_positivo(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero positivo.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
        if (entero > 0):
            return entero
        else:
            raise tp5ej1.IngresoIncorrecto(f"'{ingreso}' no es positivo!")
    except ValueError as err:
        raise tp5ej1.IngresoIncorrecto(f"'{ingreso}' no es un número!") from err

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
    if (suma_divisores == numero):
        return True
    else:
        return False
    
def prueba():
    tp5ej1.marco("numero_perfecto()")
    numero = ingreso_numero_positivo("Ingrese un numero: ")
    if (numero_perfecto(numero)):
        print(f"{numero} si es un numero perfecto")
    else:
        print(f"{numero} no es un numero perfecto")

if __name__ == "__main__":
    prueba()