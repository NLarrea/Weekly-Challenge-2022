# Reto #27
# VECTORES ORTOGONALES
# Fecha publicación enunciado: 07/07/22
# Fecha publicación resolución: 11/07/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea un programa que determine si dos vectores son ortogonales.
# - Los dos array deben tener la misma longitud.
# - Cada vector se podría representar como un array. Ejemplo: [1, -2]
# 
# Statement: Create a program that determines if two vectors are orthogonal.
# - The two arrays must have the same length.
# - Each vector could be represented as an array. Example: [1, -2]
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def areOrthogonals(arr1, arr2):
	if len(arr1) == len(arr2): return ((arr1[0]*arr2[0] + arr1[1]*arr2[1]) == 0)
	return False

print(areOrthogonals([1, 2], [2, 1])) # False
print(areOrthogonals([2, 1], [-1, 2])) # True