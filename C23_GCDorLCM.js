/*
Reto #23
MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
Fecha publicación enunciado: 07/06/22
Fecha publicación resolución: 13/06/22
Dificultad: MEDIA

Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo
(mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

Statement: Create two functions, one that computes the greatest common divisor (GCD) and one that computes the least common 
multiple (LCM) of two integers.
- You cannot use language operations that solve it directly.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function greatCommonDivisor(n1, n2){
	while(n1!==0 && n2!==0){
		let aux = n2;
		n2 = n1 % n2;
		n1 = aux;
	}
	return n1 + n2;
}

function leastCommonMultiple(n1, n2){
	return parseInt((n1 * n2) / greatCommonDivisor(n1, n2));
}

console.log(greatCommonDivisor(180,56)); // 4
console.log(leastCommonMultiple(56,180)); // 2520