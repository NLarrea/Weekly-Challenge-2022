/*
Reto #0
EL FAMOSO "FIZZ BUZZ"
Fecha publicacion enunciado: 27/12/21
Fecha publicacion resolucion: 03/01/22
Dificultad: FACIL

Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
- Multiplos de 3 por la palabra "fizz".
- Multiplos de 5 por la palabra "buzz".
- Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

Statement: Write a program that displays by console (with a print) the numbers from 1 to 100 (both included and with a line break between each print), substituting the following:
- Multiples of 3 for the word "fizz".
- Multiples of 5 for the word "buzz".
- Multiples of 3 and 5 at the same time for the word "fizzbuzz".

Creador de los retos / Creator of challenges: https://github.com/mouredev
Repositorio original de Mouredev / Original repository: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

for(let i=0; i<=100; i++){
    if(i%3===0 && i%5===0) console.log("fizzbuzz");
    else if(i%3 === 0) console.log("fizz");
    else if(i%5 === 0) console.log("buzz");
    else console.log(i);
}