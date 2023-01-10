/*
Reto #36
LOS ANILLOS DE PODER
Fecha publicación enunciado: 06/09/22
Fecha publicación resolución: 14/09/22
Dificultad: MEDIA

Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron
contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
Cada raza tiene asociado un "valor" entre 1 y 5:
- Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
- Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
- El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la
  suma del valor del ejército y el número de integrantes.
- Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
- Tienes total libertad para modelar los datos del ejercicio.
Ej: 1 Peloso pierde contra 1 Orco, 2 Pelosos empatan contra 1 Orco, 3 Pelosos ganan a 1 Orco.

Plot: Middle-earth is at war! In it will fight races loyal to Sauron
against other kind races that do not want evil to reign over their lands.
Each race has an associated "value" between 1 and 5:
- Kindly races: Harfeet (1), Good Southerners (2), Dwarves (3), Númenóreans (4), Elves (5).
- Evil Races: Evil Southerners (2), Orcs (2), Goblins (2), Wargs (3), Trolls (5)
Create a program that calculates the outcome of the battle between the 2 types of armies:
- The result can be that good wins, evil wins, or there is a draw. Depending on the
  Depending on the sum of the value of the army and the number of members.
- Each army can be composed of a variable number of members of each race.
- You have total freedom to model the exercise data.
Ex: 1 Hairy loses against 1 Orc, 2 Hairy draw against 1 Orc, 3 Hairy win against 1 Orc.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

const kindRaces = {
	harfoot: 1,
	southerner: 2,
	dwarf: 3,
	numenorean: 4,
	elf: 5
}

const evilRaces = {
	southerner: 2,
	orc: 2,
	goblin: 2,
	warg: 3,
	troll: 5
}

function battleForTheMiddleEarth(kindArmy, evilArmy){
	let kindPoints=0, evilPoints=0;
	// KIND POINTS
	// if there's only 1 kind of creature
	if(typeof kindArmy[0] === "number") kindPoints = kindArmy[0] * kindArmy[1];
	// if there're more than 1 kind of creatures
	else{
		kindArmy.forEach(element => {
			kindPoints += element[0] * element[1];
		})
	}
	// EVIL POINTS
	// if there's only 1 kind of creature
	if(typeof evilArmy[0] === "number") evilPoints = evilArmy[0] * evilArmy[1];
	// if there're more than 1 kind of creatures
	else{
		evilArmy.forEach(element => {
			evilPoints += element[0] * element[1];
		})
	}
	// WHO WINS
	if(kindPoints > evilPoints) return "Good wins!";
	else if(kindPoints < evilPoints) return "Evil wins...";
	else return "There is a tie";
}

console.log(battleForTheMiddleEarth(
	[kindRaces.elf, 1],
	[evilRaces.troll, 1]));
// There is a tie

console.log(battleForTheMiddleEarth(
	[[kindRaces.elf, 1], [kindRaces.harfoot, 1]],
	[evilRaces.troll, 1]));
// Good wins!

console.log(battleForTheMiddleEarth(
	[[kindRaces.elf, 1], [kindRaces.harfoot, 1]],
	[[evilRaces.troll, 1], [evilRaces.orc, 1]]));
// Evil wins...

console.log(battleForTheMiddleEarth(
	[[kindRaces.elf, 56], [kindRaces.harfoot, 80], [kindRaces.dwarf, 5]],
	[[evilRaces.troll, 17], [evilRaces.orc, 51], [evilRaces.warg, 10], [evilRaces.southerner, 2]]));
// Good wins!