# Reto #13
# FACTORIAL RECURSIVO
# Fecha publicación enunciado: 28/03/22
# Fecha publicación resolución: 04/04/22
# Dificultad: FÁCIL
#
# Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def factorial(f:int):
    if f == 1: return 1
    return f * factorial(f-1)

while(True): # infinite loop
    try:
        num = input("Introduce un número: ") # insert a number
        assert(num.isnumeric()) # if num is not a number, it'll raise an error
        print("{0}! = {1}".format(num, factorial(int(num)))) # result
        break # to break the infinite loop
    except AssertionError: # if num was not number, raises this error:
        print("\nERROR: debes introducir un número entero!\n")