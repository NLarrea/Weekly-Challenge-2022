/*
Reto #14
¿ES UN NÚMERO DE ARMSTRONG?
Fecha publicación enunciado: 04/04/22
Fecha publicación resolución: 11/04/22
Dificultad: FÁCIL

Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

Statement: Write a function that calculates whether a given number is an Armstrong (or narcissistic) number.
If you do not know what an Armstrong number is, you should look for information about it.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function isNarcissist(number){
	if(number < 0) return false; // negative numbers aren't Armstrong's numbers
	let nDigits = number.toString().length; // to calculate the number of digits of each number
	let sum = 0; // initial value for sum
	// equation to check if it is an Armstrong number
	number.toString().split("").forEach(n => sum += parseInt(n) ** nDigits);
	// result
	if(number === sum) return true;
	return false;
}

console.log(isNarcissist(371)); // true
console.log(isNarcissist(-371)); // false
console.log(isNarcissist(372)); // false
console.log(isNarcissist(0)); // true