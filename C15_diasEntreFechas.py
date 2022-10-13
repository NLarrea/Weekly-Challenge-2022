# Reto #15
# ¿CUÁNTOS DÍAS?
# Fecha publicación enunciado: 11/04/22
# Fecha publicación resolución: 18/04/22
# Dificultad: DIFÍCIL
#
# Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
#
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

import datetime # import to use the date types and modules

def formatChecker(dateStr:str):
    i = 0
    while(i<len(dateStr)):
        if (i==2 or i==5) and dateStr[i]!='/': return False
        if (i!=2 and i!=5) and (dateStr[i]<'0' or dateStr[i]>'9'): return False
        i += 1
    return True

def insertData():
    while True: # repeats in case of an error
        try:
            inputData = input("Write one date with the following format: dd/MM/yyyy\n")
            ans = formatChecker(inputData) # checks the format
            assert(ans) # raises an error if the format is not correct
            inputData = inputData.split('/') # splits the string in three parts
            date = datetime.datetime(int(inputData[2]), int(inputData[1]), int(inputData[0])) # creates a new datetime
            return date # returns the date
        except AssertionError: # if the format wasn't correct, raises this error
            print("\nERROR: that is not the correct format!\n")
        except ValueError: # if the value of the date is not correct (example: day = 35), raises this error
            print("\nERROR: that is not a possible date!\n")

date1 = insertData() # asks the first date
date2 = insertData() # asks the second date
date3 = abs(date1 - date2).days # calculates de difference in days
date1 = date1.strftime("%d/%m/%Y") # changes the format to "date1" output
date2 = date2.strftime("%d/%m/%Y") # changes the format to "date2" output
# prints the result:
print("Between \"{0}\" and \"{1}\" {2} {3} {4}".format(date1, date2, ("are" if date3>1 else "is"), date3, ("days" if date3>1 else "day")))