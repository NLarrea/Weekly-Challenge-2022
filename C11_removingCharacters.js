/*
Reto #11
ELIMINANDO CARACTERES
Fecha publicación enunciado: 14/03/22
Fecha publicación resolución: 21/03/22
Dificultad: FÁCIL

Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

Statement: Create a function that receives two strings as parameters (str1, str2) and prints two other strings as output (out1, out2).
- out1 will contain all characters present in str1 but NOT present in str2.
- out2 will contain all characters present in str2 but NOT present in str1.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function printNonCommon(str1, str2){
	// create two strings -> if one doesn't contain c, includes c to the other one
	let out1 = str1.split("").filter(c => !(str2.split("").includes(c))).toString();
	let out2 = str2.split("").filter(c => !(str1.split("").includes(c))).toString();
	// to print the strings
	console.log(`out1: ${out1}`);
	console.log(`out2: ${out2}`);
}

printNonCommon("naia", "larrea");
printNonCommon("I like Javascript", "I like Python");
printNonCommon("In my spare time I often learn new things about programming", "I am also a rugby player and referee");