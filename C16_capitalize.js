/*
Reto #16
EN MAYÚSCULA
Fecha publicación enunciado: 18/04/22
Fecha publicación resolución: 25/04/22
Dificultad: FÁCIL

Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

Statement: Create a function that receives a String of any type and is responsible
for capitalizing the first letter of each word.
- You cannot use language operations that solve it directly.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function capitalize(str){
	let result = ""; // empty string to save the result
	// to know when we have to capitalize a char. It starts being true because the first char must be capitalized
	let nextIsUpper = true;
	for(c of str){
		if(nextIsUpper) result += c.toUpperCase();
		else result += c;
		// if the char match one of these, next char must be capitalized
		nextIsUpper = /[^A-z0-9ñÑ]/g.test(c);
	}
	console.log(result);
}

capitalize("Hi, how are you?");
capitalize("Hi           how are you?");
capitalize("el niño ñoño")