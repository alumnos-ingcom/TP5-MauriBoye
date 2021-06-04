################
# Mauricio Boyé - @MauriBoye
# Ejercicio 3 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°3
"""
import tp5ej1, tp5ej2
    
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
    posicion = tp5ej2.ingreso_numero_entero_positivo("Posicion: ",3)
    valor = tribonacci(posicion)
    print(f"Valor = {valor}")
    
if __name__ == "__main__":
    prueba()