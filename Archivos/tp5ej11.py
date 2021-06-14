################
# Mauricio Boyé - @MauriBoye
# Ejercicio 11 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°11
"""
import tp5ej1

def promedio_movil(lista_numeros_enteros, cantidad_valores):
    i = 0
    cantidad_valores = int(cantidad_valores)
    if cantidad_valores < len(lista_numeros_enteros) and cantidad_valores > 0:
        lista_promedio_movil = []
        while i <= (len(lista_numeros_enteros)-cantidad_valores):
            k = 0
            promedio_movil = 0
            while k < cantidad_valores:
                promedio_movil = promedio_movil + lista_numeros_enteros[k+i]
                k = k + 1
            promedio_movil = promedio_movil/cantidad_valores
            lista_promedio_movil.append(promedio_movil)
            i = i + 1
    elif cantidad_valores <= 0:
        raise tp5ej1.IngresoIncorrecto("La cantidad de valores para promediar es "
                                "menor o igual a '0'")
    else:
        raise tp5ej1.IngresoIncorrecto("La cantidad de valores para promediar es "
                                "mayor a la cantidad de elementos de la lista")
    return lista_promedio_movil
    
def prueba():
    tp5ej1.marco("promedio_movil()")
    lista_numeros_enteros = [12,43,23,4,22,7]
    cantidad_valores = input("Ingrese la cantidad de valores: ")
    lista_promedio_movil = promedio_movil(lista_numeros_enteros, cantidad_valores)
    print(lista_promedio_movil)
    
if __name__ == "__main__":
    prueba()