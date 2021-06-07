################
# Mauricio Boyé - @MauriBoye
# Ejercicio 13 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°13
"""
import tp5ej1

def busqueda_palabra(texto, palabra):
    """
    Esta funcion pide el ingreso de un texto y una palabra,
    e indica la posicion de esta palabra dentro del texto
    si es que se encuentra dentro
    """
    i = 0
    k = 0
    j = 0
    lista_texto = []
    lista_palabra = []
    lista_palabra_texto = []
    while k < len(palabra):
        lista_palabra.append(palabra[k])
        k = k + 1
    while i < len(texto):
        if texto[i] != " ":
            lista_palabra_texto.append(texto[i])
        if texto[i] == " ":
            lista_texto.append(lista_palabra_texto)
            lista_palabra_texto = []
        i = i + 1
    lista_texto.append(lista_palabra_texto)
    while j < len(lista_texto):
        if lista_palabra == lista_texto[j]:
            return j
        j = j + 1
    raise tp5ej1.IngresoIncorrecto(f"La palabra '{palabra}' se ecuentra en el texto")
        
def prueba():
    tp5ej1.marco("busqueda_palabra()")
    texto = input("Ingrese un texto: ")
    palabra = input("Ingrese una palabra para buscar dentro del texto: ")
    posicion = busqueda_palabra(texto, palabra)
    print(f"La palabra '{palabra}' se ecuentra en la posición {posicion}")
    
if __name__ == "__main__":
    prueba()