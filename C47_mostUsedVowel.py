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

def mostUsedVowel(text):
    # VARIABLES AND INITIALIZATION
    # list of vowels with their respective count
    VOWELS = [
        {"value": "a", "vowel": ["a","á","à","ä","â"], "counter": 0},
        {"value": "e", "vowel": ["e","é","è","ë","ê"], "counter": 0},
        {"value": "i", "vowel": ["i","í","ì","ï","î"], "counter": 0},
        {"value": "o", "vowel": ["o","ó","ò","ö","ô"], "counter": 0},
        {"value": "u", "vowel": ["u","ú","ù","ü","û"], "counter": 0}
    ]
    text = text.lower() # convert text to lowercase

    # COUNT VOWELS
    # iterate over each character in the text
    for char in text:
        # if the character is a vowel, increase the counter
        if char in VOWELS[0]["vowel"]: VOWELS[0]["counter"] += 1
        elif char in VOWELS[1]["vowel"]: VOWELS[1]["counter"] += 1
        elif char in VOWELS[2]["vowel"]: VOWELS[2]["counter"] += 1
        elif char in VOWELS[3]["vowel"]: VOWELS[3]["counter"] += 1
        elif char in VOWELS[4]["vowel"]: VOWELS[4]["counter"] += 1
    
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
    return f'"{highestValue}"'

print(mostUsedVowel("Hello")) # "no vowels repeating more than others"
print(mostUsedVowel("ghdjf")) # "empty"
print(mostUsedVowel("Hello World")) # "o"
print(mostUsedVowel("This is a good day")) # "no vowels repeating more than others"
print(mostUsedVowel("Hola, ¿qué tal estás hoy?")) # "a"