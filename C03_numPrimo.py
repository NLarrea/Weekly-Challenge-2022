# Reto #3
# ¿ES UN NÚMERO PRIMO?
# Fecha publicación enunciado: 17/01/22
# Fecha publicación resolución: 24/01/22
# Dificultad: MEDIA
#
# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

# Función para determinar si un número es primo:
def esPrimo(num):
    i = 1
    while i<num:
        if num%i == 0 and i>1: # si un número es divisible por otro que no sea "1", no es primo
            return False
        i += 1
    return True # si no ha sido divisible por ninguno, es primo

# Creamos una lista con numeros del 1 al 100:
listaNumeros = list(range(1,101)) 
# Comprobamos que el numero sea un numero primo y si lo es, lo mostramos:
for number in listaNumeros:
    if esPrimo(number) and number!=1:
        print(number)