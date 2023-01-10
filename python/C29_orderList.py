# Reto #29
# ORDENA LA LISTA
# Fecha publicación enunciado: 18/07/22
# Fecha publicación resolución: 26/07/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que ordene y retorne una matriz de números.
# - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional "Asc" o "Desc" para
# indicar si debe ordenarse de menor a mayor o de mayor a menor.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
# 
# Statement: Create a function that sorts and returns an array of numbers.
# - The function will receive a list (e.g. [2, 4, 6, 8, 9]) and an additional parameter "Asc" or "Desc" to
# to indicate whether it should be sorted from smallest to largest or from largest to smallest.
# - It is not possible to use the language's own functions to solve it automatically.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def sort(numbers, boolean):
	for i in range(0, len(numbers)):
		for j in range(1, len(numbers)):
			if ((numbers[j]<numbers[j-1]) if(boolean) else (numbers[j]>numbers[j-1])):
				aux = numbers[j]
				numbers[j] = numbers[j-1]
				numbers[j-1] = aux
	return numbers

print(sort([4, 6, 1, 8, 2], True)) # 1, 2, 4, 6, 8
print(sort([4, 6, 1, 8, 2], False)) # 8, 6, 4, 2, 1