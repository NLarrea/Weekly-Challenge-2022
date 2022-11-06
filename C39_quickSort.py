# Reto #39
# TOP ALGORITMOS: QUICK SORT
# Fecha publicación enunciado: 27/09/22
# Fecha publicación resolución: 03/10/22
# Dificultad: MEDIA
# 
# Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",
# creado por C.A.R. Hoare.
# 	- Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a 
# 	mejorar nuestro conocimiento sobre ingeniería de software. Dedícale tiempo a entenderlo,
# 	no únicamente a copiar su implementación.
# 	- Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos
# 	los más famosos de la historia.
# 
# Statement: Implements one of the most famous sorting algorithms: the "Quick Sort",
# created by C.A.R. Hoare.
# 	- Understanding the operation of the most used algorithms in history helps us to improve our knowledge of software engineering. 
# 	improve our knowledge of software engineering. Take the time to understand it,
# 	not just copying its implementation.
# 	- This is a new series of challenges called "TOP ALGORITHMS", where we will work with and understand
# 	the most famous ones in history.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

# function to find the partition position
def partition(array, low, high):
	pivot = array[high] # choose the rightmost element as pivot
	i = low - 1 # pointer for greater element
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# if element smaller than pivot is found -> swap it with the greater element pointed by i
			i = i + 1
			# swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])
	# swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	# return the position from where partition is done
	return i + 1

# function to perform quicksort
def quickSort(array, low, high):
	if low < high:
		'''
		find pivot element such that element smaller than pivot are on the left,
		and element greater than pivot are on the right
		'''
		pi = partition(array, low, high)
		# recursive call on the left of pivot
		quickSort(array, low, pi - 1)
		# recursive call on the right of pivot
		quickSort(array, pi + 1, high)
	return array

array = [10, 7, 8, 9, 1, 5]
print(quickSort(array, 0, len(array) - 1))