/*
Reto #20
PARANDO EL TIEMPO
Fecha publicación enunciado: 16/05/22
Fecha publicación resolución: 23/05/22
Dificultad: MEDIA

Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
- Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.

Statement: Create a function that adds 2 numbers and returns the result after a few seconds.
- It will receive as parameters the 2 numbers to add and the seconds it should take to finish its execution.
- If the language supports it, it must return the result asynchronously, that is, without stopping the execution of the main program. It could be executed several times at the same time.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

// create a function that receives two numbers and time in seconds
function asyncAdd(n1, n2, sec){
	// this function will return a Promise object with the result (or error if something go wrong)
	return new Promise((resolve, reject) => {
		setTimeout(() => {
			if(n1===undefined || n2===undefined) reject(new Error("Numbers not defined")); // this shouldn't be executed
			resolve(n1+n2); // to return the result
		}, sec * 1000); // to wait sec*1000 milliseconds
	})
}

// as we get the Promise object, to print the result we need to use .then()
asyncAdd(5, 2, 10).then((result) => console.log(result));
asyncAdd(1, 3, 5).then((result) => console.log(result));