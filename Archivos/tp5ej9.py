################
# Mauricio Boyé - @MauriBoye
# Ejercicio 9 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°9
"""
import tp5ej1

def factoriales(maximo):
    """
    Esta funcion devuelve una lista de los factoriales
    menores a 1.499.999
    """
    i = 1
    numero = 1
    factorial = 1
    lista_factoriales = []
    while factorial <= maximo:
        lista_factoriales.append(factorial)
        while i < numero:
            factorial =  factorial * i
            i = i + 1
        numero = numero + 1
    del lista_factoriales[0]
    return lista_factoriales
    
def factoriones(lista):
    """
    Esta funcion devuelve una lista de los factoriones
    menores a 1.499.999
    """
    numero = 1
    maximo = 1_499_999
    factorion = 0
    lista_factoriones = []
    while numero < maximo:
        num_digito = numero
        while num_digito !=0:
            digito = int(num_digito % 10)
            factorion = factorion + lista[digito]
            num_digito=int(num_digito/10)
        if factorion == numero:
            lista_factoriones.append(factorion)
        factorion = 0
        numero = numero + 1
    return lista_factoriones

def prueba():
    tp5ej1.marco("factoriones()")
    lista_factorial = factoriales(1_499_999)
    lista_factorion = factoriones(lista_factorial)
    print(f"Los factoriones menores a 1.499.999 son: {lista_factorion}")
    
if __name__ == "__main__":
    prueba()