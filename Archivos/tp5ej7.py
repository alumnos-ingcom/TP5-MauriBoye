################
# Mauricio Boyé - @MauriBoye
# Ejercicio 7 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°7
"""
import tp5ej1

def ingreso_numero_flotante(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número flotante.
    """
    ingreso = input(mensaje)
    try:
        flotante = float(ingreso)
    except ValueError as err:
        raise tp5ej1.IngresoIncorrecto(f"'{ingreso}' no es un número!") from err
    return flotante

def distancia(puntoA, puntoB):
    """
    Esta funcion muestra la distancia entre dos puntos
    """
    if puntoB >= puntoA:
        distancia = puntoB - puntoA
    if puntoB < puntoA:
        distancia = puntoA - puntoB
    return distancia

def prueba():
    tp5ej1.marco("distancia()")
    puntoA = ingreso_numero_flotante("Ingrese el punto A del recorrido: ")
    puntoB = ingreso_numero_flotante("Ingrese el punto B del recorrido: ")
    total = distancia(puntoA, puntoB)
    if puntoB >= puntoA:
        print(f"La distancia entre {puntoA} y {puntoB} es {total}")
    if puntoB < puntoA:
        print(f"La distancia entre {puntoB} y {puntoA} es {total}")
    
if __name__ == "__main__":
    prueba()