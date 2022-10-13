# Reto #20
# PARANDO EL TIEMPO
# Fecha publicación enunciado: 16/05/22
# Fecha publicación resolución: 23/05/22
# Dificultad: MEDIA
#
# Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
# - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
# - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

import time # to wait X seconds

def sum(n1, n2, waitTime):
    res = n1 + n2
    time.sleep(waitTime) # waits "waitTime" seconds
    return res

try:
    num1 = input("Set a first number: ")
    assert(num1.isnumeric())
    num2 = input("Set a second number: ")
    assert(num2.isnumeric())
    sec = input("Set the seconds you want to wait: ")
except AssertionError:
    print("ERROR: you should set a number")
print(sum(int(num1), int(num2), int(sec)))