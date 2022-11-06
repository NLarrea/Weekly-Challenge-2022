/*
Reto #39
TOP ALGORITMOS: QUICK SORT
Fecha publicación enunciado: 27/09/22
Fecha publicación resolución: 03/10/22
Dificultad: MEDIA

Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",
creado por C.A.R. Hoare.
	- Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a 
	mejorar nuestro conocimiento sobre ingeniería de software. Dedícale tiempo a entenderlo,
	no únicamente a copiar su implementación.
	- Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos
	los más famosos de la historia.

Statement: Implements one of the most famous sorting algorithms: the "Quick Sort",
created by C.A.R. Hoare.
	- Understanding the operation of the most used algorithms in history helps us to improve our knowledge of software engineering. 
	improve our knowledge of software engineering. Take the time to understand it,
	not just copying its implementation.
	- This is a new series of challenges called "TOP ALGORITHMS", where we will work with and understand
	the most famous ones in history.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function quickSort(array, first = 0, last = array.length-1){
	if(array.length === 0) return array; // if array is empty, returns it
	// variables
	let i = first;
	let j = last;
	let pivot = parseInt((array[i] + array[j]) / 2);
	// sorting the array
	while(i < j){
		while(array[i] < pivot){
			i++;
		}
		while(array[j] > pivot){
			j--;
		}
		if(i <= j){
			let aux = array[j];
			array[j] = array[i];
			array[i] = aux;
			i++;
			j--;
		}
	}
	if(first < j) quickSort(array, first, j);
	if(last > i) quickSort(array, i, last);
	return array;
}

console.log(quickSort([3, 5, 1, 8, 9, 0])); // [ 0, 1, 3, 5, 8, 9 ]
console.log(quickSort([])); // []
