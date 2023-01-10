# Reto #11
# ELIMINANDO CARACTERES
# Fecha publicación enunciado: 14/03/22
# Fecha publicación resolución: 21/03/22
# Dificultad: FÁCIL
#
# Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def funOut1(str1:str,str2:str):
    out = "" # new empty string to save the chars in str1 that aren't in str2
    for letter in str1: # for every char in str1:
        # if the char exists in str2, continue:
        if str2.find(letter) != -1: continue
        # if the char doesn't exist in str2, save it in string:
        else: out += letter
    if out: return out # if the string is not empty, returns it
    else: return "No quedan letras que cumplan esta condición" # if the string is empty, print this

def funOut2(str1:str,str2:str):
    out = "" # new empty string to save the chars in str1 that aren't in str2
    for letter in str2: # for every char in str2:
        # if the char exists in str2, continue:
        if str1.find(letter) != -1: continue
        # if the char doesn't exist in str2, save it in string:
        else: out += letter
    if out: return out # if the string is not empty, returns it
    else: return "No quedan letras que cumplan esta condición" # if the string is empty, print this

# asks for strings:
str1 = input("Introduce una cadena: ")
str2 = input("Introduce una segunda cadena: ")
# delete the characteres:
out1 = funOut1(str1,str2)
out2 = funOut2(str1,str2)
# result:
print("\nCaracteres presentes en la primera cadena que NO estaban en la segunda:\n",out1)
print("\nCaracteres presentes en la segunda cadena que NO estaban en la primera:\n",out2)