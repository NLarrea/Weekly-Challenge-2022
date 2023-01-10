# Reto #26
# CUADRADO Y TRIÁNGULO 2D
# Fecha publicación enunciado: 27/06/22
# Fecha publicación resolución: 07/07/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
# - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
# - EXTRA: ¿Eres capaz de dibujar más figuras?
# 
# Statement: Create a program that draws a square or a triangle with asterisks "*".
# - We will indicate the size of the side and whether the figure to be drawn is one or the other.
# - EXTRA: Are you able to draw more figures?
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def drawPolygon(size, type):
	if size < 2: print("Size must be bigger than 1.")
	for value in range(0, size):
		if type == "square":
			for n in range(0, size):
				print("* ", end="")
		elif type == "triangle":
			for n in range(0, value+1):
				print("* ", end="")
		print("")

drawPolygon(10, "square")
drawPolygon(15, "triangle")