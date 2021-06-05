################
# Mauricio Boyé - @MauriBoye
# Ejercicio 12 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°12
"""
import random, tp5ej1, tp5ej2

def lista_aleatoria(cantidad_listas, cantidad_caracteres):
    k = 0
    lista = []
    while k < cantidad_listas:
        nueva_lista_aleatoria=[]
        for i in range(cantidad_caracteres):
            nueva_lista_aleatoria.append(chr(random.randint(ord("A"),ord("z"))))
        lista.append(nueva_lista_aleatoria)
        k = k + 1
    return lista

def comparacion_lista(lista1, lista2):
    i = 0
    suma1 = 0
    suma2 = 0
    while i < len(lista1):
        suma1 = suma1 + ord(str(lista1[i]))
        i = i + 1
    i = 0
    while i < len(lista2):
        suma2 = suma2 + ord(str(lista2[i]))
        i = i + 1
    return suma1 == suma2

def prueba():
    tp5ej1.marco("comparacion_lista()")
    cantidad_caracteres = tp5ej2.ingreso_numero_entero_positivo("Ingrese la cantidad"
                                               " de elementos para el par de listas: ",0)
    lista1, lista2 = lista_aleatoria(2, cantidad_caracteres)
    if comparacion_lista(lista1, lista2):
        print(f"Las listas {lista1} y {lista2} son iguales")
    else:
        print(f"Las listas {lista1} y {lista2} no son iguales")
        
if __name__ == "__main__":
    prueba()