# Reto #0
# EL FAMOSO "FIZZ BUZZ"
# Fecha publicacion enunciado: 27/12/21
# Fecha publicacion resolucion: 03/01/22
# Dificultad: FACIL
# Enunciado: Escribe un programa que muestre por consola (con un print) los n�meros de 1 a 100 (ambos incluidos y con un salto de l�nea entre cada impresi�n), sustituyendo los siguientes:
# - Multiplos de 3 por la palabra "fizz".
# - Multiplos de 5 por la palabra "buzz".
# - Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

for number in range(1,101): # range(i,j) -> cuenta desde i hasta j-1
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)