################
# Mauricio Boyé - @MauriBoye
# Ejercicio 2 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°2
"""
import tp5ej1

def ingreso_numero_entero_positivo(mensaje, numero_minimo=0):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero positivo.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
        if (entero >= numero_minimo):
            return entero
        else:
            raise tp5ej1.IngresoIncorrecto(f"'{ingreso}' no es "
                                           f"positivo y >= a {numero_minimo}")
    except ValueError as err:
        raise tp5ej1.IngresoIncorrecto(f"'{ingreso}' no es un número!") from err
    
def fibonacci(posicion):
    """
    Esta funcion devuelve un numero de una posicion
    determinada de la sucesion de fibonacci.
    """
    penutilmo = 1
    ultimo = 1
    sucesion = [1,1]
    i = 0
    while (posicion -1 > i):
        final = ultimo + penutilmo
        sucesion.append(final)
        penutilmo = final - penutilmo
        ultimo = final
        i = i + 1
    return sucesion[posicion]
    
def prueba():
    tp5ej1.marco("fibonacci()")
    print("Ingrese una posicion de la sucesión de fibonacci")
    posicion = ingreso_numero_entero_positivo("Posicion: ",2)
    valor = fibonacci(posicion)
    print(f"Valor = {valor}")
    
if __name__ == "__main__":
    prueba()