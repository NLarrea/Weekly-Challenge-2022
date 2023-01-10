/*
Reto #33
CICLO SEXAGENARIO CHINO
Fecha publicación enunciado: 15/08/22
Fecha publicación resolución: 22/08/22
Dificultad: MEDIA

Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
en el ciclo sexagenario del zodíaco chino.
- Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
- El ciclo sexagenario se corresponde con la combinación de los elementos madera,
  fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
  caballo, oveja, mono, gallo, perro, cerdo (en este orden).
- Cada elemento se repite dos años seguidos.
- El último ciclo sexagenario comenzó en 1984 (Madera Rata).

Statement: Create a function that, given a year, indicates the corresponding element and animal in the sexagenary cycle of the Chinese zodiac.
in the sexagenary cycle of the Chinese zodiac.
- Information: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
- The sexagenary cycle corresponds to the combination of the elements wood,
  fire, earth, metal, water and the animals rat, ox, tiger, rabbit, dragon, snake,
  horse, sheep, monkey, rooster, dog, pig (in that order).
- Each element is repeated two years in a row.
- The last sexagenarian cycle began in 1984 (Wood Rat).

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/


function chineseZodiac(year){
	// create two lists with the year options
	const elements = ["Wood", "Fire", "Earth", "Metal", "Water"];
	const animals = ["Rat", "Ox", "Tiger", "Rabit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"];
	// the year must be at least 604
	if(year < 604) return "The sexagenary cycle started on 604.";
	// calculate the results
	let sexagenayYear = parseInt((year - 4) % 60);
	let element = elements[parseInt((sexagenayYear % 10) / 2)];
	let animal = animals[parseInt(sexagenayYear % 12)];
	// return the result
	return `${year}: ${animal} ${element}`;
}

console.log(chineseZodiac(1924)); // 1924: Rat Wood
console.log(chineseZodiac(1946)); // 1946: Dog Fire
console.log(chineseZodiac(1984)); // 1984: Rat Wood
console.log(chineseZodiac(604)); // 604: Rat Wood
console.log(chineseZodiac(603)); // The sexagenary cycle started on 604.
console.log(chineseZodiac(1987)); // 1987: Rabit Fire
console.log(chineseZodiac(2022)); // 2022: Tiger Water