################
# Mauricio Boyé - @MauriBoye
# Ejercicio 10 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°10
"""
import tp5ej1, tp5ej2

def conversion_binario(numero):
    """
    Esta funcion convierte un numero entero positivo en una
    cadena de texto con su conversion a binario
    """
    conversion = ""
    while numero >= 1:
        binario = numero%2
        numero = numero // 2
        conversion = str(binario) + conversion
    return conversion

def conversion_entero(numero):
    """
    Esta funcion convierte una cadena de texto de un numero
    binario en un numero entero
    """
    i = 0
    entero = 0
    digitos = []
    num_digito = int(numero)
    while num_digito !=0:
        digito = int(num_digito % 10)
        digitos.append(digito)
        num_digito=int(num_digito/10)
    while i < len(digitos):
        entero = entero + ((2**i)*digitos[i])
        i = i + 1
    return entero

def prueba():
    numero = tp5ej2.ingreso_numero_entero_positivo("Ingrese un numero: ",0)
    binario = conversion_binario(numero)
    entero = conversion_entero(binario)
    tp5ej1.marco("conversion_binario()")
    print(f"La conversion de {numero} a binario es {binario}")
    tp5ej1.marco("conversion_entero()")
    print(f"La conversion de {binario} a entero es {entero}")
    
if __name__ == "__main__":
    prueba()