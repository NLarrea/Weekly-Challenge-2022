/*
Reto #35
BATALLA POKÉMON
Fecha publicación enunciado: 29/08/22
Fecha publicación resolución: 06/09/22
Dificultad: MEDIA

Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
- La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
- Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
- Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
- El programa recibe los siguientes parámetros:
	- Tipo del Pokémon atacante.
	- Tipo del Pokémon defensor.
	- Ataque: Entre 1 y 100.
	- Defensa: Entre 1 y 100.

Statement: Create a program that calculates the damage of an attack during a Pokémon battle.
- The formula will be as follows: damage = 50 * (attack / defense) * effectiveness
- Effectiveness: x2 (super effective), x1 (neutral), x0.5 (not very effective)
- There are only 4 types of Pokémon: Water, Fire, Plant and Electric (look for their effectiveness).
- The program receives the following parameters:
	- Type of the attacking Pokémon.
	- Type of the defending Pokémon.
	- Attack: Between 1 and 100.
	- Defense: Between 1 and 100.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

const pokemonType = ("WATER", "FIRE", "GRASS", "ELECTRIC");
const typeChart = {
	"WATER": ["FIRE", "GRASS"],
	"FIRE":["GRASS", "WATER"],
	"GRASS":["WATER", "FIRE"],
	"ELECTRIC": ["WATER", "GRASS"]
}

function battle(attacker, defender, attack, defense){
	if(attack<=0 || attack>100 || defense<=0 || defense>100) return "The attack and the defense values must be between 1 and 100!";
	let effectivity = 1;
	if(attacker === defender || typeChart[attacker][1]===defender){
		effectivity = 0.5;
		console.log("Not very effective...");
	} else if(typeChart[attacker][0]===defender){
		effectivity = 2;
		console.log("Super effective!");
	} else {
		console.log("Neutral");
	}
	return parseInt(50 * ((attack**2) / (defense**2)) * effectivity);
}

console.log(battle("WATER", "FIRE", 50, 30)); // 277
console.log(battle("WATER", "FIRE", 101, -10)); // The attack and the defense values must be between 0 and 100!
console.log(battle("FIRE", "WATER", 50, 30)); // 69
console.log(battle("FIRE", "FIRE", 50, 30)); // 69
console.log(battle("GRASS", "ELECTRIC", 30, 50)); // 18