# Reto #43
# TRUCO O TRATO
# Fecha publicación enunciado: 24/10/22
# Fecha publicación resolución: 02/11/22
# Dificultad: FÁCIL
# 
# Enunciado: Este es un reto especial por Halloween.
# Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y
# un listado (array) de personas con las siguientes propiedades:
# - Nombre de la niña o niño
# - Edad
# - Altura en centímetros
# 
# Si las personas han pedido truco, el programa retornará sustos (aleatorios)
# siguiendo estos criterios:
# - Un susto por cada 2 letras del nombre por persona
# - Dos sustos por cada edad que sea un número par
# - Tres sustos por cada 100 cm de altura entre todas las personas
# - Sustos: 🎃 👻 💀 🕷 🕸 🦇
# 
# Si las personas han pedido trato, el programa retornará dulces (aleatorios)
# siguiendo estos criterios:
# - Un dulce por cada letra de nombre
# - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
# - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
# - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

# imported to get a random element from both scares and candies lists
import random

def trickOrTreat(action, peopleList):
	# constants to save all the scares and candies
	SCARES = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
	CANDIES = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
	result = "" # to save the result as string
	totalHeight = 0 # to calculate the total height of every person from peopleList
	for person in peopleList:
		if action == "TRICK":
			# NAMES -> 1 scare for every two letters of the name per person
			n = 1
			while n < len(person.name):
				result += random.choice(SCARES)
				n += 2
			# AGES -> 2 scares for each age that is multiple of 2
			if person.age % 2 == 0:
				result += random.choice(SCARES) + random.choice(SCARES)
			# HEIGHT -> 3 scares for every 100 cm of height among all persons
			totalHeight += person.height
		elif action == "TREAT":
			# NAMES -> 1 candy for each letter of name
			for char in person.name:
				result += random.choice(CANDIES)
			# AGES -> 1 candy for every three years of age up to a maximum of 10 years per person
			y = 3
			while y <= person.age:
				if y > 10: break
				result += random.choice(CANDIES)
				y += 3
			# HEIGHT -> 2 candies for every 50 cm of height up to a maximum of 150 cm per person
			h = 50
			while h <= person.height:
				if h > 150: break
				result += random.choice(CANDIES) + random.choice(CANDIES)
				h += 50
	if action == "TRICK":
		# 3 scares for every 100 cm of height among all people
		h = 100
		while h <= totalHeight:
			result += random.choice(CANDIES) + random.choice(CANDIES) + random.choice(CANDIES)
			h += 100
	return result

# a class named Person to define every atributes of each person
class Person:
	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height

print(trickOrTreat("TRICK", [
	Person("Naia", 24, 163),
	Person("Cristina", 28, 153),
	Person("Irene", 21, 166),
	Person("June", 24, 172)]));
	# prints: 🎃🕷🦇🕸🎃🦇💀🕷👻🕷🕷🎃🎃👻🕷👻🍫🍰🍫🍭🍰🍪🍭🍰🍬🍫🍬🧁🍭🧁🍰🍪🧁🍡

print(trickOrTreat("TREAT", [
	Person("Naia", 24, 163),
	Person("Cristina", 28, 153),
	Person("Irene", 21, 166),
	Person("June", 24, 172)]));
	# prints: 🍩🧁🍡🍫🍩🍰🍭🍭🍡🍬🍡🍩🧁🍰🍩🍩🍭🍰🍰🍫🍪🧁🍩🧁🧁🍰🍪🍡🍭🍫🍩🍫🍩🍪🍬🍬🍫🍡🍭🍫🍪🍪🍭🧁🍡🍬🧁🍪🍬🍪🍩🧁🍪🍬🍡🍬🍡