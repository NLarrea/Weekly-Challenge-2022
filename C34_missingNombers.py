# Reto #34
# LOS NÚMEROS PERDIDOS
# Fecha publicación enunciado: 22/08/22
# Fecha publicación resolución: 29/08/22
# Dificultad: FÁCIL
# 
# Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule
# y retorne todos los que faltan entre el mayor y el menor.
# - Lanza un error si el array de entrada no es correcto.
# 
# Statement: Given a sorted array of integers with no repeats, create a function that computes
# and returns all missing integers between the largest and the smallest.
# - Throws an error if the input array is not correct.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def isSorted(arr):
	arrToCompare = []
	for number in arr: arrToCompare.append(number)
	arrToCompare.sort()
	# check if both arrays are equals
	equals = True
	for i in range(0, len(arr)):
		if arr[i] != arrToCompare[i]: equals = False
	if not equals:
		equals = True
		arrToCompare.sort(reverse=True)
		for i in range(0, len(arr)):
			if arr[i] != arrToCompare[i]: equals = False
	return equals

def lostNumbers(arr):
	# check if the array has repeating numbers
	for i in range(0,len(arr)):
		for j in range(i+1, len(arr)):
			assert (not (arr[j] == arr[i])), "This array has repeated numbers!"
			continue
	# check if the array is sorted
	sortedArr = isSorted(arr)
	if not sortedArr: assert(sortedArr), "This array is not sorted!"
	# create a new array with the result
	newArr = [] # empty list
	# if array is sorted from smallest to largest
	if arr[0] < arr[len(arr)-1]: 
		for number in range(arr[0], arr[len(arr)-1]+1): # positive step (default)
			newArr.append(number)
	# if array is sorted from largest to smallest
	else:
		for number in range(arr[0], arr[len(arr)-1]-1, -1): # negative step
			newArr.append(number)
	# return the result
	return newArr

print(lostNumbers([1, 3, 5])) # [ 1, 2, 3, 4, 5 ]
print(lostNumbers([5, 3, 1])) # [ 5, 4, 3, 2, 1 ]
print(lostNumbers([5, 1])) # [ 5, 4, 3, 2, 1 ]
print(lostNumbers([-5, 1])) # [ -5, -4, -3, -2, -1, 0, 1 ]
#print(lostNumbers([1, 3, 3, 5])) # AssertionError: This array has repeated numbers!
#print(lostNumbers([5, 7, 1])) # AssertionError: This array is not sorted!
#print(lostNumbers([10, 7, 7, 1])) # AssertionError: This array has repeated numbers!