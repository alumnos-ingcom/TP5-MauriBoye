################
# Mauricio Boyé - @MauriBoye
# Ejercicio 14 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°14
"""
import tp5ej1, tp5ej2

def numero_entero_capicua(numero):
    """
    Esta funcion indica si un numero es capicua
    """
    a = 0
    b = -1
    lista_digito = []
    lista_capicua = []
    num_digito = int(numero)
    while num_digito !=0:
        digito = int(num_digito % 10)
        lista_digito.append(digito)
        lista_capicua.insert(0,digito)
        num_digito=int(num_digito/10)
    return lista_capicua == lista_digito      

def prueba():
    tp5ej1.marco("numero_entero_capicua()")
    numero = tp5ej2.ingreso_numero_entero_positivo("ingrese un numero: ")
    resultado = numero_entero_capicua(numero)
    if resultado:
        print(f"El numero '{numero}' es capicua")
    else:
        print(f"El numero '{numero}' no es capicua")
    
if __name__ == "__main__":
    prueba()