/*
Reto #38
BINARIO A DECIMAL
Fecha publicación enunciado: 19/09/22
Fecha publicación resolución: 27/09/22
Dificultad: MEDIA

Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
funciones propias del lenguaje que lo hagan directamente.

Statement: Create a program to transform a binary number into a decimal number without using
language functions that do it directly.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function binaryToDecimal(binStr){
	let result;
	// if it's not an empty string, it checks its values
	if(binStr.trim()) result = /[^0-1]/g.test(binStr.trim()) // check if the binStr has a value other than '0' or '1'
	/* used .trim() to calculate the result of numbers when they have spaces at the beginning or end (" 10011"), but
	don't take in count those strings that are only a white space (" ") */
	else result = true; // means that the binStr is empty -> return null
	if(result === true) return null
	// transforms the binary number to decimal
	let decimal = 0
	binStr.split("").reverse().forEach((digit, index) => decimal += digit * (2**index));
	return decimal;
}

console.log(binaryToDecimal("00110")); // 6
console.log(binaryToDecimal("01100")); // 12
console.log(binaryToDecimal("000000000")); // 0
console.log(binaryToDecimal("00210")); // null
console.log(binaryToDecimal("001101001110")); // 846
console.log(binaryToDecimal("00b10")); // null
console.log(binaryToDecimal("")); // null
console.log(binaryToDecimal("-00110")); // null
console.log(binaryToDecimal(" ")); // null
console.log(binaryToDecimal(" 10011")); // 19
console.log(binaryToDecimal("1O1OO11")); // null