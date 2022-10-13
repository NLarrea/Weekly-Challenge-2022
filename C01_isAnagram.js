/*
Reto #1
¿ES UN ANAGRAMA?
Fecha publicación enunciado: 03/01/22
Fecha publicación resolución: 10/01/22
Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.

Statement: Write a function that receives two words (String) and returns true or false (Boolean) depending on whether they are anagrams or not.
An Anagram consists of forming a word by rearranging ALL the letters of another initial word.
It is NOT necessary to check that both words exist.
Two words that are exactly the same are not anagrams.

Creador de los retos / Creator of challenges: https://github.com/mouredev
Repositorio original de Mouredev / Original repository: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin
*/

function isAnagram(str1="", str2=""){
    if(str1.length !== str2.length) return false; // if their length is not the same, they're not anagrams
    if(str1.toLowerCase() == str2.toLowerCase()) return false; // if they're equals, they're not anagrams
    // to compare arrays
    return str1.toLowerCase().split("").sort().every((value, i) => value === str2.toLowerCase().split("").sort()[i]);
    /* How does this work?
        1. str1 -> lower case
        2. split str1 -> we're gonna create a list from the string
            str1 = "hello" -> str1.split("") gives us: [ 'h', 'e', 'l', 'l', 'o' ]
        3. sort the list
        4. lower case, split and sort the srt2
        5. check if every value from the str1 list is equal to every value of str2 list */
}

console.log(isAnagram("mora", "roma")); // true
console.log(isAnagram("pose", "rose")); // false
console.log(isAnagram("hello", "world")); // false