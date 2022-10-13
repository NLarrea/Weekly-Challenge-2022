# Reto #19
# CONVERSOR TIEMPO
# Fecha publicación enunciado: 09/05/22
# Fecha publicación resolución: 16/05/22
# Dificultad: FACIL
#
# Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def timeToMillis(days,hours,mins,secs):
    daysToMillis = days * 24 * 60 * 60 * 1000
    hoursToMillis = hours * 60 * 60 * 1000
    minsToMillis = mins * 60 * 1000
    secsToMillis = secs * 1000
    return daysToMillis + hoursToMillis + minsToMillis + secsToMillis

print(timeToMillis(0,0,0,10))
print(timeToMillis(2,5,-45,10))
print(timeToMillis(2000000000,5,45,10))