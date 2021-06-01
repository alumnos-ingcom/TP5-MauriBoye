################
# Mauricio Boyé - @MauriBoye
# Ejercicio 1 - TP N°5
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Ejercicio N°1
"""

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_numero_entero(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto(f"'{ingreso}' no es un número!") from err
    return entero

def numero_par_impar(numero):
    """
    Esta funcion indica si el numero evaluado es par o impar.
    """
    if (numero >= 0):
        while (numero > 1):
            if (numero >= 2):
                numero = numero - 2
        if (numero == 0):
            return True
        elif (numero == 1):
            return False
    if (numero < 0):
        while (numero < -1):
            if (numero <= -2):
                numero = numero + 2
        if (numero == 0):
            return True
        elif (numero == -1):
            return False
        
def marco(texto):
    """
    Esta funcion crea un marco a un texto deseado
    """
    print("\n"+"╴"*80)
    print("╔"+"═"*len(texto)+"╗")
    print(f"║{texto}║")
    print("╚"+"═"*len(texto)+"╝")
    print("╴"*80)
    
def prueba():
    marco("numero_par_impar()") 
    numero = ingreso_numero_entero("Ingrese un numero: ")
    resultado = numero_par_impar(numero)
    if (resultado):
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

if __name__ == "__main__":
    prueba()