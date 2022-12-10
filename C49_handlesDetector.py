# Reto #49
# EL DETECTOR DE HANDLES
# Fecha publicación enunciado: 05/11/22
# Fecha publicación resolución: 12/12/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente
# Expresiones Regulares.
# Debes crear una expresión regular para cada caso:
# - Handle usuario: Los que comienzan por "@"
# - Handle hashtag: Los que comienzan por "#"
# - Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

import re

def handleDetector(text):
    # regular expressions
    users = r"^@[A-z0-9\.\-\_]*"
    hashtags = r"^#[A-z0-9]*"
    web1 = r"(?:https:\/\/)[A-z0-9\.]*"
    web2 = r"(?:^http:\/\/)[A-z0-9\.]*"
    web3 = r"(?:^www\.)[A-z0-9\.]*"

    # create list with the items to check
    textList = text.split(", ")
    
    # empty list to save the matchess
    matches = []

    # check if they match and save the matched item in a list
    for item in textList:
        if re.findall(users, item) or re.findall(hashtags, item) or re.findall(web1, item) or re.findall(web2, item) or re.findall(web3, item):
            matches.append(item)
    
    return matches if matches else f"There are no matches in the following text:\n\t'{text}'"

# SOME EXAMPLES

USER_LIST = "@NLarrea, @n.loust, wef@user, @user123, 123user@";
HASHTAG_LIST = "#octoverse, #javascript, this#not, not#hashtag, lastTry#";
WEB_LIST = "https://github.com, https:/github.com, http://google.es, www.codedex.io, www.toptal.com";
POPURRI = "@nloust_, n@larrea, www.github.com, ww.github.com, github.www.com, #awesome, https;//nothing"

print(handleDetector(USER_LIST)) # [ '@NLarrea', '@n.loust', '@user123' ]
print(handleDetector(HASHTAG_LIST)) # [ '#octoverse', 'javascript' ]
print(handleDetector(WEB_LIST)) # [ 'https://github.com', 'http://google.es', 'www.codedex.io', 'www. toptal.com' ]
print(handleDetector(POPURRI)) # [ '@nloust_', 'www.github.com', '#awesome' ]
print(handleDetector("In this text there are no matches at all"))