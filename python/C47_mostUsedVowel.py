# Reto #47
# VOCAL MÁS COMÚN
# Fecha publicación enunciado: 21/11/22
# Fecha publicación resolución: 28/11/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea un función que reciba un texto y retorne la vocal que más veces se repita.
# Si no hay vocales podrá devolver vacío.
# 
# Statement: Create a function that receives a text and returns the most repeated vowel.
# If there are no vowels it may return empty.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

""" def mostUsedVowel(text):
    # VARIABLES AND INITIALIZATION
    # list of vowels with their respective count
    VOWELS = [
        {"value": "a", "vowelOptions": ["a","á","à","ä","â"], "counter": 0},
        {"value": "e", "vowelOptions": ["e","é","è","ë","ê"], "counter": 0},
        {"value": "i", "vowelOptions": ["i","í","ì","ï","î"], "counter": 0},
        {"value": "o", "vowelOptions": ["o","ó","ò","ö","ô"], "counter": 0},
        {"value": "u", "vowelOptions": ["u","ú","ù","ü","û"], "counter": 0}
    ]
    text = text.lower() # convert text to lowercase

    # COUNT VOWELS
    # iterate over each character in the text and check if it is a vowel
    for char in text:
        for vowel in VOWELS:
            # if the character is a vowel, increase its counter
            if char in vowel["vowelOptions"]: vowel["counter"] += 1
    
    # CHECK WHICH VOWEL HAS THE HIGHEST COUNT
    # variables to store the most repeated vowel and its counter
    highest = 0
    highestValue = ""
    # iterate over each vowel in the list
    for i in range(0, len(VOWELS)):
        # if the vowel has a higher counter than the previous one, update the variables
        if VOWELS[i]["counter"] > highest:
            highest = VOWELS[i]["counter"]
            highestValue = VOWELS[i]["value"]
    
    # RESULT
    # if the highest counter is 0, return empty
    if highestValue == "": return "empty"
    # sort the list by counter (descending)
    VOWELS.sort(key = lambda x: x["counter"], reverse=True)
    # if the highest counter is equal to the second highest counter, return that there is no most repeated vowel
    if VOWELS[0]["counter"] == VOWELS[1]["counter"]: return "no vowels repeating more than others"
    # return the most repeated vowel
    return f'"{highestValue}"' """

import unicodedata

def mostUsedVowel(text):
    vowelCount = {} # dictionary to store the count of each vowel
    for char in unicodedata.normalize('NFD', text.lower()):
        if char in "aeiou":
            if char in vowelCount: vowelCount[f"{char}"] += 1
            else: vowelCount.setdefault(f"{char}", 1)
    mostRepeated = []
    maxRepeated = 0
    for vowel in vowelCount:
        count = vowelCount[vowel]
        if count >= maxRepeated:
            if count > maxRepeated: mostRepeated = []
            mostRepeated.append(vowel)
            maxRepeated = count
    return mostRepeated if mostRepeated else "There are no vowels"

print(mostUsedVowel("Hello")) # ['e', 'o']
print(mostUsedVowel("ghdjf")) # "There are no vowels"
print(mostUsedVowel("Hello World")) # ['o']
print(mostUsedVowel("This is a good day")) # ['i', 'a', 'o']
print(mostUsedVowel("Hola, ¿qué tal estás hoy?")) # ['a']