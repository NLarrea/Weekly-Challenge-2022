# Reto #30
# MARCO DE PALABRAS
# Fecha publicación enunciado: 26/07/22
# Fecha publicación resolución: 01/08/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
# un marco rectangular de asteriscos.
# - '¿Qué te parece el reto?' Se vería así:
# 	**********
# 	* ¿Qué   *
# 	* te     *
# 	* parece *
# 	* el     *
# 	* reto?  *
# 	**********
# 
# Statement: Create a function that receives a text and displays each word on a line, forming a rectangular asterisk frame.
# a rectangular frame of asterisks.
# - 'What do you think of the challenge?' It would look like this:
# 	**************
# 	* What       *
# 	* do         *
# 	* you        *
# 	* think      *
# 	* of         *
# 	* the        *
# 	* challenge? *
# 	**************
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def drawFrame(string):
	maxWidth = 0 # to save the length of the largest word
	newStr = []
	for word in string.split(" "):
		if len(word)+4 > maxWidth: maxWidth = len(word) + 4
		if word != "": newStr.append(word)
	wordCounter = len(newStr)
	# draw the frame
	for row in range(0, wordCounter+2):
		# code for the first and the last rows
		if row == 0 or row == wordCounter+1: print("*" * maxWidth)
		else:
			# using a while loop because we need to update the 'col' value
			col = 0
			while col <= maxWidth:
				# code for the first and last columns
				if col == 0 or col == maxWidth: print("*", end="")
				# in the second columns the words are printed
				elif col == 2:
					print(newStr[row-1], end="")
					col += len(newStr[row-1]) # col value updates
				# in the rest of the columns we have spaces
				else: print(" ", end="")
				col += 1 # col value updates to avoid creating an infinite loop
			print("") # to jump to the next line

drawFrame("What do you think of the challenge?")
drawFrame("What do             you think of the challenge?")
drawFrame("How many community code challenges have you solved?")
drawFrame("This is gonna be smaller")