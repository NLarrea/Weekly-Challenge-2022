# Reto #8
# DECIMAL A BINARIO
# Fecha publicación enunciado: 18/02/22
# Fecha publicación resolución: 02/03/22
# Dificultad: FÁCIL
#
# Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def decimalToBinary(num:int):
    t = []
    a = num
    i = 0
    # Convertimos el número a binario y lo guardamos en una tabla:
    while a != 0:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            b = int(a % 2)
            a = int(a / 2)
            t.append(b) # añadimos el resto a la tabla
            i += 1
    # Reordenamos la tabla creada:
    invertedList = t[::-1]
    # Convertimos los datos de la tabla invertida en un número entero:
    j = 0
    number = 0
    while j<i:
        number *= 10
        number += invertedList[j]
        j += 1
    return number

while(True):
    try:
        number = input("Introduce un número entero: ")
        assert(number.isnumeric()) # si no es un número, dará error
        print("El número {0} en binario es: {1}".format(number,decimalToBinary(int(number))))
        break
    except AssertionError:
        print("\nERROR: debes introducir un número ENTERO!\n")