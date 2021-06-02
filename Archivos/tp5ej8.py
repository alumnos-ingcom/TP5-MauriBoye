################
# Mauricio Boyé - @MauriBoye
# Ejercicio 8 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°8
"""
import tp5ej1

def cifrado_cesar(texto, rotado):
    """
    Esta funcion devuelve un texto cifrado una
    cantidad de caracteres determinado.
    """
    texto_cifrado = []
    texto_cifrado_caracteres = []
    i = 0
    while i < len(texto):
        if (ord(texto[i])+int(rotado)) <= 122:
            texto_cifrado.append(ord(texto[i])+int(rotado))
            texto_cifrado_caracteres.append(chr(texto_cifrado[i]))
        if (ord(texto[i])+int(rotado)) > 122:
            texto_cifrado.append(ord(texto[i])+int(rotado)-58)
            texto_cifrado_caracteres.append(chr(texto_cifrado[i]))
        i = i + 1
    cifrado = [texto_cifrado, texto_cifrado_caracteres]
    return cifrado
    
def descifrado_cesar(texto_cifrado, rotado):
    """
    Esta funcion devuelve un texto descifrado una
    cantidad de caracteres determinado.
    """
    texto_descifrado = []
    texto_descifrado_unicode = []
    i = 0
    while i < len(texto_cifrado):
        if (texto_cifrado[i])-int(rotado) <= 65:
            texto_descifrado.append(chr(texto_cifrado[i]-int(rotado)+58))
            texto_descifrado_unicode.append(ord(texto_descifrado[i]))
        if (texto_cifrado[i])-int(rotado) > 65:
            texto_descifrado.append(chr(texto_cifrado[i]-int(rotado)))
            texto_descifrado_unicode.append(ord(texto_descifrado[i]))
        i = i + 1
    descifrado = [texto_descifrado, texto_descifrado_unicode]
    return descifrado

def prueba():
    texto = input("Ingrese un texto: ")
    rotado = input("Ingrese la cantidad de caracteres rotados: ")
    texto_cifrado, texto_cifrado_caracteres = cifrado_cesar(texto, rotado)
    texto_descifrado, texto_descifrado_unicode = descifrado_cesar(texto_cifrado, rotado)
    tp5ej1.marco("cifrado_cesar()")
    print(f"{texto_cifrado}={texto_cifrado_caracteres}")
    tp5ej1.marco("descifrado_cesar()")
    print(f"{texto_descifrado}={texto_descifrado_unicode}")

if __name__ == "__main__":
    prueba()