# Reto #16
# EN MAYÚSCULA
# Fecha publicación enunciado: 18/04/22
# Fecha publicación resolución: 25/04/22
# Dificultad: FÁCIL
#
# Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def capitalize(txt):
    result = ""
    nextIsUpper = True # because the first char is always uppercase
    for char in txt:
        if nextIsUpper: result += char.upper() # adds char uppercase to result
        else: result += char # adds char to result
        nextIsUpper = char in "'.,;:?!¿¡ " # checks if char is special char because next one must be uppercase
    return result

# three random strings to convert:
text1 = "¿hola qué tal estás?"
text2 = "¿hola      qué tal estás?"
text3 = "El niño ñoño"
# capitalizes the first char of every words:
print(capitalize(text1))
print(capitalize(text2))
print(capitalize(text3))