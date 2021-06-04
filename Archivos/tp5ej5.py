################
# Mauricio Boyé - @MauriBoye
# Ejercicio 5 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°5
"""
import tp5ej1

def inversion_mayusculas(texto):
    i = 0
    inversion=""
    while i < len(texto):
        if ord(texto[i]) >= ord("a") and ord(texto[i]) <= ord("z"):
            inversion = inversion + chr(ord(texto[i]) - 32)
        elif ord(texto[i]) >= ord("A") and ord(texto[i]) <= ord("Z"):
            inversion = inversion + chr(ord(texto[i]) + 32)
        else:
            inversion = inversion + texto[i]
        i = i + 1
    return inversion

def prueba():
    tp5ej1.marco("inversion_mayusculas()")
    texto = input("Ingrese un texto: ")
    print(f"Inversion: {inversion_mayusculas(texto)}")

if __name__ == "__main__":
    prueba()