# Reto #32
# EL SEGUNDO
# Fecha publicación enunciado: 08/08/22
# Fecha publicación resolución: 15/08/22
# Dificultad: FÁCIL
#
# Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

lista = [1,4,23,98,56,43,76,12,7]
lista.sort()
print(lista[len(lista)-2])