################
# Mauricio Boyé - @MauriBoye
# Ejercicio 3 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°3
"""
import tp5ej1

def ingreso_numero_entero_positivo(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero positivo.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
        if (entero >= 3):
            return entero
        else:
            raise tp5ej1.IngresoIncorrecto(f"'{ingreso}' no es "
                                           "positivo y >= 3")
    except ValueError as err:
        raise tp5ej1.IngresoIncorrecto(f"'{ingreso}' no es un número!") from err
    
def tribonacci(posicion):
    """
    Esta funcion devuelve un numero de una posicion
    determinada de la sucesion de tribonacci.
    """
    antepenultimo = 1
    penutilmo = 1
    ultimo = 1
    sucesion = [1,1,1]
    i = 0
    while (posicion -2 > i):
        final = ultimo + penutilmo + antepenultimo
        sucesion.append(final)
        antepenultimo = final - penutilmo - antepenultimo
        penutilmo = final - penutilmo - antepenultimo
        ultimo = final
        i = i + 1
    return sucesion[posicion]

def prueba():
    tp5ej1.marco("tribonacci()")
    print("Ingrese una posicion de la sucesión de tribonacci")
    posicion = ingreso_numero_entero_positivo("Posicion: ")
    print(f"Valor = {tribonacci(posicion)}")
    
if __name__ == "__main__":
    prueba()