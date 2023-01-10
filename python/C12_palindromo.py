# Reto #12
# ¿ES UN PALÍNDROMO?
# Fecha publicación enunciado: 21/03/22
# Fecha publicación resolución: 28/03/22
# Dificultad: MEDIA
#
# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

# dictionary with the characters we want to erase:
charList = [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/"]

def esPalindromo(phrase:str):
    newStr = removeChars(phrase) # removes some chars
    newStr = newStr.lower() # lowercase every sentence
    invertedStr = "" # empty string
    i = len(newStr)-1
    while(i>=0):
        invertedStr += newStr[i]
        i -= 1
    if invertedStr == newStr: return True
    else: return False

def removeChars(string:str):
    i = 0
    for c in charList:
        string = string.replace(c,"") # removes the character from the charList
    while i < len(string):
        if string[i] == "á": string[i] = "a" # changes 'á' to 'a'
        elif string[i] == "é": string[i] = "e" # changes 'é' to 'e'
        elif string[i] == "í": string[i] = "i" # changes 'í' to 'i'
        elif string[i] == "ó": string[i] = "o" # changes 'ó' to 'o'
        elif string[i] == "ú": string[i] = "u" # changes 'ú' to 'u'
        i += 1
    return string

phrase = str(input("Introdue a text: "))
result = esPalindromo(phrase)
print("El texto \"{0}\" {1}".format(phrase, "es paíndromo" if result else "no es palíndromo"))