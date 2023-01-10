/*
Reto #42
CONVERSOR DE TEMPERATURA
Fecha publicación enunciado: 17/10/22
Fecha publicación resolución: 24/10/22
Dificultad: FÁCIL

Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
- Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
- En caso contrario retornará un error.

Statement: Create a function that transforms degrees Celsius to Fahrenheit and vice versa.
- For an input data to be correct it must have a symbol "°" and its unit ("C" or "F").
- Otherwise it will return an error.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function temperatureConverter(degrees){
	let myRegex = /(\d)(°)(C|F)/g; // regex pattern to check the format: NUMBER°C or NUMBER°F
	try{
		if(!myRegex.test(degrees.replace(/ /g, ""))) throw new Error("Invalid values!");
		let dNum = degrees.trim().replace(/[ °C]/, ""); // gets the number of the degrees
		if(dNum.endsWith("C")){
			// if the string ends with "C" -> it's in Celsius and must be converted to Fahrenheit
			return `${((parseFloat(dNum) * 9/5) + 32).toFixed(2)}°F`;
		} else {
			// if the string doesn't end with "C" -> it's in Fahrenheit and must be converted to Celsius
			return `${((parseFloat(dNum) - 32) * 5/9).toFixed(2)}°C`;
		}
	} catch(err){
		return err; // error message
	}
}

console.log(temperatureConverter("100°C")); // 212.00°F
console.log(temperatureConverter("100°F")); // 37.78°C
console.log(temperatureConverter("100C")); // [Error: Invalid values!]
console.log(temperatureConverter("100F")); // [Error: Invalid values!]
console.log(temperatureConverter("100")); // [Error: Invalid values!]
console.log(temperatureConverter("100")); // [Error: Invalid values!]
console.log(temperatureConverter("- 100 °C ")); // -148.00°F
console.log(temperatureConverter("- 100 °F ")); // -73.33°C
console.log(temperatureConverter("100A°C")); // [Error: Invalid values!]
console.log(temperatureConverter("100A°F")); // [Error: Invalid values!]
console.log(temperatureConverter("°C")); // [Error: Invalid values!]
console.log(temperatureConverter("°F")); // [Error: Invalid values!]