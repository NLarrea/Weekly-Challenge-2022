/*
Reto #3
¿ES UN NÚMERO PRIMO?
Fecha publicación enunciado: 17/01/22
Fecha publicación resolución: 24/01/22
Dificultad: MEDIA

Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.

Statement: Write a program that checks if a number is a prime number or not.
With this done, print the prime numbers between 1 and 100.

Creador de los retos semanales: https://github.com/mouredev
Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function isPrime(n){
    // if the number is divisible by other -> not a prime number -> return false
    for(let i=2;i<n;i++) if(n%i === 0) return false;
    // if n is not divisible it is a prime number -> send it to be printed
    return n;
}

for(let i=1;i<=100;i++) if(isPrime(i)) console.log(i);