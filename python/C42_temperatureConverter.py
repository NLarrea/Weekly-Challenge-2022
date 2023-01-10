# Reto #42
# CONVERSOR DE TEMPERATURA
# Fecha publicación enunciado: 17/10/22
# Fecha publicación resolución: 24/10/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
# - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
# - En caso contrario retornará un error.
# 
# Statement: Create a function that transforms degrees Celsius to Fahrenheit and vice versa.
# - For an input data to be correct it must have a symbol "°" and its unit ("C" or "F").
# - Otherwise it will return an error.
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

# imported the library to use regex
import re

def temperatureConverter(degrees):
	# create a regex pattern
	myRegex = re.compile("(\d)(°)(C|F)")
	# replace every white spaces in degrees string with ""
	dSpaces = re.sub("\s", "", degrees)
	try:
		# if the string doesn't match de regex -> it raises an error
		assert re.search(myRegex, dSpaces)
		if dSpaces.endswith("C"): # if the string ends with "C" -> it's in Celsius and must be converted to Fahrenheit
			return f"{((float(re.sub('[ °C]', '', dSpaces)) * 9/5) + 32):.2f}°F"
		else: # if the string doesn't end with "C" -> it's in Fahrenheit and must be converted to Celsius
			return f"{((float(re.sub('[ °F]', '', dSpaces)) - 32) * 5/9):.2f}°C"
	except (AssertionError):
		return "Error: Invalid format!" # error message

print(temperatureConverter("100°C")) # 212.00°F
print(temperatureConverter("100°F")) # 37.78°C
print(temperatureConverter("100C")) # Error: Invalid format!
print(temperatureConverter("100F")) # Error: Invalid format!
print(temperatureConverter("100")) # Error: Invalid format!
print(temperatureConverter("100")) # Error: Invalid format!
print(temperatureConverter("- 100 °C ")) # -148.00°F
print(temperatureConverter("- 100 °F ")) # -73.33°C
print(temperatureConverter("100A°C")) # Error: Invalid format!
print(temperatureConverter("100A°F")) # Error: Invalid format!
print(temperatureConverter("°C")) # Error: Invalid format!
print(temperatureConverter("°F")) # Error: Invalid format!