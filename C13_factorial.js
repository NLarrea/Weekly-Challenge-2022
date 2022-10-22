/*
Reto #13
FACTORIAL RECURSIVO
Fecha publicación enunciado: 28/03/22
Fecha publicación resolución: 04/04/22
Dificultad: FÁCIL

Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

Statement: Write a function that calculates and returns the factorial of a given number recursively.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function factorial(num){
	if(num === 1) return 1
	return num * factorial(num - 1);
}

console.log(factorial(5));
console.log(factorial(10));