# Reto #38
# BINARIO A DECIMAL
# Fecha publicación enunciado: 19/09/22
# Fecha publicación resolución: 27/09/22
# Dificultad: MEDIA
# 
# Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
# funciones propias del lenguaje que lo hagan directamente.
# 
# Statement: Create a program to transform a binary number into a decimal number without using
# language functions that do it directly.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

import re # library to use regex

def binaryToDecimal(binStr):
	binStr = binStr.replace(" ", "")
	# check if there are only '0' and '1' in the string if it exists
	if binStr:
		result = re.findall(r"[^0-1]", binStr, re.MULTILINE)
	# if it is an empty string, return None
	else: return None
	# if the regex result has a match -> return None
	if result: return None
	# calculate the decimal number of the binStr
	decimal, index = 0, 0
	for digit in reversed(binStr):
		decimal += int(digit) * (2**index)
		index += 1
	return decimal

print(binaryToDecimal("00110")) # 6
print(binaryToDecimal("01100")) # 12
print(binaryToDecimal("000000000")) # 0
print(binaryToDecimal("00210")) # None
print(binaryToDecimal("001101001110")) # 846
print(binaryToDecimal("00b10")) # None
print(binaryToDecimal("")) # None
print(binaryToDecimal("-00110")) # None
print(binaryToDecimal(" ")) # None
print(binaryToDecimal(" 10011")) # 19
print(binaryToDecimal("1O1OO11")) # None