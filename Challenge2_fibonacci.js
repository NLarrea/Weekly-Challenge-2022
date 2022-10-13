/*
Reto #2
LA SUCESIÓN DE FIBONACCI
Fecha publicación enunciado: 10/01/22
Fecha publicación resolución: 17/01/22
Dificultad: DIFÍCIL

Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...

Statement: Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
The Fibonacci series consists of a sequence of numbers in which the next number is always the sum of the previous two.
0, 1, 1, 2, 3, 5, 8, 13...

Creador de los retos / Creator of challenges: https://github.com/mouredev
Repositorio original de Mouredev / Original repository: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

// fibonacci function
function fib(i, f1, f2){
    if(i === 0) return 0; // if it's the first fibonacci (i=0), returns 0
    else if(i === 1) return 1; // if it's the second fibonacci (i=1), returns 1
    return f1 + f2; // else, returns the sum of the previous two
}

// we create the previous fibonacci and the one before the previous one
let fib1 = 0;
let fib2 = 0;
// loop to print all the fibonaccis
for(let i=0; i<=50; i++){
    let actualFib = fib(i, fib1, fib2); // uses the function to calculate the actual fibonacci
    console.log(actualFib); // prints the actual fibonacci
    // updates the values
    fib2 = fib1;
    fib1 = actualFib;
}