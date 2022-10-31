/*
Reto #31
AÑOS BISIESTOS
Fecha publicación enunciado: 01/08/22
Fecha publicación resolución: 08/08/22
Dificultad: FÁCIL

Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio.

Statement: Create a function that prints the next 30 leap years following a given one.
- Use the least number of lines to solve the exercise.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function print30LeapYears(year){
	let printed = 0; // to count how many years are printed
	for(let i=0; printed<30; i++){
		// if it is a leap year -> prints the year and updates the counter
		if((year+i)%4===0 && ((year+i)%400===0 || (year+i)%100!==0)){ // => condition to be a leap year
			console.log(`${printed+1}: ${year+i}`);
			printed++;
		}
	}
}

print30LeapYears(1999);
/* prints:
1: 2000 
2: 2004 
3: 2008 
4: 2012 
5: 2016 
6: 2020 
7: 2024 
8: 2028 
9: 2032 
10: 2036 
11: 2040 
12: 2044 
13: 2048 
14: 2052 
15: 2056 
16: 2060 
17: 2064 
18: 2068 
19: 2072 
20: 2076 
21: 2080 
22: 2084 
23: 2088 
24: 2092 
25: 2096 
26: 2104 
27: 2108 
28: 2112 
29: 2116 
30: 2120
*/
print30LeapYears(-500); // BC years
/* prints:
1: -496 
2: -492 
3: -488 
4: -484 
5: -480 
6: -476 
7: -472 
8: -468 
9: -464 
10: -460 
11: -456 
12: -452 
13: -448 
14: -444 
15: -440 
16: -436 
17: -432 
18: -428 
19: -424 
20: -420 
21: -416 
22: -412 
23: -408 
24: -404 
25: -400 
26: -396 
27: -392 
28: -388 
29: -384 
30: -380
*/