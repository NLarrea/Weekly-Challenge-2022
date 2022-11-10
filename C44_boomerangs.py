# Reto #44
# BUMERANES
# Fecha publicación enunciado: 02/10/22
# Fecha publicación resolución: 07/11/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que retorne el número total de bumeranes de un array de números
# enteros e imprima cada uno de ellos.
# - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números seguidos, en el que el
#   primero y el último son iguales, y el segundo es diferente. Por ejemplo [2, 1, 2].
# - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).
# 
# Statement: Create a function that returns the total number of boomerangs from an array of integers and prints each of them.
# and prints each of them.
# - A boomerang is a sequence formed by 3 numbers in a row, where the first and the last one are the same, and the second one is different.
#   first and last are the same, and the second is different. For example [2, 1, 2].
# - In the array [2, 1, 2, 2, 3, 3, 3, 4, 2, 4] there are 2 boomerangs ([2, 1, 2] and [4, 2, 4]).
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def numberOfBoomerangs(numList):
	# if the length of the list is less than 3, it can't have any boomerangs
	if len(numList) < 3: return f"There are no bommerangs in {numList}, there should be at least 3 numbers!"
	counter = 0 # counts the total number of boomerangs
	i = 0 # index of the while loop
	while i < len(numList)-2:
		rNum = numList[i] # updates the value of rNum
		# if rNum is equal to the number 2 positions ahead of it -> counter++
		if numList[i+2] == rNum: counter += 1
		i += 1 # updates the index value -> important to avoid creating infinite loops
	return f"There {'is' if counter == 1 else 'are'} {counter} {'boomerang' if counter == 1 else 'boomerangs'} in {numList}"

print(numberOfBoomerangs([2, 1, 2, 3, 3, 4, 2, 4])) # There are 2 boomerangs in [2, 1, 2, 3, 3, 4, 2, 4]
print(numberOfBoomerangs([2, 1, 2, 1, 2])) # There are 3 boomerangs in [2, 1, 2, 1, 2]
print(numberOfBoomerangs([1, 2, 3, 4, 5])) # There are 0 boomerangs in [1, 2, 3, 4, 5]
print(numberOfBoomerangs([2, 2, 2, 2, 2])) # There are 3 boomerangs in [2, 2, 2, 2, 2]
print(numberOfBoomerangs([2, -2, 2, -2, 2])) # There are 3 boomerangs in [2, -2, 2, -2, 2]
print(numberOfBoomerangs([1, 2, 1])) # There is 1 boomerang in [1, 2, 1]
print(numberOfBoomerangs([2, -2])) # There are no bommerangs in [2, -2], there should be at least 3 numbers!
print(numberOfBoomerangs([2])) # There are no bommerangs in [2], there should be at least 3 numbers!
print(numberOfBoomerangs([])) # There are no bommerangs in [], there should be at least 3 numbers!