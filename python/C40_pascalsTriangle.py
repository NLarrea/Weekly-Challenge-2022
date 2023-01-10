# Reto #40
# TRIÁNGULO DE PASCAL
# Fecha publicación enunciado: 03/10/22
# Fecha publicación resolución: 10/10/22
# Dificultad: MEDIA
# 
# Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
# únicamente el tamaño del lado.
# - Aquí puedes ver rápidamente cómo se calcula el triángulo:
#   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
# 
# Statement: Create a function that is able to draw the "Pascal's Triangle" by giving only the size of the side.
# only the size of the side.
# - Here you can quickly see how the triangle is calculated:
#   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def pascalTriangle(size):
	lastRow = [] # empty list to save last row's values
	for row in range(0, size):
		currentRow = [] # empty list to save the current row's values
		triangleRow = "" # empty string to save the current row's values and print them
		for element in range(0, row+1):
			if element>=1 and element<row:
				value = lastRow[element-1] + lastRow[element]
				triangleRow += f"{value} "
				currentRow.append(value)
			else:
				triangleRow += "1 "
				currentRow.append(1)
		print(" "*(size-row) + triangleRow)
		lastRow = currentRow

pascalTriangle(5)
''' prints:
     1  
    1 1  
   1 2 1  
  1 3 3 1  
 1 4 6 4 1
'''
pascalTriangle(1) # prints: 1
pascalTriangle(0) # nothing is printed
pascalTriangle(-5) # nothing is printed