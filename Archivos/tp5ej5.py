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
        if texto[i] == "a":
            inversion = inversion + "A"
        elif texto[i] == "b":
            inversion = inversion + "B"
        elif texto[i] == "c":
            inversion = inversion + "C"
        elif texto[i] == "d":
            inversion = inversion + "D"
        elif texto[i] == "e":
            inversion = inversion + "E"
        elif texto[i] == "f":
            inversion = inversion + "F"
        elif texto[i] == "g":
            inversion = inversion + "G"
        elif texto[i] == "h":
            inversion = inversion + "H"
        elif texto[i] == "i":
            inversion = inversion + "I"
        elif texto[i] == "j":
            inversion = inversion + "J"
        elif texto[i] == "k":
            inversion = inversion + "K"
        elif texto[i] == "l":
            inversion = inversion + "L"
        elif texto[i] == "m":
            inversion = inversion + "M"
        elif texto[i] == "e":
            inversion = inversion + "E"
        elif texto[i] == "n":
            inversion = inversion + "N"
        elif texto[i] == "ñ":
            inversion = inversion + "Ñ"
        elif texto[i] == "o":
            inversion = inversion + "O"
        elif texto[i] == "p":
            inversion = inversion + "P"
        elif texto[i] == "q":
            inversion = inversion + "Q"
        elif texto[i] == "r":
            inversion = inversion + "R"
        elif texto[i] == "s":
            inversion = inversion + "S"
        elif texto[i] == "t":
            inversion = inversion + "T"
        elif texto[i] == "u":
            inversion = inversion + "U"
        elif texto[i] == "v":
            inversion = inversion + "V"
        elif texto[i] == "w":
            inversion = inversion + "W"
        elif texto[i] == "x":
            inversion = inversion + "X"
        elif texto[i] == "y":
            inversion = inversion + "Y"
        elif texto[i] == "z":
            inversion = inversion + "Z"
        elif texto[i] == "A":
            inversion = inversion + "a"
        elif texto[i] == "B":
            inversion = inversion + "b"
        elif texto[i] == "B":
            inversion = inversion + "c"
        elif texto[i] == "D":
            inversion = inversion + "d"
        elif texto[i] == "E":
            inversion = inversion + "e"
        elif texto[i] == "F":
            inversion = inversion + "f"
        elif texto[i] == "G":
            inversion = inversion + "g"
        elif texto[i] == "H":
            inversion = inversion + "h"
        elif texto[i] == "I":
            inversion = inversion + "i"
        elif texto[i] == "J":
            inversion = inversion + "j"
        elif texto[i] == "K":
            inversion = inversion + "k"
        elif texto[i] == "L":
            inversion = inversion + "l"
        elif texto[i] == "M":
            inversion = inversion + "m"
        elif texto[i] == "E":
            inversion = inversion + "e"
        elif texto[i] == "N":
            inversion = inversion + "n"
        elif texto[i] == "Ñ":
            inversion = inversion + "ñ"
        elif texto[i] == "O":
            inversion = inversion + "o"
        elif texto[i] == "P":
            inversion = inversion + "p"
        elif texto[i] == "Q":
            inversion = inversion + "q"
        elif texto[i] == "R":
            inversion = inversion + "r"
        elif texto[i] == "S":
            inversion = inversion + "s"
        elif texto[i] == "T":
            inversion = inversion + "t"
        elif texto[i] == "U":
            inversion = inversion + "u"
        elif texto[i] == "V":
            inversion = inversion + "v"
        elif texto[i] == "W":
            inversion = inversion + "w"
        elif texto[i] == "X":
            inversion = inversion + "x"
        elif texto[i] == "Y":
            inversion = inversion + "y"
        elif texto[i] == "Z":
            inversion = inversion + "z"
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