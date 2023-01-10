# Reto #14
# ¿ES UN NÚMERO DE ARMSTRONG?
# Fecha publicación enunciado: 04/04/22
# Fecha publicación resolución: 11/04/22
# Dificultad: FÁCIL
#
# Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def isNarcisist(number):
    nDigits = countDigits(number) # counts the number of digits in "number"
    equal = 0 # to save the value of num
    for n in number: # equation:
        equal += int(n)**nDigits #*
    if int(number) == equal: return True #*
    return False
    #* need to convert to int() because "number" is a str()

def countDigits(number):
    count = 0
    for n in number:
        count += 1
    return count # returns number of digits

while True:
    try:
        num = input("Insert a number: ") # ask for a number
        assert(num.isnumeric()) # if it's not a number, raises an error
        break # to break the infinite loop
    except AssertionError: # if num wasn't a number, raises this error
        print("\nERROR: you must insert a number!\n")
result = isNarcisist(num) # calculates the result, num is sent as an str()
# result:
print("The number \"{0}\" is {1}.".format(num, "an Armstrong's number" if result else "not an Armstrong's number"))