# Reto #6
# INVIRTIENDO CADENAS
# Fecha publicación enunciado: 07/02/22
# Fecha publicación resolución: 14/02/22
# Dificultad: FÁCIL
#
# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

cadena = input("Introduce una cadena de texto: ")
invertida = ""
i = len(cadena)-1
while i>=0:
    invertida += cadena[i]
    i -= 1
invertida += '\0'
print(invertida)