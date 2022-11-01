# Reto #31
# AÑOS BISIESTOS
# Fecha publicación enunciado: 01/08/22
# Fecha publicación resolución: 08/08/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
# - Utiliza el menor número de líneas para resolver el ejercicio.
# 
# Statement: Create a function that prints the next 30 leap years following a given one.
# - Use the least number of lines to solve the exercise.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def print30leapYears(year):
	printed = 0 # to count how many years are printed
	i = 0 # to update the current year
	while printed < 30:
		# check if the year is a leap year or not
		if (year+i) % 4 == 0 and ((year+i) % 400 == 0 or (year+i) % 100 != 0):
			print("{0}: {1}".format(printed+1, year+i)) # if it is -> prints the number and the year
			printed += 1 # updates the printed value
		i += 1 # to avoid creating an infinite loop and jump to next year

print30leapYears(1999)
print30leapYears(-500)