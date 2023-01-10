/*
Reto #19
CONVERSOR TIEMPO
Fecha publicación enunciado: 09/05/22
Fecha publicación resolución: 16/05/22
Dificultad: FACIL

Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.

Statement: Create a function that receives days, hours, minutes and seconds (as integers) and returns its result in milliseconds.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function toMillis(days, hours, minutes, seconds){
	const daysToMillis = days * 24 * 60 * 60 * 1000;
	const hoursToMillis = hours * 60 * 60 * 1000;
	const minutesToMillis = minutes * 60 * 1000;
	const secondsToMillis = seconds * 1000;
	return daysToMillis + hoursToMillis + minutesToMillis + secondsToMillis;
}

console.log(toMillis(0,0,0,10)); // 10000
console.log(toMillis(2,5,-45,10)); // 188110000
console.log(toMillis(2000000000,5,45,10)); // 172800000020710000