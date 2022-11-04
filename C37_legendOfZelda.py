# Reto #37
# LOS LANZAMIENTOS DE "THE LEGEND OF ZELDA"
# Fecha publicación enunciado: 14/09/22
# Fecha publicación resolución: 19/09/22
# Dificultad: MEDIA
# 
# Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom"
# y se lanzará el 12 de mayo de 2023.
# Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
# Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
# 	- Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto
# 	puedes usar el mes, o incluso inventártelo)
# 
# Announcement: A new "The Legend of Zelda" has been announced! It will be called "Tears of the Kingdom".
# and it will be released on May 12, 2023.
# But do you remember how much time has passed between the various "The Legend of Zelda" games in history?
# Create a program that calculates how many years and days there are between 2 Zelda games that you select.
# 	- You must search for each of the titles and its release day (if you don't find the exact day
# 	you can use the month, or even make it up).
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

from datetime import date, timedelta

# list of objects with the information of every game
games = [
	{"id": "THE_LEGEND_OF_ZELDA", "name": "The Legend of Zelda", "date": date(1986,2,21)},
    {"id": "THE_ADVENTURE_OF_LINK", "name": "Zelda II: The Adventure of Link", "date": date(1987,1,14)},
    {"id": "A_LINK_TO_THE_PAST", "name": "The Legend of Zelda: A Link to the Past", "date": date(1991,11,21)},
    {"id": "LINKS_AWAKENING", "name": "The Legend of Zelda: Link's Awakening", "date": date(1993,6,6)},
    {"id": "OCARINA_OF_TIME", "name": "The Legend of Zelda: Ocarina of Time", "date": date(1998,11,21)},
    {"id": "MAJORAS_MASK", "name": "Zelda: Majora's Mask", "date": date(2000,4,27)},
    {"id": "ORACLE_OF_SEASONS", "name": "The Legend of Zelda: Oracle of Seasons", "date": date(2011,2,27)},
    {"id": "ORACLE_OF_AGES", "name": "The Legend of Zelda: Oracle of Ages", "date": date(2011,2,27)},
    {"id": "FOUR_SWORDS", "name": "The Legend of Zelda: Four Swords", "date": date(2002,12,3)},
    {"id": "THE_WIND_WAKER", "name": "The Legend of Zelda: The Wind Waker", "date": date(2002,12,13)},
    {"id": "FOUR_SWORDS_ADVENTURES", "name": "The Legend of Zelda: Four Swords Adventures", "date": date(2004,3,18)},
    {"id": "THE_MINISH_CUP", "name": "The Legend of Zelda: The Minish Cap", "date": date(2004,11,4)},
    {"id": "TWILIGHT_PRINCES", "name": "The Legend of Zelda: Twilight Princess", "date": date(2006,11,19)},
    {"id": "PHANTOM_HOURGLASS", "name": "The Legend of Zelda: Phantom Hourglass", "date": date(2007,6,23)},
    {"id": "SPIRIT_TRACKS", "name": "The Legend of Zelda: Spirit Tracks", "date": date(2009,12,7)},
    {"id": "SKYWARD_SWORD", "name": "The Legend of Zelda: Skyward Sword", "date": date(2011,11,18)},
    {"id": "A_LINK_BETWEEN_WORLDS", "name": "The Legend of Zelda: A Link Between Worlds", "date": date(2013,11,23)},
    {"id": "TRI_FORCE_HEROES", "name": "The Legend of Zelda: Tri Force Heroes", "date": date(2015,10,11)},
    {"id": "BREATH_OF_THE_WILD", "name": "The Legend of Zelda:  Breath of the Wild", "date": date(2017,3,3)},
    {"id": "TEARS_OF_THE_KINGDOM", "name": "The Legend of Zelda: Tears of the Kingdom","date": date(2023,5,12)}
]

def timeBetweenRelease(g1, g2):
	# variables
	date1, date2 = 0, 0
	# find and save the date data
	for game in games:
		if game["id"] == g1: date1 = game["date"]
		if game["id"] == g2: date2 = game["date"]
	if date1 == 0 or date2 == 0: return "Couldn't calculate the time..."
	# calculate the time between releases in days
	result = (date1 - date2).days if date1>=date2 else (date2 - date1).days
	# calculate the years
	resultYears = int(result / 365)
	resultDays = int(((result / 365) - int(result / 365)) * 365)
	# find the names of the games
	for game in games:
		if game["id"] == g1: name1 = game["name"]
		if game["id"] == g2: name2 = game["name"]
	# result
	return f"Between '{name1}' and '{name2}' are {resultYears} years and {resultDays} days!"	

print(timeBetweenRelease("THE_LEGEND_OF_ZELDA", "TEARS_OF_THE_KINGDOM"))
print(timeBetweenRelease("TEARS_OF_THE_KINGDOM", "THE_LEGEND_OF_ZELDA"))
print(timeBetweenRelease("THE_LEGEND_OF_ZELDA", "THE_ADVENTURE_OF_LINK"))
print(timeBetweenRelease("THE_ADVENTURE_OF_LINK", "THE_LEGEND_OF_ZELDA"))
print(timeBetweenRelease("THE_LEGEND_OF_ZELDA", "THE_LEGEND_OF_ZELDA"))
print(timeBetweenRelease("ORACLE_OF_SEASONS", "ORACLE_OF_AGES"))