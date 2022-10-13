# Reto #22
# CONJUNTOS
# Fecha publicación enunciado: 01/06/22
# Fecha publicación resolución: 07/06/22
# Dificultad: FÁCIL
#
# Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def calculateSet(l1, l2, b):
    result = [] # empty list
    for item1 in l1:
        if not(b) and (item1 not in l2) and (item1 not in result): result.append(item1) # b = false
        for item2 in l2:
            if b and item2==item1 and not(item1 in result): result.append(item1) # b = true -> item1 == item2 (doesn't matter which one add)
            elif not(b) and (item2 not in l1) and (item2 not in result): result.append(item2) # b = false
    return result


print(calculateSet([1,2,3,3,4], [2,2,3,3,3,4,6], True))
print(calculateSet([1,2,3,3,4], [2,2,3,3,3,4,6], False))