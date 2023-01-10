/*
Reto #15
¿CUÁNTOS DÍAS?
Fecha publicación enunciado: 11/04/22
Fecha publicación resolución: 18/04/22
Dificultad: DIFÍCIL

Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

Statement: Create a function that calculates and returns how many days there are between two strings representing dates.
- A string representing a date has the format "dd/MM/yyyy".
- The function will receive two Strings and return an Int.
- The difference in days will be absolute (the order of the dates does not matter).
- If one of the two strings does not represent a correct date an exception will be thrown.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function daysBetween(str1, str2){
	const regFormat = /^([0-9]){2}[\/]([0-9]){2}[\/]([0-9]){4}/; // to check the format of the strings
	try{
		// if the formatting is not correct in at least one of the strings -> throws an error
		if(!(regFormat.test(str1)) || !(regFormat.test(str2))) throw new Error("Incorrect date format!");
	}
	catch(err){
		return(err); // catches and returnes the error thrown by the "throw new Error()"
	}
	// if there's no error -> saves the values of the strings in variables of type date
	const date1 = new Date(str1.split("/")[2], str1.split("/")[1]-1, str1.split("/")[0]);
	const date2 = new Date(str2.split("/")[2], str2.split("/")[1]-1, str2.split("/")[0]);
	// calculates the milliseconds between the two dates, then converts it to days
	const diff = Math.abs(date1.getTime() - date2.getTime()) / 1000 / 3600 / 24;
	return diff; // returns the result
}

console.log(daysBetween("18/05/2022", "29/05/2022")); // 11 -> OK
console.log(daysBetween("NLarrea", "29/04/2022")); // [Error: Incorrect date format!]
console.log(daysBetween("18/5/2022", "29/04/2022")); // [Error: Incorrect date format!]
// the last one = error -> because the statement says that the format must have two digits in the month