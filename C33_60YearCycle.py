# Reto #33
# CICLO SEXAGENARIO CHINO
# Fecha publicación enunciado: 15/08/22
# Fecha publicación resolución: 22/08/22
# Dificultad: MEDIA
# 
# Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
# en el ciclo sexagenario del zodíaco chino.
# - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
#   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
#   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
# - Cada elemento se repite dos años seguidos.
# - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
# 
# Statement: Create a function that, given a year, indicates the corresponding element and animal in the sexagenary cycle of the Chinese zodiac.
# in the sexagenary cycle of the Chinese zodiac.
# - Information: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# - The sexagenary cycle corresponds to the combination of the elements wood,
#   fire, earth, metal, water and the animals rat, ox, tiger, rabbit, dragon, snake,
#   horse, sheep, monkey, rooster, dog, pig (in that order).
# - Each element is repeated two years in a row.
# - The last sexagenarian cycle began in 1984 (Wood Rat).
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

def chineseZodiac(year):
	# create constants with the possible values
	ELEMENTS = ("Wood", "Fire", "Earth", "Metal", "Water")
	ANIMALS = ("Rat", "Ox", "Tiger", "Rabit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig")
	# check if year is correct
	if year < 604: return "The first sexagenary year was 604."
	# calculate the result
	sexagenaryYear = (year - 4) % 60
	element = ELEMENTS[int((sexagenaryYear % 10) / 2)]
	animal = ANIMALS[int(sexagenaryYear % 12)]
	# return the result
	return "{0}: {1} {2}".format(year, animal, element)


print(chineseZodiac(1924)) # 1924: Rat Wood
print(chineseZodiac(1946)) # 1946: Dog Fire
print(chineseZodiac(1984)) # 1984: Rat Wood
print(chineseZodiac(604)) # 604: Rat Wood
print(chineseZodiac(603)) # The sexagenary cycle started on 604.
print(chineseZodiac(1987)) # 1987: Rabit Fire
print(chineseZodiac(2022)) # 2022: Tiger Water